import pycurl, json


f = open('movies.json')
data = json.load(f)


apiurl = 'http://130.245.168.53:9200/hw7/_doc'

data = json.dumps(data[1])

c = pycurl.Curl()

c.setopt(pycurl.URL, apiurl)
c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
c.getinfo(pycurl.RESPONSE_CODE)
