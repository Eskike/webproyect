from django.contrib import admin
from .models import Red


# Register your models here.
class RedAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ["key"]
        else:
            return []
    

admin.site.register(Red, RedAdmin) 