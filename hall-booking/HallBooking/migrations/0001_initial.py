# Generated by Django 3.0 on 2021-06-12 05:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10)),
                ('age', models.IntegerField(default=18)),
                ('mobile_no', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
                ('pid_no', models.CharField(max_length=10)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('im', models.ImageField(default='avatar.png', upload_to='Profile_pics/')),
                ('role', models.IntegerField(choices=[(0, 'guest'), (1, 'user'), (2, 'manager')], default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
            name='RoleRqst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('roletype', models.PositiveIntegerField(choices=[(1, 'user'), (2, 'manager')])),
                ('proof', models.ImageField(blank=True, upload_to='')),
                ('is_checked', models.BooleanField(default=0)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField()),
                ('your_address', models.CharField(max_length=70)),
                ('occupation', models.CharField(max_length=30)),
                ('male_birthc', models.FileField(upload_to='CertificateProofs/')),
                ('female_birthc', models.FileField(upload_to='CertificateProofs/')),
                ('rooms_needed', models.IntegerField(default=2)),
                ('date', models.DateField(null=True)),
                ('timings', models.CharField(default='AM to PM', max_length=30)),
                ('noof_hours', models.IntegerField(default=3)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdHl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=50)),
                ('halltype', models.CharField(choices=[('Marriage', 'Marriage'), ('Seminar', 'Seminar'), ('Event', 'Event')], default='Event', max_length=10)),
                ('aircond', models.CharField(choices=[('AC', 'Ac'), ('Non-AC', 'Non-AC')], default='Non-AC', max_length=10)),
                ('ACHall_Amount', models.CharField(default='25000 per hour', max_length=30)),
                ('NonACHall_Amount', models.CharField(default='20000 per hour', max_length=30)),
                ('occupancy', models.IntegerField(null=True)),
                ('rooms', models.IntegerField(default=0)),
                ('ACRoom_Cost', models.CharField(default='5000 per hour', max_length=30)),
                ('NonACRoom_Cost', models.CharField(default='3000 per hour', max_length=30)),
                ('area', models.CharField(max_length=20)),
                ('advance', models.IntegerField(default=300)),
                ('status', models.CharField(default='Available', max_length=50)),
                ('fil', models.FileField(upload_to='Hall_Images/')),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
