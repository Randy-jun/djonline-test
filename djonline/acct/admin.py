from django.contrib import admin

from acct.models import Agency_t,Application_t,Line_Price_t,Ref_Price_t,Tourist_t,Settlement_t
class AgencyAdmin(admin.ModelAdmin):
    list_display =('id','name')
admin.site.register(Agency_t,AgencyAdmin)
admin.site.register(Application_t)
admin.site.register(Line_Price_t)
admin.site.register(Ref_Price_t)
admin.site.register(Tourist_t)
admin.site.register(Settlement_t)

