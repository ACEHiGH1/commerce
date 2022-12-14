# Generated by Django 4.1.1 on 2022-10-24 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='userWatchlistListings', to='auctions.auctionlisting'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
