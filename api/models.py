from django.conf import settings


class UserModel:
    @classmethod
    def all(cls):
        return settings.USERS

class ResourceModel:
    @classmethod
    def all(cls):
        return settings.RESOURCES
