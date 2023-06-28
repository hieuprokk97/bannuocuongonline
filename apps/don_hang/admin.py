from django.contrib import admin
from .models import DonHang

class DonHangAdmin(admin.ModelAdmin):
    list_display = ['ma_don_hang', 'ten_don_hang' ,'ngay_dat', 'ngay_giao', 'trang_thai',
                    'ma_khach_hang', 'ma_shipper']

admin.site.register(DonHang, DonHangAdmin)
# Register your models here.
