#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 2.7.6

# pip install beautifulsoup selenium

"""
  A simple script to crawl pages of given url using a 
  headless browser and getting the page load stats

  Usage: python zavadanak.py https://www.sonsuzdongu.com
"""

import os
import sys

from BeautifulSoup import BeautifulSoup
from urlparse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TODO: update that path
chromeDriverPath = "/usr/bin/chromedriver"

options = Options()
options.headless = True


def crawl_urls(driver, already_crawled_urls, url, domain):
    url_list = list()
    already_crawled_urls.append(url)

    driver.get(url)

    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
    fetchStart = driver.execute_script("return window.performance.timing.fetchStart")
    domInteractive = driver.execute_script("return window.performance.timing.domInteractive")
    loadEventStart = driver.execute_script("return window.performance.timing.loadEventStart")

    ttfb = responseStart - fetchStart
    domReady = ttfb + domInteractive - responseStart
    pageLoad = ttfb + loadEventStart - responseStart

    print("\n---------\n")
    print("URL: %s" % url)
    print("TTFB: %d" % ttfb)
    print("Dom ready: %d" % domReady)
    print("Page load: %d" % pageLoad)

    html = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(html)
    urls = soup.findAll("a")

    for a in urls:
        if (a.get("href")) and urlparse(a.get("href")).netloc == domain :
            url_list.append(a.get("href"))

    # remove duplicates
    for page in set(url_list):
        if (page not in already_crawled_urls):
            crawl_urls(driver, already_crawled_urls, page, domain)

    else:
        return already_crawled_urls, url_list


if __name__ == "__main__":
    try:
        parent_url = sys.argv[1]
        print ("Crawling : %s" % parent_url)
    except :
        print ("You need to send a base url")
        sys.exit(1)
    try:
        domain = urlparse(parent_url).netloc
        if not domain:
            raise
    except: 
        print ("Not a valid url")
        sys.exit(1)

    driver = webdriver.Chrome(executable_path=chromeDriverPath,   options=options)  

    already_crawled_urls = list()
    already_crawled_urls = crawl_urls(driver, already_crawled_urls, parent_url, domain)
    driver.quit()
