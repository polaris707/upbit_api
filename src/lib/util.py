#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests

UPBIT_BASE_URL = "https://api.upbit.com/v1"
REQUEST_TIMEOUT = 2

def setupLogging(filename, logger_level=logging.DEBUG, fh_level=logging.DEBUG, ch_level=logging.DEBUG):
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    fh = logging.FileHandler(filename)
    fh.setLevel(fh_level)
    fh.setFormatter( logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%m-%d %H:%M:%S') )

    ch = logging.StreamHandler()
    ch.setLevel(ch_level)
    ch.setFormatter( logging.Formatter('%(levelname)s %(message)s') )

    logger = logging.getLogger('')
    logger.setLevel(logger_level)
    logger.addHandler(fh)
    logger.addHandler(ch)

def callAPI(method, url, params):
    ret = None

    try:
        r = requests.request(method, url, params=params, timeout=REQUEST_TIMEOUT)
        ret = r if r.status_code == requests.codes.ok else None

    except Exception as e:
        logging.error(f"[callAPI] Exception - ({method}){url}", exc_info=True)

    return ret

def callUpbitAPI(method, path, params):
    return callAPI(method, f"{UPBIT_BASE_URL}{path}", params)

if __name__ == '__main__' :
    setupLogging("test.log")
    r = callUpbitAPI("GET", "/market/all", {"isDetails":"false"})
    print(r.json())
    # print(type(r.text))
    None