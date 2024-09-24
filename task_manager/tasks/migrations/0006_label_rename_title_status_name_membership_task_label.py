# Generated by Django 5.1.1 on 2024-09-24 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_rename_performer_task_executor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.RenameField(
            model_name='status',
            old_name='title',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.label', verbose_name='Label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='Task')),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
                'db_table': 'task_label_membership',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, related_name='task_as_label', through='tasks.Membership', to='tasks.label', verbose_name='Label'),
        ),
    ]
