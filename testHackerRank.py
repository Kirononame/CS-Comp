import urllib.request
import requests
import json

metrics_endpoint = 'https://metrics.hackerrank.com/app_metrics'
subb = 'http://api.hackerrank.com/checker/submission.json'
api_key = 'hackerrank|1106228-1338|f21f96c9c68bf501f15f01b0c9202822fbf4b211'


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
r = requests.post(subb, data={'source': source,'lang': 30,'testcases': inputx, 'api_key': api_key})

#jdata = json.load(r.text)

j = r.json()

data = j['result']['stdout']


print(data)
print(type(data))
data[0] = data[0].rstrip('\n')
print(data)
data[0] = data[0].rstrip('\n')
print(data)
print(outputx)
print(type(outputx))
outputx[0] = outputx[0].rstrip('\n')
print(data[0] == outputx[0])
