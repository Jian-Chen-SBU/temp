import pycurl, json

from collections import OrderedDict

f = open('movies.json')
content = json.load(f, object_pairs_hook=OrderedDict)
apiurl = 'http://130.245.168.53:9200/hw6/_doc'
for d in content:
	data = json.dumps(d)
	c = pycurl.Curl()
	c.setopt(pycurl.URL, apiurl)
	c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()
	c.close()
#	c.getinfo(pycurl.RESPONSE_CODE)
