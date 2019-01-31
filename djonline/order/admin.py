from django.contrib import admin

from order.models import o_jieji,o_order,o_songji,o_tourist
# Register your models here.
admin.site.register(o_jieji)
admin.site.register(o_order)
admin.site.register(o_songji)
admin.site.register(o_tourist)