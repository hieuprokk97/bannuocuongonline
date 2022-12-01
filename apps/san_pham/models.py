# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.loai_san_pham.models import LoaiSanPham
from django.utils.html import mark_safe
from django.db.models import Count
class SanPham(models.Model):
    ma_san_pham = models.CharField(primary_key=True, max_length = 20)
    ten_san_pham = models.CharField(max_length=100)
    don_gia = models.DecimalField(max_digits=10, decimal_places=2)
    don_vi_tinh = models.CharField(max_length=10)
    thanh_phan = models.TextField(default = '')
    mo_ta = models.TextField(default = '')
    hinh_anh = models.ImageField(null = True, blank = True, upload_to = "img/sanpham/")
    ma_loai = models.ForeignKey(LoaiSanPham, on_delete=models.PROTECT, db_column='ma_loai')
    
    def image_preview(self):
        if self.hinh_anh:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.hinh_anh.url))
        return ""

    def __str__(self):
        return f"{self.ma_san_pham}"
    class Meta:
        managed = True
        db_table = 'san_pham'
