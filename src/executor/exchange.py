#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../lib")
from util import *

def getAccounts():
    payload = {
        'access_key': ORANGE_UPBIT_API_ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
    }
    headers = makeUpbitOrangeHeader(payload)
    path = "/accounts"
    r = callUpbitAPI("GET", path, headers=headers)
    return r.json() if r else None

def getOrdersChance():
    return

if __name__ == "__main__" :
    setupLogging("exchange.log")
    pprint.pprint(getAccounts())