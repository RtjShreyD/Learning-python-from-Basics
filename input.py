import json
with open('example_1.json','r') as input:
	obj = json.load(input)
	print('Hello,' + obj['fruit'])