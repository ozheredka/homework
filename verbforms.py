from flask import Flask
from flask import url_for, render_template, request, redirect
from pymystem3 import Mystem
from collections import Counter

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


@app.route('/verbform', methods=['get', 'post'])
def verbform():
    if request.form:
        text = request.form['text']
        result, lemmas = verb_analysis(text)
        result = result.replace('\n', '<br>')
        return render_template('verbforms_page.html', input=text, text=result, data=lemmas)
    return render_template('verbforms_page.html')


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
