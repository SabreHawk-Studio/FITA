# Generated by Django 2.0.6 on 2018-07-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('初级', '初级'), ('中级', '中级'), ('高级', '高级')], max_length=2, verbose_name='难度'),
        ),
    ]
