# Generated by Django 2.0 on 2017-12-09 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timeline', '0002_auto_20171207_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='postcomments',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commentlikes',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='timeline.PostComments'),
        ),
        migrations.AddField(
            model_name='commentlikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='commentlikes',
            unique_together={('comment', 'user')},
        ),
    ]
