# Generated by Django 3.1.7 on 2021-02-25 23:54

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20, verbose_name='Subject')),
                ('title', models.TextField(verbose_name=' ')),
                ('optionA', models.CharField(max_length=30, verbose_name='Aoption')),
                ('optionB', models.CharField(max_length=30, verbose_name='Boption')),
                ('optionC', models.CharField(max_length=30, verbose_name='Coption')),
                ('optionD', models.CharField(max_length=30, verbose_name='Doption')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10, verbose_name='answer')),
                ('level', models.CharField(choices=[('2', 'general'), ('1', 'easy'), ('3', 'difficult')], max_length=10, verbose_name='level')),
                ('score', models.IntegerField(default=1, verbose_name='score')),
            ],
            options={
                'verbose_name': 'Single choice question bank',
                'verbose_name_plural': 'Single choice question bank',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (5, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Teacher ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, verbose_name='Gender')),
                ('Dept', models.CharField(choices=[('College of Computer and Communication', 'College of Computer and Communication'), ('School of Electrical and Automation', 'School of Electrical and Automation'), ('Foreign Language Institute', 'Foreign Language Institute'), ('College of Science', 'College of Science')], default=None, max_length=40, verbose_name='College')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='mailbox')),
                ('password', models.CharField(default='000000', max_length=20, verbose_name='password')),
                ('birth', models.DateField(verbose_name='date of birth')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ManyToManyField(to='SchoolManagement.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=20, verbose_name='Subject')),
                ('Major', models.CharField(max_length=20, verbose_name='Applicable for test papers')),
                ('examtime', models.DateTimeField()),
                ('Tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolManagement.teacher')),
                ('pid', models.ManyToManyField(to='SchoolManagement.Question')),
            ],
            options={
                'verbose_name': 'Test paper',
                'verbose_name_plural': 'Test paper',
                'db_table': 'paper',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email_address')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(upload_to='media/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SchoolManagement.usermanager')),
                ('approved', models.BooleanField(default=False)),
                ('enrolled', models.ManyToManyField(related_name='enrolled_subjects', to='SchoolManagement.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=20, verbose_name='Subject')),
                ('grade', models.IntegerField()),
                ('sid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SchoolManagement.student')),
            ],
            options={
                'verbose_name': 'Achievement',
                'verbose_name_plural': 'Achievement',
                'db_table': 'grade',
            },
        ),
    ]
