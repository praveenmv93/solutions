# Generated by Django 3.1.5 on 2021-01-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excellapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_email', models.EmailField(max_length=50)),
                ('client_phone', models.IntegerField()),
                ('client_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='client_notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_meetd', models.DateField()),
                ('client_meett', models.TimeField()),
                ('proj_update', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='client_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('project_title', models.CharField(max_length=50)),
                ('client_quotation', models.CharField(max_length=50)),
                ('client_duedate', models.DateField()),
                ('client_meet', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='client_suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=100)),
                ('ad_approve', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_name', models.CharField(max_length=50)),
                ('fac_email', models.EmailField(max_length=50)),
                ('fac_post', models.CharField(max_length=30)),
                ('fac_exp', models.CharField(max_length=30)),
                ('fac_qualify', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='fin_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='proj_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('type_of_proj', models.CharField(max_length=100)),
                ('proj_sts', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('proj_duedate', models.DateField()),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='proj_sts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sts_date', models.DateField()),
                ('sts_des', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_feedback', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_email', models.EmailField(max_length=50)),
                ('staff_phone', models.IntegerField()),
                ('staff_address', models.CharField(max_length=100)),
                ('staff_job', models.CharField(max_length=50)),
                ('staff_exp', models.CharField(max_length=10)),
                ('staff_qualify', models.CharField(max_length=30)),
                ('staff_salary', models.IntegerField()),
                ('staff_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='staff_attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_email', models.EmailField(max_length=50)),
                ('staff_job', models.CharField(max_length=50)),
                ('per_attend', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='staff_joballoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_email', models.EmailField(max_length=50)),
                ('staff_alloc', models.CharField(max_length=50)),
                ('job_desc', models.CharField(max_length=100)),
                ('accept_reject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='staff_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_dept', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.CharField(max_length=10)),
                ('leave_type', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='staff_leavedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_dept', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.CharField(max_length=10)),
                ('leave_type', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='stu_attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend_per', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='stu_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='stu_pro_sts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_sts', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stu_suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=100)),
                ('ad_approve', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_email', models.EmailField(max_length=50)),
                ('stu_phone', models.IntegerField()),
                ('stu_address', models.CharField(max_length=100)),
                ('stu_age', models.IntegerField()),
                ('stu_college', models.CharField(max_length=50)),
                ('stu_course', models.CharField(max_length=30)),
                ('stu_language', models.CharField(max_length=50)),
                ('pro_due', models.DateField()),
                ('stu_fee', models.CharField(max_length=20)),
                ('stu_password', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
