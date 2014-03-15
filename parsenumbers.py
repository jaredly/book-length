#!/usr/bin/env python

import os
import re

def get_htmls():
    return [x for x in os.listdir('.') if x.startswith('page_')]

def get_books(fname):
    text = open(fname).read()
    starts = "<div class='result_item'>"
    ends = "</div>"
    pos = 0
    results = []
    while starts in text:
        pos += text.index(starts)
        text = text[text.index(starts):]
        #if ends not in text:
        #    print "failed to find the end", pos
        end = text.index(ends)
        results.append(text[:end])
        text = text[end:]
    return results

def get_pagenumber(text):
    if '<h3>' not in text or '</h3>' not in text:
        return False
    h3 = text[text.index('<h3>'):text.index('</h3>')]
    pn = re.findall(r'\b(\d+)\]? p(ages|\.)', h3)
    if not pn:
        #print 'no page number', h3
        return False
    return int(pn[0][0].split()[0])

def main():
    numbers = []
    for fname in get_htmls():
        #print "getting", fname
        results = get_books(fname)
        for result in results:
            num = get_pagenumber(result)
            if num is not False:
                numbers.append(num)
    open('data.R', 'w').write('z = c(' + ', '.join(map(str, numbers)) + ')')
    print 'out of', len(numbers)
    print sum(numbers)/float(len(numbers))

main()

# vim: et sw=4 sts=4
