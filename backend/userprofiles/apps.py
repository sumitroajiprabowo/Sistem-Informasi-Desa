from django.apps import AppConfig


class UserprofilesConfig(AppConfig):
    name = 'userprofiles'


class ProfilesConfig(AppConfig):
    name = 'userprofiles'

    def ready(self):
        import userprofiles.signals