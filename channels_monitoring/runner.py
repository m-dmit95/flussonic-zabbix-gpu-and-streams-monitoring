#!/usr/bin/env python3
from requests.auth import HTTPBasicAuth

import settings

from flussonic_api import FlussonicApi

''' Подгатавливаем авторизацию '''
auth = HTTPBasicAuth(
    settings.AUTH_INFO['login'],
    settings.AUTH_INFO['pass'],
)
''' Создаем объект FlussonicApi и авторизуемся '''
api = FlussonicApi(settings.AUTH_INFO['url'], auth)
''' Получаем список нерабочих каналов, либо OK если все работает '''
print(api.format_failure_channels_for_zabbix())
