from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 属性表示这个配置类是加载到哪个应用的，每个配置类必须包含此属性，默认自动生成
    name = 'book'
    # AppConfig.verbose_name属性用于设置该应用的直观可读的名字，此名字在Django提供的Admin管理站点中会显示
    verbose_name = '书籍管理'