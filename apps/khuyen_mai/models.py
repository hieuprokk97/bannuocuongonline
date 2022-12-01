# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KhuyenMai(models.Model):
    ma_khuyen_mai = models.IntegerField(primary_key=True)
    ten_khuyen_mai = models.CharField(max_length=30)
    mo_ta_khuyen_mai = models.CharField(max_length=100)
    ngay_bat_dau = models.DateTimeField()
    ngay_ket_thuc = models.DateTimeField()
    khuyen_mai_bang_tien = models.IntegerField()
    gia_tri_khuyen_mai = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ma_khuyen_mai

    class Meta:
        managed = True
        db_table = 'khuyen_mai'
