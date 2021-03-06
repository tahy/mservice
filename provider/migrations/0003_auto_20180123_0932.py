# Generated by Django 2.0.1 on 2018-01-23 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20180123_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
            ],
        ),
        migrations.AlterField(
            model_name='area',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Provider', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='area',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='provider.Service', verbose_name='Услуга'),
            preserve_default=False,
        ),
    ]
