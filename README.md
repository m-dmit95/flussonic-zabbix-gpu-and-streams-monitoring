# flussonic-zabbix-gpu-and-streams-monitoring

Шаблон для мониторинга GPU и userparameter для получения списка неработающих стримов на Flussonic Media Server.

Получение списка стримов работает с помощью API Flussonic Media Server.

## Установка

1. Скопировать каталоги `channels_monitoring` и `gpu_monitoring` в `/etc/zabbix/scripts/`
2. Скопировать конфиг с юзерпараметрами `flussonic_userparameters.conf` в `/etc/zabbix/zabbix_agentd.conf.d/`
3. Прописать адрес сервера, логин и пароль от API Flussonic в `/etc/zabbix/scripts/channels_monitoring/settings.py`
4. Перезапустить zabbix-agent - `systemctl restart zabbix-agent`
5. В zabbix:
   * Для мониторинга GPU импортировать шаблон `zbx_nvidia-smi-multi-gpu.xml`.
   * Для получения списка неработающих стримов - добавить в ваш основной шаблон элемент данных с ключом `flussonic_failure_channels`

## Дополнительно

Решение для мониторинга GPU основано на https://github.com/derpaherk/Zabbix-GPU-Monitoring

`etc/zbx_nvidia-smi-multi-gpu.xml` - исходный шаблон.

Я добавил в него мониторинг *Encoder Utilization* и *Decoder Utilization*.
