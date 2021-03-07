from django.apps import AppConfig


class ActionConfig(AppConfig):
    name = 'human_digita.action'
    def ready(self) -> None:
        import human_digita.action.signals.handlers
