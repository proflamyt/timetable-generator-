# Generated by Django 3.2 on 2021-09-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.IntegerField(blank=True, default=1, null=True)),
                ('course_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('size', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('size', models.IntegerField(default=0)),
                ('lab', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.IntegerField(default=1, null=True)),
                ('time', models.IntegerField(choices=[(1, 'an hour class'), (2, 'two hours class'), (3, 'three hours class')], default=1)),
                ('lab', models.BooleanField(default=False)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
                ('department', models.ManyToManyField(to='timetable.Department')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.instructor')),
            ],
        ),
    ]