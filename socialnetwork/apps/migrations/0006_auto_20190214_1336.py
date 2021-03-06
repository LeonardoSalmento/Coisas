# Generated by Django 2.1.5 on 2019-02-14 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20190214_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='apps.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_posts', to='apps.Profile'),
        ),
    ]
