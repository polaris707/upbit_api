#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../lib")
from util import *

def getCandle(market, scale="minutes", to=None, count=100, unit=1):
    if scale == "minutes":
        path = f"/candles/{scale}/{unit}"
    else:
        path = f"/candles/{scale}"

    params = {
        "market":market
        , "count":count
        , "to":to # yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss
    }

    r = callUpbitAPI("GET", path, params=params)
    return r.json() if r else None

def getTradeTick(market, to=None, count=100, cursor=None, daysAgo=None):
    path = "/trades/ticks"
    params = {
        "market":market
        , "count":count
        , "to":to # HHmmss or HH:mm:ss
        , "cursor":cursor # sequential_id in response
        , "daysAgo":daysAgo # 1~7
    }

    r = callUpbitAPI("GET", path, params=params)
    return r.json() if r else None

def getTicker(markets=[]):
    path = "/ticker"
    params = {
        "markets":','.join(markets)
    }

    r = callUpbitAPI("GET", path, params=params)
    return r.json() if r else None

def getOrderbook(markets=[]):
    path = "/orderbook"
    params = {
        "markets":','.join(markets)
    }

    r = callUpbitAPI("GET", path, params=params)
    return r.json() if r else None

if __name__ == "__main__" :
    setupLogging("quotation.log")
    # pprint.pprint(getCandle("KRW-BTC", count=10))
    # pprint.pprint(getTradeTick("KRW-BTC", count=1))
    # pprint.pprint(getTicker(["KRW-BTC"]))
    pprint.pprint(getOrderbook(["KRW-BTC"]))