# Generated by Django 3.2 on 2023-04-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.TextField(max_length=200, null=True)),
                ('customer_review', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]