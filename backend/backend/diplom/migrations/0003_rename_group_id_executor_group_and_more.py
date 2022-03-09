# Generated by Django 4.0.3 on 2022-03-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0002_rename_dictgroup_dict_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='executor',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='executor',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='lab',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='permission_id',
            new_name='permission',
        ),
        migrations.RenameField(
            model_name='user_has_courses',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='user_has_courses',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user_has_labs',
            old_name='lab_id',
            new_name='lab',
        ),
        migrations.RenameField(
            model_name='user_has_labs',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='user_id',
        ),
    ]