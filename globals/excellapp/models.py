from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from django.db import models


# Create your models here.
class Name(models.Model):
    name_value = models.CharField(max_length=100)

    def __str__(self):  # if Python 2 use __unicode__
        return self.name_value


class UserProfile(User):
    user_mobile = models.IntegerField(null=True)


class staff(models.Model):
    staff = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=50)
    staff_email = models.EmailField(max_length=50)
    staff_phone = models.IntegerField()
    staff_address = models.CharField(max_length=100)
    staff_job = models.CharField(max_length=50)
    staff_exp = models.CharField(max_length=10)
    staff_qualify = models.CharField(max_length=30)
    staff_salary = models.IntegerField()
    staff_password = models.CharField(max_length=10)


class client(models.Model):
    clients = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField(max_length=50)
    client_phone = models.IntegerField()
    client_password = models.CharField(max_length=50)


class client_request(models.Model):
    # client_id=models.ForeignKey(client,on_delete=models.DO_NOTHING)
    clients = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    project_title = models.CharField(max_length=50)
    client_quotation = models.CharField(max_length=50)
    client_duedate = models.DateField()
    client_meet = models.CharField(max_length=30)
    # approved = models.BooleanField()


class projects(models.Model):
    project_name = models.CharField(max_length=120, blank=True, null=True)
    project_client = models.ForeignKey(client, on_delete=models.CASCADE, blank=True, null=True)


class client_suggestion(models.Model):
    # client_id=models.ForeignKey(client,on_delete=models.DO_NOTHING)
    clients = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    projects = models.ForeignKey(projects, on_delete=models.CASCADE, blank=True, null=True)
    suggestion = models.CharField(max_length=100)
    ad_approve = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class client_notify(models.Model):
    # client_id=models.ForeignKey(client,on_delete=models.DO_NOTHING)
    clients = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    client_meetd = models.DateField()
    client_meett = models.TimeField()
    proj_update = models.CharField(max_length=50)


class proj_sts(models.Model):
    client_id = models.ForeignKey(client, on_delete=models.CASCADE, blank=True, null=True)
    projects = models.ForeignKey(projects, on_delete=models.CASCADE, blank=True, null=True)
    sts_date = models.DateField()
    sts_des = models.CharField(max_length=50)


class student(models.Model):
    student = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=30)
    stu_email = models.EmailField(max_length=50)
    stu_phone = models.IntegerField()
    stu_address = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    stu_college = models.CharField(max_length=50)
    stu_course = models.CharField(max_length=30)
    stu_language = models.CharField(max_length=50)
    pro_due = models.DateField()
    stu_fee = models.CharField(max_length=20)
    stu_password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class stu_attend(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    attend_per = models.CharField(max_length=10)


class remark(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    stu_feedback = models.CharField(max_length=100)
    date = models.DateField()


class stu_suggestion(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    suggestion = models.CharField(max_length=100)
    ad_approve = models.CharField(max_length=20)


class stu_leave(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    stu_name = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=10)
    comment = models.CharField(max_length=50)


class stu_pro_sts(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    pro_sts = models.CharField(max_length=100)


class faculty_det(models.Model):
    fac_name = models.CharField(max_length=50)
    fac_email = models.EmailField(max_length=50)
    fac_post = models.CharField(max_length=30)
    fac_exp = models.CharField(max_length=30)
    fac_qualify = models.CharField(max_length=40)


class fin_report(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, blank=True, null=True)
    report = models.CharField(max_length=100)
    date = models.DateField()


class proj_company(models.Model):
    client_id = models.ForeignKey(client, on_delete=models.CASCADE, blank=True, null=True)
    project_title = models.CharField(max_length=100)
    type_of_proj = models.CharField(max_length=100)
    proj_sts = models.CharField(max_length=50)
    start_date = models.DateField()
    proj_duedate = models.DateField()
    remarks = models.CharField(max_length=100)


class staff_attend(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, blank=True, null=True)
    staff_name = models.CharField(max_length=30)
    staff_email = models.EmailField(max_length=50)
    staff_job = models.CharField(max_length=50)
    per_attend = models.CharField(max_length=20)


class staff_joballoc(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE, blank=True, null=True)
    staff_email = models.EmailField(max_length=50)
    staff_alloc = models.CharField(max_length=50)
    job_desc = models.CharField(max_length=100)
    accept_reject = models.CharField(max_length=50)


class staff_leave(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_dept = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=10)
    leave_type = models.CharField(max_length=10)
    comment = models.CharField(max_length=50)


class staff_leavedata(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_dept = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=10)
    leave_type = models.CharField(max_length=10)
    comment = models.CharField(max_length=50)
