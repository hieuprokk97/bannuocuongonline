from django.contrib import admin
from apps.nguoi_dung.models import NguoiDung
# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ma_nguoi_dung', 'tai_khoan', 'mat_khau', 'loai_tai_khoan', 'email')
admin.site.register(NguoiDung, NguoiDungAdmin)