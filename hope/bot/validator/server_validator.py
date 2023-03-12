
from dataclasses import dataclass


@dataclass
class ServerValidator:
    server: object
    MESSAGES: dict

    def has_server(self) -> bool:
        """Check if there is an empty server available or not
        """
        countries = self.server.objects.filter(down=False)
        if not countries:
            msg = self.MESSAGES['message_choice_country_not_found_error']
            return False, msg
        else:
            msg = self.MESSAGES['message_choice_country']
            return True, msg