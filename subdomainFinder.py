# You can find subdomain using this python script.
# Just replace the target_url "example.com" to your target url.
# OpenSource <3

import requests
import argparse

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Subdomain enumeration tool.")
    parser.add_argument("domain", help="Target domain to scan for subdomains")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    args = parser.parse_args()

    target_url = args.domain

    try:
        with open(args.wordlist, "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = word + "." + target_url
                response = request(test_url)
                if response:
                    print("[+] Discovered subdomain --> " + test_url)
    except FileNotFoundError:
        print(f"[!] Wordlist file '{args.wordlist}' not found.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
