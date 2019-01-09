from flask import Flask, request, url_for, session, flash, render_template, make_response
import urllib3
import json

app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = 'deve'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@app.route('/SoftwareDeveloperChallenge', methods=['GET','POST'])
def index():
    if request.method is 'POST':
        if request.form['search'] is None:
            return redirect(url_for(index)) #if there's no search data and somebody forced a POST display clean page
        session['search'] = request.args.get('search')
        

    return
