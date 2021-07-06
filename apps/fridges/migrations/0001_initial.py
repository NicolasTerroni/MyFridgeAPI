# Generated by Django 3.1.3 on 2021-07-03 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Last date time on which the object was modified.', verbose_name='modified_at')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('ingredients', models.ManyToManyField(related_name='fridge_ingredients', to='ingredients.Ingredient')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created', '-modified'),
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
