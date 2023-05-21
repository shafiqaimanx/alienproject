#!/usr/bin/env python3
# @_shafiqaiman_
import requests
import random
import json
import sys

class color:
    RESET = '\033[0m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'

agentz_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
]

# CHANGE THIS IF [file not found!]
WEBSITEZ_PATH = "websitez.json"
RAND_AGENTZ   = random.choice(agentz_list)

def banner():
    print(" _______ _______     ")
    print("|   _   |   _   |    AlienProject - CLI tool for findings username.")
    print("|.  1   |.  1   |    Inspire by (https://github.com/sherlock-project/sherlock).")
    print("|.  _   |.  ____|    v.N/A")
    print("|:  |   |:  |        ")
    print("|::.|:. |::.|        ")
    print("`...|...>;:.'    Made with love: @_shafiqaiman_\n")

if __name__ == "__main__":
    try:
        username = sys.argv[1].strip()
    except IndexError:
        print("Usage: {} <username>".format(sys.argv[0]))
        sys.exit(1)

    with open(WEBSITEZ_PATH, 'r') as f:
        banner()
        print(f"{color.GREEN}[+]{color.RESET} Checking username {color.YELLOW}{username}{color.RESET} on:")
        for line in json.loads(f.read())['websitez_list']:
            url = line['search'].format(username)
            headers = {'User-Agent':RAND_AGENTZ}
            resp = requests.get(url, headers=headers)

            if line['error'] not in resp.text:
                print(f"{color.GREEN}[!]{color.RESET} {color.YELLOW}{line['name']}{color.RESET}: {line['mainurl'].format(username)}")
            else:
                continue