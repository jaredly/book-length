#!/usr/bin/env python

import random
import urllib
import time

def sample(number, total_pages=13572592/20):
    pages_to_get = []
    print "getting", number, "of", total_pages
    while len(pages_to_get) < number:
        i = random.randrange(1, total_pages)
        if i not in pages_to_get:
            pages_to_get.append(i)
    print "have my numbers"
    return pages_to_get

def get_page(number):
    url = 'http://www.loc.gov/search/?q=&all=true&sp=' + str(number) + '&in=original-format%3Abook'
    return urllib.urlopen(url).read()

def main():
    start = time.time()
    pages = sample(100)
    for i, page in enumerate(pages):
        spage = time.time()
        print "getting", page
        text = get_page(page)
        open('page_' + str(page) + '.html', 'w').write(text)
        took = time.time() - spage
        print "took", took
        print 'remaining', (took * (99 - i))/1000, 'seconds'
    print 'total time', time.time() - start

main()

# vim: et sw=4 sts=4
