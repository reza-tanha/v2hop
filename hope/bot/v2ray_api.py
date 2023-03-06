import requests
import json
import time
import base64
import random
from hope.bot.telegram.configs import *


class XUIAPI:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.login_url = f"http://{server}:{SERVERS_PORT}/uxadm/login"
        self.add_inbounds = f"http://{server}:{SERVERS_PORT}/uxadm/xui/inbound/add"
        self.list_inbounds = f"http://{server}:{SERVERS_PORT}/uxadm/xui/inbound/list"
        self.delete_inbounds = f"http://{server}:{SERVERS_PORT}/uxadm/xui/inbound/del/"
        self.session = requests.Session()
        if PERFECTMONEY_PROXY:
            self.session.proxies = PERFECTMONEY_PROXY

    def data_proxy(self, expire_date, total, uuid_, ch=False):
        if not ch:
            time_now = int(time.time())
            expire_date = int(str(time_now+expire_date * 60 * 60)+"000")

        port = random.randint(10000, 65000)
        total = total * 1024 * 1024
        data = {
            "up": 0,
            "down": 0,
            "remark": BOT_USERNAME,
            "enable": True,
            "expiryTime": expire_date,
            "autoreset": False,
            "ipalert": False,
            "iplimit": 0,
            "total": total,
            "port": port,
            "protocol": "vmess",
            "settings": json.dumps({
                "clients": [
                    {
                        "id": uuid_,
                        "email": "S7XMasc.lo1e@xray.com",
                        "alterId": 0,
                        "total": total
                    }
                ],
                "disableInsecureEncryption": False
            }),

            "streamSettings": json.dumps({
                "network": "tcp",
                "security": "none",
                "tcpSettings": {
                    "header": {
                        "type": "http",
                        "request": {
                            "method": "GET",
                            "path": [
                                "/"
                            ],
                            "headers": {
                                "Host": [
                                    "soft98.ir"
                                ]
                            }
                        },
                        "response": {
                            "version": "1.1",
                            "status": "200",
                            "reason": "OK",
                            "headers": {}
                        }
                    },
                    "acceptProxyProtocol": False
                }
            }),

            "sniffing": json.dumps({
                "enabled": True,
                "destOverride": [
                    "http",
                    "tls"
                ]
            })
        }
        proxy_hash = {
            "v": "2",
            "ps": BOT_USERNAME,
            "add": self.server,
            "port": port,
            "id": uuid_,
            "aid": 0,
            "net": "tcp",
            "type": "http",
            "host": "soft98.ir",
            "path": "/",
            "tls": "none"
        }
        peoxy_hash = base64.b64encode(str(proxy_hash).encode('utf-8')).decode()
        return data, "vmess://"+peoxy_hash, uuid_

    def getSession(self, expire_date, total, uuid, ch=False):
        DATA = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(
            self.login_url,
            data=DATA
        )
        config_data = self.data_proxy(expire_date, total, uuid, ch)
        self.session.post(
            self.add_inbounds,
            data=config_data[0]
        )
        self.session.close()
        return config_data[1], config_data[2], config_data[0]["total"]

    def get_one_inbounds_config(self, uuid: str):
        """Filter inbounds config with uuid"""
        data = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(url=self.login_url, data=data)
        response = self.session.post(url=self.list_inbounds)
        objects = response.json()["obj"]
        for config in objects:
            settings = json.loads(config['settings'])
            client_id = settings["clients"][0]['id']
            if client_id == uuid:
                return {
                    "id": config["id"],
                    "port": config["port"],
                    "protocol": config["protocol"],
                    "remark": config["remark"],
                    "uuid": client_id
                }

    def get_config_uuid(self, uuid):
        DATA = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(
            self.login_url,
            data=DATA
        )
        r = self.session.post(
            self.list_inbounds
        )
        configs = r.json()["obj"]
        for conf in configs:
            settings = json.loads(conf['settings'])
            conf_uuid = settings["clients"][0]['id']
            if uuid == conf_uuid:
                return conf

    def delete_config(self, id):
        data = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(self.login_url, data=data)
        response = self.session.post(self.delete_inbounds + str(id))
        return response.json()
    
    def get_count_config(self):
        DATA = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(
            self.login_url,
            data=DATA
        )
        r = self.session.post(
            self.list_inbounds
        )
        objects = r.json()["obj"]
        conf_list = []
        for config in objects:
            is_enable = json.dumps(config['enable'])
            if is_enable and config['total'] > 157286400:
                conf_list.append(config)

        return conf_list
            