# -*- coding: utf8 -*-
import requests

class handler(BaseHTTPRequestHandler):

def main_handler(event, context):
    r = requests.post("https://api.github.com/repos/Zfour/my-blog-source-file/dispatches",
    json = {"event_type": "run-it"},
    headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': 'token 19424a8773ae35f324bd470f934f14a774d5382e'})
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code