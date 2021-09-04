#!/usr/bin/env python3

import requests
import json


class FlussonicApi():
    '''
    Данный класс хранит в себе методы для взаимодействия с Flussonic API
    '''
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth

    def api_get_query(self, query):
        ''' Делает запрос в апи и возвращает результат в UTF-8 '''
        url = f'{self.url}flussonic/api/{query}'
        server_info = requests.get(url, auth=self.auth)
        server_info = server_info.content.decode('utf-8')
        server_info = json.loads(server_info)
        return server_info

    def get_working_channels(self):
        ''' Парсим нужную информацию о работающих каналах на сервере '''
        media = self.api_get_query('media')
        result = []
        for entry in media:
            if entry['entry'] == 'stream':
                stream_name = entry['value']['name']
                try:
                    stream_title = entry['value']['options']['title']
                except KeyError:
                    stream_title = f'restream_{stream_name}'
                data = {'name': stream_name, 'title': stream_title}
                result.append(data)
        return result

    def get_all_channels_state(self):
        ''' Парсим статус каналов на сервере '''
        media = self.api_get_query('media')
        result = []
        for entry in media:
            if entry['entry'] == 'stream':
                stream_name = entry['value']['name']
                try:
                    stream_title = entry['value']['options']['title']
                except KeyError:
                    stream_title = f'restream_{stream_name}'
                stream_alive = entry['value']['stats']['alive']
                data = {
                    'name': stream_name,
                    'title': stream_title,
                    'alive': stream_alive,
                }
                result.append(data)
        return result

    def get_failure_channels(self):
        channels = self.get_all_channels_state()
        failure_channels = []
        for channel in channels:
            if channel['alive'] is False:
                failure_channels.append(channel)
        return failure_channels

    def format_failure_channels_for_zabbix(self):
        failure_channels = self.get_failure_channels()
        failure_count = len(failure_channels)
        if failure_count == 0:
            return 'OK - all channels working'
        fail_str = f'These [{failure_count}] channels are not working: \n'
        for channel in failure_channels:
            fail_str += (
                f"{channel['title']} ({channel['name']})\n"
            )
        return fail_str
