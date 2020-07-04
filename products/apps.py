from django.apps import AppConfig



class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from ordermaker.urls import api_router
        from products.views import router

        api_router.include_router(router, tags=["products"])