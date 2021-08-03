import requests
import urllib3
import xmltodict

from utils.connect import login_get_sid
from utils.search import search_results

# Docs https://docs.splunk.com/Documentation/SplunkCloud/8.2.2105/RESTREF/RESTsearch

userName = ''
password = ''
baseUrl = 'https://<splunkurl>/servicesNS/nobody/search/search/jobs/'
searchQuery = 'jobs'

sid = login_get_sid(searchQuery, userName, password, baseUrl)

expand_search = search_results(sid, baseUrl, userName, password)