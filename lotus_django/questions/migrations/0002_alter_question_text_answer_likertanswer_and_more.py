# Generated by Django 5.0.3 on 2024-04-06 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0007_user_remove_entry_user_remove_journal_entry_and_more'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=255),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.user')),
            ],
        ),
        migrations.CreateModel(
            name='LikertAnswer',
            fields=[
                ('likert_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotus.user')),
            ],
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('text_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=30)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
            ],
        ),
    ]