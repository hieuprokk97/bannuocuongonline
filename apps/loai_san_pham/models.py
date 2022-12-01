# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LoaiSanPham(models.Model):
    ma_loai = models.CharField(primary_key=True, max_length = 20)
    ten_loai = models.CharField(max_length=30)
    hinh_anh_loai = models.ImageField(null = True, blank = True, upload_to = "img/sanpham/")

    def __str__(self):
        return f"{self.ma_loai}"
    class Meta:
        managed = True
        db_table = 'loai_san_pham'
