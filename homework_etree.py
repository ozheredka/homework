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

from lxml import etree
root = etree.HTML(page.content)

#/html/body/div[1]/div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/a/div
names = root[1][0][3][1][1][2][1][0][1]
for n in names:
    if 'n' in n.attrib['title']:
        header = n[0]
        name = header[0][0].text
        print(name)

phone01 = root[1][0][3][1][1][2][1][0][0][0]
for number in phone1:
    header = number[0]
    phone1 = header[0].text

phone02 = root[1][0][3][1][1][2][1][0][0][1]
for number in phone2:
    header = number[0]
    phone2 = header[0].text
#/html/body/div[1]/div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/a
mail = root[1][0][3][1][1][2][1][0][0]
for m in mail:
    if 'm' in m.attrib['data-at']:
        header = m[0]
        email1 = header[2].text
        email2 = email1.replace('-at-', '@')
        email2 = email2.replace('","', '')
        email2 = email2.replace('["', '')
        email = email2.replace('"]', '')

#/html/body/div[1]/div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/p/span[1]/a
prof = root[1][0][3][1][1][2][1][0][1]
for p in prof:
    header = p[0]
    position = header[1].text

information = []
persons = re.findall('<div class="post person">(.+)</div>', page, flags = re.DOTALL)
for i in persons:
    teacher = Person(i)
    teacher.name
    teacher.phone
    teacher.email
    teacher.position
    information.append(teacher)

print (information)