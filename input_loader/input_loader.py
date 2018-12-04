import requests
import os.path
import sys

def get_input(day):
    path = f'day{day}.txt'
    if os.path.isfile(path):
        return open(path).read()
    
    cookie = {'session': '53616c7465645f5f34fad9ceebd1bbf84a3bd7bd9bb29a74a986803905d56ccb76c23a8c16ffda2b5032b258e3d710cb'}
    url = f'https://adventofcode.com/2018/day/{day}/input'
    req = requests.get(url, allow_redirects=True, cookies=cookie)
    
    if req.status_code != 200:
        print(f'ERROR: Http request failed: {req.status_code} {req.reason}.', file=sys.stderr)
        return ''
    
    open(path, mode='w').write(req.text)
    return req.text
