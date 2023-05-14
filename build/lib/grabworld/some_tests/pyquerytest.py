# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

with open('test.html','r',encoding='utf-8') as f:
    doc = pq(f.read())
trs = doc('tr').items()
page = doc('.page_info')
print(page.text().split('/')[-1])
# for i in trs:
#     a = i.text().split('\n')
#     print(a)