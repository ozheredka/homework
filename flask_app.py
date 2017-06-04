from flask import Flask
from flask import url_for, render_template, request, redirect
from pymystem3 import Mystem
from collections import Counter
import pymorphy2
import re
import requests
import json

m = Mystem()
app = Flask(__name__)


def verb_analysis(text):
    words_num = 0
    verbs_num = 0
    transit_num = 0
    intransit_num = 0
    perfect_num = 0
    imperfect_num = 0
    verb_lemmas = []
    ana = m.analyze(text)
    for i in ana:
        if i['text'].strip() and 'analysis' in i and i['analysis']:
            pos = i['analysis'][0]['gr'].split('=')[0].split(',')[0]
            words_num += 1
            if pos == 'V':
                verbs_num += 1

                if 'пе' in i['analysis'][0]['gr']:
                    transit_num += 1
                elif 'нп' in i['analysis'][0]['gr']:
                    intransit_num += 1

                if 'несов' in i['analysis'][0]['gr']:
                    imperfect_num += 1
                else:
                    perfect_num += 1

                verb_lemmas += i['analysis'][0]['lex'].split()
    verbs_percent = verbs_num / words_num * 100
    lemmas_dict = Counter(verb_lemmas).most_common()
    lemmas = dict(lemmas_dict)
    result = 'Всего глаголов: {0}, что составляет {1}%'.format(verbs_num, verbs_percent) + '\n Переходных глаголов: {}'.format(transit_num) \
             + '\n Непереходных глаголов: {}'.format(intransit_num) + '\n Глаголов совершенного вида: {}'.format(perfect_num) \
             + '\n Глаголов несовершенного вида: {}'.format(imperfect_num)
    return result, lemmas

def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def VK(group1, group2):
    info1 = vk_api('groups.getMembers', group_id1=group1)
    members_group1 = info1['response']['count']
    info2 = vk_api('groups.getMembers', group_id2=group2)
    members_group2 = info2['response']['count']
    members_both = [x for x in info1['response']['users'] if x in info2['response']['users']]
    return members_group1, members_group2, members_both


def talking_app(text1):
    morph = pymorphy2.MorphAnalyzer()
    f = open('words.txt', 'r', encoding='utf-8').read()[:60000]
    corpus = re.sub('\d+', '', f)
    d = {}
    for i in corpus.split():
        t = morph.parse(i)
        word = t[0]
        d[i] = str(word.tag).split()[0]

    new_sent = []

    for i in text1.split():
        ana = morph.parse(i)
        a = ana[0]
        tag_first_part = str(a.tag).split()[0]
        tag_change = str(a.tag).split()[-1].split(',')

        for j in d:
            if d[j] == tag_first_part:
                new_word = morph.parse(j)[0]
                for k in tag_change:
                    nw = new_word.inflect({k})
                    new_word = nw
                new_sent.append(new_word.word)
                break

    new_sent = ' '.join(new_sent)
    return new_sent


@app.route('/verbform', methods=['get', 'post'])
def verbform():
    if request.form:
        text = request.form['text']
        result, lemmas = verb_analysis(text)
        result = result.replace('\n', '<br>')
        return render_template('verbforms_page.html', input=text, text=result, data=lemmas)
    return render_template('verbforms_page.html')

@app.route('/VKapi', methods=['get', 'post'])
def VKapi():
    if request.form:
        group_id1 = request.form['group_id1']
        group_id2 = request.form['group_id2']
        num1, num2, num_both = VK(group_id1, group_id2)
        return render_template('VK.html', group_id1=group_id1, group_id2=group_id2, num1=num1, num2=num2, num_both=num_both)
    return render_template('VK.html')

@app.route('/talkingapp', methods=['get', 'post'])
def talkingapp():
    if request.form:
        text1 = request.form['text']
        new_sent = talking_app(text1).replace('\n', '<br>')
        return render_template('talkingapp.html', input=text1, text=new_sent)
    return render_template('talkingapp.html')


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
