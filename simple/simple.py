#!/usr/bin/env python3

event = {
"headers" : {
    "accept" : "*/*",
    "content-type" : "application/json",
    "Host" : "api.dev.abbeyroad.yotra.io",
    "User-Agent" : "curl/7.79.1",
    "X-Forwarded-For" :"17.69.195.86",
    "x-requestid" : "9870d943-5df9-4339-bb3b-4a4c49dd4163"
    }
}

if 'headers' in event and event['headers']:
    if 'x-requestId'.lower() in (header.lower() for header in event['headers'].keys()):

        for header in event['headers'].keys():
            if 'x-requestId'.lower() == header.lower():
                apple_header = event["headers"][header]
                print("apple_header = " + apple_header)
    else:
            error_message = "no x-requestId in event[headers]"
            print("error_message: " + error_message)
