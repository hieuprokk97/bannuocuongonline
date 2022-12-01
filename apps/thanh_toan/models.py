# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.don_hang.models import DonHang

class ThanhToan(models.Model):
    thanh_toan_tien_mat = models.IntegerField()
    ma_thanh_toan = models.CharField(max_length=30)
    ma_don_hang = models.ForeignKey(DonHang, on_delete = models.PROTECT, db_column='ma_don_hang')

    class Meta:
        managed = True
        db_table = 'thanh_toan'
