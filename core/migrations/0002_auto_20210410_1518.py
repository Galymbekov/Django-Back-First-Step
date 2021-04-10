# Generated by Django 3.1.8 on 2021-04-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.DecimalField(decimal_places=100000, max_digits=1000000, max_length=1000000),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20000),
        ),
    ]
