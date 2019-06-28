from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Import Groups to Database"""

    def import_groups(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        group, created = Group.objects.get_or_create(name="provinsi")
        if created:
            group.name = "provinsi"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="kabupaten")
        if created:
            group.name = "kabupaten"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="kecamatan")
        if created:
            group.name = "kecamatan"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="desa")
        if created:
            group.name = "desa"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

    def handle(self, *args, **options):
        """Call the function to import Groups"""
        self.import_groups()
