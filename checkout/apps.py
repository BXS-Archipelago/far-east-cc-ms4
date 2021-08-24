from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

# custom update total model method will be called, updating the order total 
# automatically
    def ready(self):
        import checkout.signals