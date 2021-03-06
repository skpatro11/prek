# Generated by Django 4.0.5 on 2022-06-25 03:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('prek', '0002_added_course_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('monthly_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monthly_discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('yearly_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('yearly_discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_plans', to='prek.course')),
            ],
            options={
                'db_table': 'plans',
            },
        ),
    ]
