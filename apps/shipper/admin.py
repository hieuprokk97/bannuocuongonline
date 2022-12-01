from django.contrib import admin
from apps.shipper.models import Shipper
# Register your models here.
class ShipperAdmin(admin.ModelAdmin):
    list_display = ['ma_shipper', 'ten_shipper', 'tien_luong', 'nam_sinh']

admin.site.register(Shipper, ShipperAdmin)
