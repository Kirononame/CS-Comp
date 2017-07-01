import urllib.request
import requests
import json
import urllib
from urllib.parse import unquote
from flask import Flask, jsonify, request, render_template
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


app = Flask(__name__)

metrics_endpoint = 'https://metrics.hackerrank.com/app_metrics'
sub = 'http://api.hackerrank.com/checker/submission.json'
api_key = 'hackerrank|1106228-1338|f21f96c9c68bf501f15f01b0c9202822fbf4b211'

end_time = datetime(2017, 4, 24, 15, 30, 0, 0)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/')
@app.route('/<string:name>')
def man(name = None):
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    #app.logger.info('Info')

    if(datetime.now() > end_time):
        return 'Time Over'
    
    return render_template('website.html', name = name)
    
    """
    if request.method == 'POST':
        content = urllib.request.urlopen("http://api.hackerrank.com/checker/languages.json").read()
        return ('post happened\n')
    else:
        return 'hello\n\t\r'  # Showing "It works Message" + jsonify({'message' : 'It works'})
    """

@app.route('/post/<string:name>', methods=['GET'])
def returnOne(name):

    return jsonify({'language' : 'a'})


@app.route('/post', methods=['POST'])
def post():

    h = request.get_json()
    s = h['source']
    l = h['lang']
    g = h['group']
    q = h['question']
    hour = h['hour']
    m = h['minutes']
    seconds = h['seconds']
    mSeconds = h['milliseconds']
    beg = '//'

    if(datetime.now() > end_time):
        app.logger.info('Team: ' + g + ' solved: ' + q + ' After Time')
        return 'Time Over'

    if(l ==  'py'):
        beg = '#'

    s = unquote(unquote(s))
    s =  beg + ' ' + str(hour) + ':' + str(m) + ':' + str(seconds) + ':' + str(mSeconds) + '\n' + s

    g = unquote(unquote(g))
    if (len(g) > 10):
        g = g[:10]
    
    fName = 'comp/' + g + '_' + q + '_' + str(m) + '.' + l
        
    with open(fName, "w") as f:
        f.write(s)

    app.logger.info('Team: ' + g + ' solved: ' + q)
    
    return ('Done')

"""   
    inputx = '["7 11\\n5 15\\n3 2\\n-2 2 1\\n5 -6\\n"]'

    outputx = ['1\n1\n']

    source = 's,t = input().strip().split(' ')\n\
s,t = [int(s),int(t)]\n\
a,b = input().strip().split(' ')\n\
a,b = [int(a),int(b)]\n\
m,n = input().strip().split(' ')\n\
m,n = [int(m),int(n)]\n\
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]\n\
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]\n\
\n\
house = range(s, (t + 1))\n\
print(len([apple for apple in apples if ((a + apple) in house)]))  # num_of_apples\n\
print(len([orange for orange in oranges if ((b + orange) in house)]))  # num_of_oranges\n'
    
    # data={'source': 'print 1','lang': 5, 'testcases': '["1"]', 'api_key': api_key})
    # content = urllib.request.urlopen("http://api.hackerrank.com/checker/languages.json").read()
    r = requests.post(sub, data={'source': s, 'lang': l,'testcases': inputx, 'api_key': api_key})

    j = r.json()

    data = j['result']['stdout']
    data[0] = data[0].rstrip('\n')

    outputx[0] = outputx[0].rstrip('\n')
    # str(data[0] == data[0])
    
"""

@app.route('/ip')
@app.route('/hip/<name>')
def ip(name = None):
    
    if(datetime.now() > end_time):
        return 'Time Finished'
    
    return render_template('ip.html', name = name)
    

@app.route('/q1')
@app.route('/q1t/<name>')
def getQ1(name = None):

    if(datetime.now() > end_time):
        return 'Time Over'
    
    return render_template('question1.html', name = name)

@app.route('/q2')
@app.route('/q2t/<name>')
def getQ2(name = None):

    if(datetime.now() > end_time):
        return 'Time Over'
    
    return render_template('question2.html', name = name)

@app.route('/q3')
@app.route('/q3t/<name>')
def getQ3(name = None):

    if(datetime.now() > end_time):
        return 'Time Over'
    
    return render_template('question3.html', name = name)

@app.route('/q4')
@app.route('/q4t/<name>')
def getQ4(name = None):

    if(datetime.now() > end_time):
        return 'Time Over'
    
    return render_template('question4.html', name = name)


if(__name__ == '__main__'):
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s","%Y-%m-%d %H:%M:%S")
    app.logger.addHandler(handler)
    app.run(debug=True, port=8080, host='0.0.0.0')
