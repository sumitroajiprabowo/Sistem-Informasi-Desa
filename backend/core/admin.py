from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models
from areacode.models import Province, Regency, District, Village
from userprofiles.models import Profile
from goverment.models import (Kelembagaan, Jabatan, Pelatihan,
                              Pemerintahan, KelembagaanJabatan,
                              PelatihanAparatur)


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(Province)
admin.site.register(Regency)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Profile)
admin.site.register(Kelembagaan)
admin.site.register(Jabatan)
admin.site.register(Pelatihan)
admin.site.register(Pemerintahan)
admin.site.register(KelembagaanJabatan)
admin.site.register(PelatihanAparatur)
