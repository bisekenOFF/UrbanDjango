# Generated by Django 4.2.18 on 2025-01-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('DecimalField', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BooleanField', models.BooleanField()),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]
