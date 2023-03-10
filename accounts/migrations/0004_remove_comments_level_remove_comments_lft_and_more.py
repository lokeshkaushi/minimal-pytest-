# Generated by Django 4.1.4 on 2023-02-13 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='level',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='userss', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('rid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('Comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='accounts.comments')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounts.reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
