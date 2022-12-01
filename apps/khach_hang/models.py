from django.db import models
from apps.nguoi_dung.models import NguoiDung

class KhachHang(models.Model):
    ma_khach_hang = models.IntegerField(primary_key=True)
    ten_khach_hang = models.CharField(max_length=40)
    khach_hang_thuong_xuyen = models.IntegerField()
    sdt = models.CharField(max_length = 11, default=None)
    so_nha = models.CharField(max_length=30, default=None)
    duong = models.CharField(max_length=30, default=None)
    phuong = models.CharField(max_length=30, default=None)
    quan = models.CharField(max_length=30, default=None)
    thanh_pho = models.CharField(max_length=30, default=None)
    ma_nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.PROTECT, db_column='ma_nguoi_dung')

    def __str__(self):
        return f"{self.ma_khach_hang}"
    class Meta:
        managed = True
        db_table = 'khach_hang'
