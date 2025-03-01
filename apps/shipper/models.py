# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Shipper(models.Model):
    ma_shipper = models.IntegerField(primary_key=True)
    ten_shipper = models.CharField(max_length=30)
    tien_luong = models.DecimalField(max_digits=10, decimal_places=2)
    nam_sinh = models.DateField()

    def __str__(self):
        return f"{self.ma_shipper}"

    class Meta:
        managed = True
        db_table = 'shipper'
