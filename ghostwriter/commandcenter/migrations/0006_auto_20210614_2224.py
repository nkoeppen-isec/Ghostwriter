# Generated by Django 3.0.10 on 2021-06-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandcenter', '0005_auto_20201102_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='namecheapconfiguration',
            name='reset_dns',
            field=models.BooleanField(default=False, help_text='Reset DNS records when releasing a checked-out domain', verbose_name='Reset DNS Records'),
        ),
        migrations.AlterField(
            model_name='namecheapconfiguration',
            name='api_key',
            field=models.CharField(default='Namecheap API Key', help_text='Your Namecheap API key', max_length=255),
        ),
        migrations.AlterField(
            model_name='namecheapconfiguration',
            name='api_username',
            field=models.CharField(default='API Username', help_text='Your Namecheap API username', max_length=255, verbose_name='API Username'),
        ),
        migrations.AlterField(
            model_name='namecheapconfiguration',
            name='client_ip',
            field=models.CharField(default='Your external IP address registered with Namecheap', max_length=255, verbose_name='Whitelisted IP Address'),
        ),
        migrations.AlterField(
            model_name='namecheapconfiguration',
            name='page_size',
            field=models.IntegerField(default=100, verbose_name='Page Size'),
        ),
        migrations.AlterField(
            model_name='namecheapconfiguration',
            name='username',
            field=models.CharField(default='Account Username', help_text='Your Namecheap username', max_length=255),
        ),
    ]