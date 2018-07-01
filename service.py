import json
with open('example_1.json','r') as input:
	obj = json.load(input)
	with open('output.txt', 'w') as output:
		output.write(obj['name'] + "'s Taste:\n")
		for tasty in obj['Taste']:
			output.write(tasty + "\n")
			