from django.contrib import admin
from apps.khach_hang.models import KhachHang 
# Register your models here.
class KhangHangModel(admin.ModelAdmin):
    list_display = ['ma_khach_hang', 'ten_khach_hang', 'duong', 'phuong', 'quan', 'thanh_pho' ,'khach_hang_thuong_xuyen', 'ma_nguoi_dung']
admin.site.register(KhachHang, KhangHangModel)