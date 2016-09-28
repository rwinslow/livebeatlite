import json
import os
import re
import sys
import warnings

from flask import render_template
from flask import request
from flaskexample import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('master.html')

@app.route('/slides')
def slides():
    return render_template('slides.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('overlay_test.html')

@app.route('/go/<video_id>')
def go(video_id):
    # Get and clean video id to pull data
    try:
        video_id = str(int(video_id))
    except:
        print('Bad ID')

    # Get arguments from cache for display
    json_base = '/home/ubuntu/flaskexample/static/cache'
    with open(os.path.join(json_base, '{}.json'.format(video_id))) as f:
        kwargs_in = json.load(f)

    return render_template(
        'go.html',
        **kwargs_in
    )
