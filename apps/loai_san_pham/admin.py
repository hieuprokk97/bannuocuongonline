from asyncio import format_helpers
from audioop import reverse
from configparser import LegacyInterpolation
from urllib.parse import urlencode
from django.contrib import admin
from .models import LoaiSanPham
# Register your models here.
class LoaiSanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_loai', 'ten_loai')
    search_fields = ['ten_loai']
    list_filter = ('ma_loai', 'ten_loai')
admin.site.register(LoaiSanPham, LoaiSanPhamAdmin)