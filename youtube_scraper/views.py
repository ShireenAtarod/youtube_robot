import os
import json
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .models import Channel
from .forms import ChannelForm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def index(request):
    form = ChannelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            keyWord = form.cleaned_data['keyword']

            scrap(request, keyWord)

    return render(request, 'youtube_scraper.html', context)




def scrap(request, keyWord):
    print(keyWord)
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get(f"https://youtube.com/results?search_query={keyWord}&sp=EgIQAg%253D%253D")
    driver.maximize_window()

    # Reject all coockies
    try:
        rejectCockies = driver.find_element("xpath", '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button')
        if rejectCockies:
            rejectCockies.click()
    except:
        pass

    # Find Channels Info
    channelLinks = []
    channelSubs = []
    while len(channelLinks) < 100:
        #scroll window
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        channelLinks.extend(driver.find_elements("xpath", '//*[@id="main-link"]'))
        channelSubs.extend(driver.find_elements("xpath", '//*[@id="video-count"]'))
    
    results = {
        "keyWord": keyWord,
        "data": []
    }

    for i in range(100):
        link = channelLinks[i].get_attribute('href')
        subscriber_no = channelSubs[i].text.split(' ')[0]
        info = {
            'link': link,
            'subscribers': subscriber_no 
        }
        results["data"].append(info)

        channel = Channel(link=link, subscriber=subscriber_no, keyword=keyWord)
        channel.save()

    save_file = open("savedata.json", "w")  
    json.dump(results, save_file, indent = 6)  
    save_file.close()  

    # response = HttpResponse(save_file.read(), content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename=savedata.json'


