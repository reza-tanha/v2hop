from concurrent.futures import ThreadPoolExecutor
import requests


class XUIAPI:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.login_url = f"http://{server}:6257/admux/login"
        self.list_inbounds = f"http://{server}:6257/admux/xui/inbound/list"
        self.delete_inbounds = f"http://{server}:6257/admux/xui/inbound/del/"
        self.session = requests.Session()
        # self.session.proxies = {"http": "socks5h://127.0.0.1:2020","https": "socks5h://127.0.0.1:2020"}

    def delete_config(self, id) -> int:
        data = {
            "username": self.username,
            "password": self.password,
        }
        self.session.post(self.login_url, data=data)
        response = self.session.post(self.delete_inbounds + str(id))
        res = response.json()
        print(res)
        return res
    
    def get_configs(self) -> list:
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
            if not config['enable']:
                conf_list.append(config['id'])
        return conf_list
            

server = input("Enter Ip Server : ")         
xui = XUIAPI(server, "", "")
with ThreadPoolExecutor(max_workers=200) as execute:
    execute.map(xui.delete_config, xui.get_configs())