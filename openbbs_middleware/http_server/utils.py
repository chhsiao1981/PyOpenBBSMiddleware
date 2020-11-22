# -*- coding: utf-8 -*-

from flask import request

import pyutil_mongo

from openbbs_middleware import cfg
from openbbs_middleware.utils.util_http import http_post
from openbbs_middleware.utils.util_time import get_current_milli_ts


def get_ip():

    return request.remote_addr


def validate_user(user_id, password, ip):
    url = cfg.config.get('ptt_server', '') + '/login'
    err, result = http_post(url, {'UserID': user_id, 'Passwd': password, "IP": ip})
    if err is not None:
        return err, ''

    cfg.logger.info('result: %s', result)

    jwt = result.get('Jwt', '')

    pyutil_mongo.db_update('user', {'user_id': user_id}, {'jwt': jwt, 'active': True, 'last_login': get_current_milli_ts()})

    return None, jwt
