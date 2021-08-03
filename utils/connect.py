import requests
import urllib3
import xmltodict

userName = ''
password = ''
baseUrl = ''

def login_get_sid(searchQuery, userName, password, baseUrl):
    response = requests.request("POST", baseUrl, auth=(userName, password), data=searchQuery, verify=True) # Change Verify=False if you do not have certs imported.
    response_text = response.text
    raw_sid = xmltodict.parse(response_text)
    sid = raw_sid['response'].get('sid')
    return sid