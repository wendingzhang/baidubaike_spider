# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 19:51:29 2016

@author: wending.zhang
"""
import urllib2
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
            
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
        