from functools import reduce
from operator import or_
from django.contrib import admin
from .models import SanPham
# Register your models here.
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_san_pham', 'ten_san_pham', 'don_gia', 'don_vi_tinh', 'thanh_phan', 'mo_ta', 'hinh_anh', 'ma_loai')
    search_fields = ['ma_san_pham']
    list_filter= ('ma_san_pham', 'ten_san_pham', 'don_gia')

admin.site.register(SanPham, SanPhamAdmin)