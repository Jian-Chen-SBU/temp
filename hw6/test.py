import json
from collections import OrderedDict

f = open('movies.json')
data = json.load(f,object_pairs_hook=OrderedDict)

for d in data:
	print(d)
