import requests


url = "https://github.com/Panelinio/Ryzdo/deferred-ast/master/log.txt"

payload ={
    "content" : "Test IVY - ale z apki"
}

headers = {
    "Authorization" : "token"
}

res = requests.post(url, payload, headers=headers)