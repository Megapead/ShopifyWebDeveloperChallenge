from flask import Flask, request, url_for, session, flash, render_template, make_response
import urllib3
import json
import sys

app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = 'deve'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@app.route('/SoftwareDeveloperChallenge', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print('test',file=sys.stderr)
        if request.form['itemname'] is None:
            return redirect(url_for(index)) #if there's no search data and somebody forced a POST display clean page

        session['search'] = request.form['itemname']
        print('test2',file=sys.stderr)
        with open('data.json') as data_file:
            data = json.load(data_file)

        for item in data:
            if item["keywords"] is not None:
                keyword_string = item["keywords"]
                keyword_string = keyword_string.replace(',',' ')
                keyword_list = keyword_string.split(' ')
                print(keyword_list)
                if request.form['itemname'] in keyword_list:
                    print(item["body"])
                    return item["body"]
    return render_template('base.html')
