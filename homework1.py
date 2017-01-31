import re
class Person:
    def __init__(self, obj): 
        self.name = self.findname
        self.phone = self.findphone
        self.email = self.findemail
        self.position = self.findposition

    def findname(self):
        name = re.search('<div class="g-pic person-avatar-small2" title="(.+)" alt=', text, flags = re.DOTALL)
        return name

    def findphone(self):
        phone1 = re.search('<div class="l-extra small">(.+)</div>', text)
        for i in phone1:
            phone = re.findall('<span>(.+)</span>', phone1.group(0), flags = re.DOTALL)
            return phone

    def findemail(self):
        mail = re.search('<a class="link" data-at=(.+)></a>', text, flags=re.DOTALL)
        email = mail.group(0).replace('-at-', '@')
        email = email.replace('","', '')
        email = email.replace('["', '')
        email = email.replace('"]', '')
        return email

    def findposition(self):
        position = {}
        place = re.search('<p class="with-indent7">(\w+)</p>', text, flags=re.DOTALL)
        info = re.findall('<span>(.+)</span>', place)
        for i in info:
            degree = re.search('\w+', i)
            place1 = re.findall('<a class="link" href=".+">(.+)</a>', i)
            position = degree.group(0) + place1
            return position

text = open('classperson.txt', 'r', encoding = 'utf-8')
page = text.read()
text.close()
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
