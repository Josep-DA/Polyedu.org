from django.apps import AppConfig


class PolyEduConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polyedu'
    
    def ready(self):
        import polyedu.signals