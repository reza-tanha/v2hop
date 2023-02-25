from django.apps import AppConfig


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hope.bot'
    def ready(self) -> None:
        import hope.bot.signals
