# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default
from os import truncate
from django.db import models
from apps.khach_hang.models import KhachHang
from apps.shipper.models import Shipper
class DonHang(models.Model):
    ma_don_hang = models.CharField(primary_key=True, max_length=10)
    ten_don_hang = models.TextField(max_length=50, blank=True)
    ngay_dat = models.DateTimeField(auto_now_add = True, blank=True)
    ngay_giao = models.DateTimeField(auto_now = truncate, blank=True)
    trang_thai = models.IntegerField(default=0)
    tong_tien_hang = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    ma_khach_hang = models.ForeignKey(KhachHang, on_delete=models.PROTECT, db_column='ma_khach_hang')
    ma_shipper = models.ForeignKey(Shipper, on_delete=models.PROTECT, db_column='ma_shipper', null=True)

    def __str__(self):
        return f"{self.ma_don_hang}, {self.ngay_dat}, {self.ngay_giao},{self.tong_tien_hang}, {self.ma_khach_hang}, {self.ma_shipper}"

    class Meta:
        managed = True
        db_table = 'don_hang'