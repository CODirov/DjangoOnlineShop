from django.contrib import admin

from .models import Category, News, Filial, Director


class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["views"]


admin.site.register(Category)
admin.site.register(News, NewsAdmin)
admin.site.register(Filial)
admin.site.register(Director)
