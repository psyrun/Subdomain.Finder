# You can find subdomain using this python script.
# Just replace the url "example.com" to your target url.
# OpenSource <3

import requests

url = "example.com"

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "example.com"

with open("./subdomainList.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        request(test_url)
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)

