from flask import Flask, request, url_for, session, flash, render_template, make_response, Markup
import urllib3
import json
import sys
import cgi
import html

app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = 'deve'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def unicodeToHTMLEntities(text):

    return cgi.escape(text).encode('ascii', 'htmlcharrefreplace')


@app.route('/SoftwareDeveloperChallenge', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['itemname'] is None:
            return redirect(url_for(index)) #if there's no search data and somebody forced a POST display clean page

        session['search'] = request.form['itemname']
        with open('data.json') as data_file:
            data = json.load(data_file)
        json_list = []
        for item in data:
            if item["keywords"] is not None:
                keyword_string = item["keywords"]
                keyword_string = keyword_string.replace(',',' ')
                keyword_string = keyword_string.replace('(',' ')
                keyword_string = keyword_string.replace(')',' ')
                keyword_string = keyword_string.replace('-',' ')
                keyword_list = keyword_string.split(' ')
                if request.form['itemname'] in keyword_list:
                    item["favourited"] = 'False'
                    item['body'] = html.unescape(item['body'])
                    json_list.append(item)
                    markup = Markup(item['body'])

        if json_list is not {}:
            return render_template('base.html', table_search = json_list, mrkup = markup)
            #return json.dumps(json_list)
        else:
            return "Invalid search"
    return render_template('base.html',table_search = [],mrkup = "blank")
