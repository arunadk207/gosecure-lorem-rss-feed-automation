import requests
import unittest
import xml.etree.ElementTree as ET
import logging
import os

class LoremRssFeedTest(unittest.TestCase):
    
    BASE_API_URL = "https://lorem-rss.herokuapp.com/feed"
    
    def getResponse(self, params):
       
        response = requests.get(self.BASE_API_URL, params=params)
        return response
    
    def test_api_url_invalid(self):
        params = {}
        self.BASE_API_URL = "https://lorem1-rss.herokuapp.com/feed"
        response = self.getResponse(params)
        assert response.status_code == 404
    
    def test_status_code(self):
        params = {}
        response = self.getResponse(params)
        assert response.status_code == 200
    
    def test_feed(self):
        params = {}
        response = self.getResponse(params)
        root = ET.fromstring(response.content)
        print(response.content)
        title = root.findtext("./channel/title")
        '''Consider title tag alone to test, can follow same pattern to test other tags in the response '''
        assert bool(response and response.content and response.content.strip()) == True
        assert title == "Lorem ipsum feed for an interval of 1 minutes with 10 item(s)"
    
    def test_feed_with_params(self):
        params = {'unit':'second', 'interval': '30'}
        response = self.getResponse(params)
        root = ET.fromstring(response.content)
        title = root.findtext("./channel/title")
        assert bool(response and response.content and response.content.strip()) == True
        assert title == "Lorem ipsum feed for an interval of 30 seconds with 10 item(s)"
    
