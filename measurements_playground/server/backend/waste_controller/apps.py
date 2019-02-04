from django.apps import AppConfig


class WasteControllerConfig(AppConfig):
    name = 'waste_controller'

    def ready(self):
        from . import mqtt
        mqtt.client.loop_start()
