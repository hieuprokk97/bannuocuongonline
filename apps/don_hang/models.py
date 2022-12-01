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
from apps.khuyen_mai.models import KhuyenMai
from apps.shipper.models import Shipper
from apps.san_pham.models import SanPham
class DonHang(models.Model):
    ma_don_hang = models.CharField(primary_key=True, max_length=10)
    ngay_dat = models.DateTimeField(auto_now_add = True, blank=True)
    ngay_giao = models.DateTimeField(auto_now = truncate, blank=True)
    trang_thai = models.IntegerField(default=0)
    tong_tien_hang = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    ma_khuyen_mai = models.ForeignKey(KhuyenMai, on_delete=models.PROTECT, db_column='ma_khuyen_mai', null=True)
    ma_khach_hang = models.ForeignKey(KhachHang, on_delete=models.PROTECT, db_column='ma_khach_hang')
    ma_shipper = models.ForeignKey(Shipper, on_delete=models.PROTECT, db_column='ma_shipper', null=True)
    ma_san_pham = models.ForeignKey(SanPham, on_delete=models.PROTECT, db_column='ma_san_pham', null=True)

    def __str__(self):
        return f"{self.ma_don_hang}, {self.ngay_dat}, {self.ngay_giao}, {self.so_nha}, {self.duong}, {self.phuong}, {self.quan}, {self.thanh_pho}, {self.tong_tien_hang}, {self.ap_dung_khuyen_mai},  {self.gia_tri_khuyen_mai}, {self.tong_so_tien}, {self.ma_khuyen_mai}, {self.ma_khach_hang}, {self.ma_shipper}, {self.ma_san_pham}"

    class Meta:
        managed = True
        db_table = 'don_hang'