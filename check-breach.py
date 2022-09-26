#!/bin/python3

from urllib.request import urlopen, Request
from sys import argv as sysargv
from getpass import getpass
from hashlib import sha1

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def get_hash_suffixs(hash_prefix):
    request = Request(f"https://api.pwnedpasswords.com/range/{hash_prefix}")
    request.add_header("Add-Padding", "true")
    with urlopen(request) as breached_hashes:
        return [items.decode("utf-8").split(":")[0] for items in breached_hashes.read().split()]

def have_i_been_pwned(password_hash):
    flag = False
    prefix = password_hash['prefix']
    suffix = password_hash['suffix']
    breached_hash_suffixs = get_hash_suffixs(prefix)
    for hash_suffix in breached_hash_suffixs:
        if hash_suffix == suffix:
            flag = True
            break
    return flag

def main():
    password = " ".join(sysargv[1:])
    if password == "": password = getpass("Password: ")
    sha1_hash = sha1(password.encode()).hexdigest().upper()
    hash_components = {"prefix": sha1_hash[:5], "suffix": sha1_hash[5:]}
    if have_i_been_pwned(hash_components):
        print(bcolors.WARNING + "Critical: " + bcolors.FAIL + "Password is breached!" + bcolors.ENDC) 
    else:
        print(bcolors.OKGREEN + "Safe: " + bcolors.OKCYAN + "Password Not Found In Any Data Breach" + bcolors.ENDC)
        
if __name__ == "__main__":
    main()
