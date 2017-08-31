from django.shortcuts import render, render_to_response, HttpResponse
import requests
import json
from datetime import datetime 

# url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=5922265149.1677ed0.6f5dd6496f3b4402a8df0ef2015fcf05'

def grabber(request):
    jsonList = []
    req = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=5922265149.1677ed0.6f5dd6496f3b4402a8df0ef2015fcf05')
    jsonList.append(json.loads(req.content))
    userData = {}
    userData1 = {}
    parsedData1 = []
    parsedData = []
    for data in jsonList:
        userData = data['data'] # [0]['images']['standard_resolution']['url']
    parsedData1.append(userData)
    
    for index in range(len(parsedData1)):
        for x in parsedData1[index]:
            x1 = {}
            x2 = {}
            x3 = {}
            x1['tags'] = x['tags']
            x2['url'] = x['images']['standard_resolution']['url']
            x3['post'] = {**x1, **x2}
            parsedData.append(x3)
    return render_to_response('grabber/grabber.html', {'parsedData':parsedData})
    # return HttpResponse(parsedData)