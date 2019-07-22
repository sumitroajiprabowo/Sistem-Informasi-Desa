from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models
from areacode.models import Province, Regency, District, Village
from userprofiles.models import Profile
from goverment.models import (Kelembagaan, Jabatan, Pelatihan,
                              ProfilePemerintahan,
                              )


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'province', 'regency',
                    'district', 'village', 'is_active', 'is_superuser']
    search_fields = ('email', 'username')
    ordering = ('district',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields':
                              ('username',)}
         ),
        (_('Wilayah'), {'fields':
                        ('province', 'regency',
                         'district', 'village')}
         ),
        (_('Permissions'), {'fields':
                            ('is_active', 'is_staff',
                             'is_superuser')}
         ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'groups', 'province',
                       'regency', 'district', 'village')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(Province)
admin.site.register(Regency)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Profile)
admin.site.register(Kelembagaan)


class JabatanAdmin(admin.ModelAdmin):
    model = Jabatan
    list_display = ['name', 'get_kelembagaan']

    def get_kelembagaan(self, obj):
        return obj.kelembagaan.name

    """Allows column order sorting"""
    get_kelembagaan.admin_order_field = 'kelembagaan'

    """Renames column head"""
    get_kelembagaan.short_description = 'Nama Kelembagaan'


admin.site.register(Jabatan, JabatanAdmin)


class ProfilePemerintahaninline(admin.StackedInline):
    model = ProfilePemerintahan
    can_delete = False


admin.site.register(ProfilePemerintahan)
admin.site.register(Pelatihan)
