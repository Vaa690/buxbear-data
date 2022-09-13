from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'is_staff',
    )

admin.site.register(User, UserAdmin)