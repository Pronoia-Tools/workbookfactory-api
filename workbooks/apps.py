from django.apps import AppConfig

class WorkbooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workbooks'

    def ready(self):
        import workbooks.signals
