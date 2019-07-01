from django.db import models


class Province(models.Model):
    """Model Database Provinsi"""
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Provinsi"
        db_table = "area_provinces"

    def __str__(self):
        return self.name


class Regency(models.Model):
    """Model Database Kabupaten"""
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Kabupaten"
        db_table = "area_regencies"

    def __str__(self):
        return self.name


class District(models.Model):
    """Model Database Kecamatan"""
    name = models.CharField(max_length=255)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Kecamatan"
        db_table = "area_districts"

    def __str__(self):
        return self.name


class Village(models.Model):
    """Model Database Desa"""
    id = models.BigIntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Desa"
        db_table = "area_villages"

    def __str__(self):
        return self.name
