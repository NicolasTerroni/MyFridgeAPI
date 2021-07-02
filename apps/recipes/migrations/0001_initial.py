# Generated by Django 3.1.3 on 2021-07-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Last date time on which the object was modified.', verbose_name='modified_at')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='recipes/pictures')),
                ('description', models.TextField(blank=True, max_length=150)),
                ('instructions', models.TextField(blank=True)),
                ('is_veggie', models.BooleanField(default=False, help_text='Recipes with ingredients that do not contain meat or derivatives.')),
                ('is_vegan', models.BooleanField(default=False, help_text='Recipes with ingredients that do not come from animals.')),
                ('ingredients', models.ManyToManyField(related_name='recipe_ingredients', to='ingredients.Ingredient')),
            ],
            options={
                'ordering': ('-created', '-modified'),
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
