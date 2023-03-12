from .functions import *

from dataclasses import dataclass
from django.shortcuts import get_object_or_404
from hope.bot.v2ray_api import XUIAPI


@dataclass()
class ChangeLocation:
    telegram: object
    user: object
    new_server: object
    chat_id: int
    message_id: int
    new_uuid: int
    config_id: int
    callback_id: int


    def calculate_new_volume(self, xray, proxy_config_uuid) -> tuple:
        """Calculate the remaining amount of user traffic"""
        user_config = xray.get_config_uuid(proxy_config_uuid)
        if not user_config:
            return
        new_volume = user_config['total'] - (user_config['down'] + user_config['up'])
        return user_config, int(user_config['total'] / 1024 ), int(new_volume / 1024)


    def validate_config(self, proxy_config: object) -> bool:
        """Check user config was expired or not
            and check available user config volume
        """
        if proxy_config.expire_date <= datetime.now().date():
            return self.telegram.send_AnswerCallbackQuery(
                self.callback_id,
                text=MESSAGES["message_config_expire_error"]
            )

        if self.new_volume <= 500:  # if volume < 500 mb
            return self.telegram.send_AnswerCallbackQuery(
                self.callback_id,
                text=MESSAGES["message_reloc_not_enogh_volume_error"]
            )
        return True


    def update_user_balance(self, last_server: object, plan: object):
        """Update user balance"""
        if not last_server.is_tunnel and self.new_server.is_tunnel:
            kilobytes_volume_price = plan.price / self.total_volume
            new_balance = kilobytes_volume_price * self.new_volume
            if self.user.user_balance.balance < new_balance:
                self.telegram.send_AnswerCallbackQuery(
                    self.callback_id,
                    text=MESSAGES["message_not_balance"]
                )
                return False

            self.user.user_balance.balance -= new_balance
            self.user.user_balance.save()
            return True

        if last_server.is_tunnel and not self.new_server.is_tunnel:
            kilobytes_volume_price = plan.price / self.total_volume
            new_balance = kilobytes_volume_price * self.new_volume
            self.user.user_balance.balance += new_balance
            self.user.user_balance.save()
            return True

        return True


    def remove_last_config(self, xray: object):
        """Remove config from the server"""
        try:
            xray.delete_config(self.user_config["id"])
            new_xray = XUIAPI(
                user=self.user.username,
                server=self.new_server.ip,
                username=self.new_server.username,
                password=self.new_server.password
            )
            data = new_xray.getSession(self.user_config['expiryTime'], int(self.new_volume/1024), self.new_uuid, True)
            return data
        except:
            return


    def create_new_configuration(self, proxy_config: object, select_config: list):
        """Create new config"""
        num_change_location = proxy_config.last_num_change + 1
        new_proxy_config = ProxyConfig(
            proxy_hash=select_config[0],
            server=self.new_server,
            volume=proxy_config.volume,
            is_use=True,
            user=self.user,
            uuid=self.new_uuid,
            last_num_change=num_change_location,
            expire_date=proxy_config.expire_date
        )
        new_proxy_config.save()
        proxy_config.delete()
        return self.telegram.editMessageText(
            self.chat_id,
            self.message_id,
            show_config_info(select_config, new_volume=self.new_volume*1024),
            reply_markup=show_start_home_buttons(self.chat_id),
        )


    def main(self):
        proxy_config = get_object_or_404(ProxyConfig, id=self.config_id)
        plan = get_object_or_404(Plan, volume=proxy_config.volume)
        last_server = proxy_config.server

        xray = XUIAPI(
            server=last_server.ip,
            username=last_server.username,
            password=last_server.password
        )
        data = self.calculate_new_volume(xray, proxy_config.uuid)
        if not data:
            return

        self.user_config, self.total_volume, self.new_volume = data
        balance = self.update_user_balance(last_server, plan)
        if not balance:
            return

        if not self.validate_config(proxy_config):
            return

        select_config = self.remove_last_config(xray)
        if not select_config:
            return

        self.create_new_configuration(proxy_config, select_config)