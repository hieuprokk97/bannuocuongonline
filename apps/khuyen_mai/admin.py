from django.contrib import admin
from .models import KhuyenMai

class KhuyenMaiModel(admin.ModelAdmin):
    list_display = ['ma_khuyen_mai', 'ten_khuyen_mai', 'mo_ta_khuyen_mai', 'ngay_bat_dau', 'ngay_ket_thuc', 'khuyen_mai_bang_tien', 'gia_tri_khuyen_mai']

admin.site.register(KhuyenMai, KhuyenMaiModel)
