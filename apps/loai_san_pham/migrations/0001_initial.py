# Generated by Django 4.1 on 2022-10-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoaiSanPham',
            fields=[
                ('ma_loai', models.AutoField(primary_key=True, serialize=False)),
                ('ten_loai', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'loai_san_pham',
                'managed': False,
            },
        ),
    ]
