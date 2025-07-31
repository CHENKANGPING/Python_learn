from django.apps import AppConfig


class AbsentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.absent'  # 修改为完整的应用路径
