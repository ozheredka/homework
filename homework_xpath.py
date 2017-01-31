class Person:
    def __init__(self, obj):
        self.name = name
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email
        self.position = position

import re
import requests
page = requests.get('https://www.hse.ru/org/persons/?ltr=%D0%95;udept=22726')

from lxml import html
tree = html.fromstring(page.content)
name = tree.xpath('.div[@class="g-pic"/text()')
phone1 = tree.xpath('//div[@class="l-extra small"][1]/text()')
phone2 = tree.xpath('//div[@class="l-extra small"][2]/text()')
email = tree.xpath('.a[@data-at]/text()')
position = tree.xpath('//p[@class="with-indent7"]/text()')

information = []
persons = re.findall('<div class="post person">(.+)</div>', page)
for i in persons:
    teacher = Person(i)
    teacher.name
    teacher.phone
    teacher.email
    teacher.position
    information.append(teacher)

print (information)