########################################
# HTTP requests fundamentals in python
# -------------------------------------
#
# Learn the various ways to make HTTP/1.1 requests
# in python through code examples.
#
# requests: https://pypi.org/project/requests
# urllib3: https://urllib3.readthedocs.io/en/latest
# urllib2: https://docs.python.org/2/library/urllib2.html
# httplib2: https://github.com/httplib2/httplib2
#
# By Doug Purcell
# http://www.purcellconsult.com
#
##########################################

import requests
import urllib
from urllib.request import urlopen
import urllib3
import httplib2


# Requests Overview
# -----------------
# Fully supports a restful API
# get, post, put, delete, methods
# international domains and urls
# keep-alive & connection pooling (uses urllib3 for this)
# browser-style SSL verification

# making a simple HTTP/1.1 request

wiki = requests.get('https://en.wikipedia.org/wiki/Main_Page')

print(wiki.status_code)  # checks the status codes: 200

print(requests.codes['temporary_redirect'])  # 307

# after a server returns the response you want, can collect content

t = wiki.text       # response in bytes
c = wiki.content    # response in Unicode

print(dir(wiki))    # see all of the cool functionality you can do!
print(wiki.headers['Content-Type'])

# The urllib module
# ------------------
# URL Handing Modules: https://docs.python.org/3/library/urllib.html
# contains several modules for working with URLS such as
# urllib.request, urllib.error, urllib.parse, and urllib.robotparser

# returns the URL of the resource received
url = urllib.request.urlopen('https://www.gocomics.com/comics/popular')

# returns URL of the resource retrieved
link = url.geturl()

# returns meta info of the page like headers
code = url.info()

# returns the HTTP status of the response
status = url.getcode()

print(url)
print(link)
print(code)
print(status)

# The urllib2 module
# ------------------
# A module that's been split across various modules
# in python3 named urllib.request and urllib.error.
# since the urllib2 module has been split across several modules,
# must do the following: from urllib.request import urlopen

site = urlopen('https://www.latimes.com')
content = ''
for text in site:
    content += str(text)

# The urllib3 module
# ------------------
# A powerful HTTP client for python. Some of its features:
# Thread safety
# Connection pooling
# Client-side SSL/TLS verification
# File uploads with multipart encoding

http = urllib3.PoolManager()    # needed to make requests
r = http.request('GET', 'http://www.yahoo.com')
print(r.data.decode('utf-8'))

h = httplib2.Http('.cache')
(resp_headers, content) = h.request('http://www.example.org', 'GET')

h = httplib2.Http(".cache")
h.add_credentials('name', 'password')
(resp, content) = h.request("https://example.org/chapter/2",
                            "PUT", body="This is text",
                            headers={'content-type':'text/plain'} )

# Why so many options for making HTTP requests?
# There are many talented developers who feel they can
# create a better solution then the other ones.