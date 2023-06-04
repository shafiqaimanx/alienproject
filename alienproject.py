#!/usr/bin/env python3
# SHAFIQAIMAN
import requests
import random
import json
import sys

class color:
    RESET   = '\033[0m'
    RED     = '\033[38;5;196m'
    GREEN   = '\033[38;5;118m'
    YELLOW  = '\033[38;5;226m'

GOOD    = f"{color.GREEN}[+]{color.RESET}"
ERROR   = f"{color.RED}[!]{color.RESET}"
RESULT  = f"{color.GREEN}[-]{color.RESET}"

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
    print("`...|...>;:.'    Made with love: SHAFIQAIMAN\n")

if __name__ == "__main__":
    try:
        username = sys.argv[1].strip()
        if len(sys.argv) <= 2:
            username = sys.argv[1].strip()
        else:
            print("{} Usage: {} <username>".format(GOOD, sys.argv[0]))
            sys.exit(1)
    except IndexError:
        print("{} Usage: {} <username>".format(GOOD, sys.argv[0]))
        sys.exit(1)

    try:
        with open(WEBSITEZ_PATH, 'r') as f:
            banner()
            print(f"{GOOD} Checking username {color.YELLOW}{username}{color.RESET} on:")
            try:
                count = 0
                for line in json.loads(f.read())['websitez_list']:
                    error   = bytes.fromhex(line['error']).decode(line['unicode'])
                    url     = line['search'].format(username)
                    headers = {'User-Agent':RAND_AGENTZ}
                    resp    = requests.get(url, headers=headers)

                    if resp.status_code == 200:
                        if error not in resp.text:
                            print(f"{RESULT} {color.YELLOW}{line['name']}{color.RESET}: {line['mainurl'].format(username)}")
                        else:
                            continue
                        count += 1
                if count > 0:
                    print("{} Done checking username...".format(GOOD))
                else:
                    print(f"{ERROR} Sorry, can't find {color.YELLOW}{username}{color.RESET} anywhere...")
            except KeyboardInterrupt:
                print("\n{} User quitting...".format(ERROR))
                sys.exit(1)
    except FileNotFoundError:
        print("{} File not found!... [{}]".format(ERROR, WEBSITEZ_PATH))
        sys.exit(1)