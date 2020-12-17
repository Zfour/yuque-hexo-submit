# -*- coding: utf8 -*-
from http.server import BaseHTTPRequestHandler
import requests
def handler(event, context):
    r = requests.post("https://api.github.com/repos/Zfour/my-blog-source-file/dispatches",
    json = {"event_type": "run-it"},
    headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': 'token 325b0fef4d80cfb4ff06c38507d9c1f7149c3bf9'})
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code