import requests
import urllib3
import xmltodict


def search_results(sid, baseUrl, userName, password)
    queryUrl = baseUrl + '/' + sid + '/results'
    response = requests.request('GET', queryUrl, auth=(userName, password), verify=True) # Set verify=False if you do not have SSL cert installed.
    search_results = response.text
    return response.text