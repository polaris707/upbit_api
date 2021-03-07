#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import jwt
import uuid
import hashlib
import pprint

from credential import *

UPBIT_BASE_URL = "https://api.upbit.com/v1"
REQUEST_TIMEOUT = 2

def setupLogging(filename, logger_level=logging.DEBUG, fh_level=logging.DEBUG, ch_level=logging.DEBUG):
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    fh = logging.FileHandler(filename)
    fh.setLevel(fh_level)
    fh.setFormatter( logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%m-%d %H:%M:%S") )

    ch = logging.StreamHandler()
    ch.setLevel(ch_level)
    ch.setFormatter( logging.Formatter("%(levelname)s %(message)s") )

    logger = logging.getLogger("")
    logger.setLevel(logger_level)
    logger.addHandler(fh)
    logger.addHandler(ch)

def callAPI(method, url, **kwargs):
    ret = None

    try:
        r = requests.request(method, url, **kwargs)
        r.raise_for_status()
        ret = r
    except Exception as e:
        logging.error(f"[callAPI] Exception - ({method}){url}\n{kwargs}", exc_info=True)

    return ret

def callUpbitAPI(method, path, timeout=REQUEST_TIMEOUT, **kwargs):
    return callAPI(method, f"{UPBIT_BASE_URL}{path}", timeout=timeout, **kwargs)

def makeUpbitOrangeHeader(payload):
    jwt_token = jwt.encode(payload, ORANGE_UPBIT_API_SECRET_KEY)
    authorize_token = 'Bearer {}'.format(jwt_token)
    return {"Authorization": authorize_token}

if __name__ == "__main__" :
    None