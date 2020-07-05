from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from ordermaker.urls import api_router
        from users.views import router

        api_router.include_router(router, tags=["users"])