# Generated by Django 4.1 on 2022-10-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('san_pham', '0002_sanpham_hinh_anh_sanpham_mo_ta_sanpham_thanh_phan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='hinh_anh',
            field=models.ImageField(upload_to='static/img/sanpham/'),
        ),
    ]
