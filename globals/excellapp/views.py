from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import staffForm
from .models import UserProfile, student, staff, client_request, client, faculty_det, stu_leave, staff_leavedata, \
    proj_company, remark


def sample(request):
    print("Hi", request.user)
    p = UserProfile.objects.all()
    for i in p:
        print(i.username)
    print(p)

    # obj = UserProfile()
    # obj.username = "a"
    # obj.set_password("a")
    # obj.save()
    obj = UserProfile.objects.get(id=3)
    user = authenticate(username="a", password="a")
    if user is not None:
        login(request, user)
    print(request.user)
    return HttpResponse("hi")


def index(request):
    return render(request, 'publicapp/index.html', {})


def about(request):
    return render(request, 'publicapp/about.html', {})


def software(request):
    return render(request, 'publicapp/software.html', {})


def digital(request):
    return render(request, 'publicapp/digital.html', {})


def android(request):
    return render(request, 'publicapp/android.html', {})


def adindex1(request):
    return render(request, 'publicapp/adindex1.html', {})


def adprosts(request):
    return render(request, 'publicapp/adprosts.html', {})


def form_elements(request):
    return render(request, 'adminapp/form_elements.html', {})


def proindex(request):
    return render(request, 'publicapp/proindex.html', {})


def instructor(request):
    return render(request, 'projectapp/instructor.html', {})


def course(request):
    return render(request, 'projectapp/course.html', {})


def testimonial(request):
    return render(request, 'publicapp/testimonial.html', {})


def stureg(request):
    return render(request, 'publicapp/stureg.html', {})


def stufacdet(request):
    return render(request, 'publicapp/stufacdet.html', {})


def stuprosts(request):
    return render(request, 'publicapp/stuprosts.html', {})


def contact(request):
    return render(request, 'publicapp/contact.html', {})


def stulogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']
        user = student.objects.get(stu_email=uname, stu_password=passw)
        # form=studentForm(instance=user)
        if user is not None:
            return render(request, 'publicapp/stuprofile1.html', {"form": user})
            return HttpResponse("fail")
    return render(request, 'publicapp/stulogin.html', {})


def stafflogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']
        user = staff.objects.get(staff_email=uname, staff_password=passw)
        if user is not None:
            return render(request, 'publicapp/staffprofile.html', {"form": user})
            return HttpResponse("fail")
    return render(request, 'publicapp/stafflogin.html', {})


def clientlogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']
        user = client.objects.get(client_email=uname, client_password=passw)
        if user is not None:
            return render(request, 'publicapp/clientprofile.html', {})
            return HttpResponse("fail")

    return render(request, 'publicapp/clientlogin.html', {})


def adlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        if User.objects.filter(is_superuser=1).exists():
            user = authenticate(request, username=uname, password=passw)
            if user is not None:
                login(request, user)
                return render(request, "publicapp/adindex1.html")
            return HttpResponse('fail')
    else:
        return render(request, "publicapp/adlogin.html", {})


def clientreg(request):
    return render(request, "publicapp/clientreg.html", {})
    # try:
    # client_name=request.GET['client_name']
    # client_email=request.GET['client_email']
    # client_phone=request.GET['client_phone']
    # client_password=request.GET['client_password']
    # p=client(client_name,client_email,client_phone,client_password)
    # p.save()
    # return HttpResponse("success")


def clientreq(request):
    return render(request, "publicapp/clientreq.html", {})


def stuleaveform(request):
    return render(request, 'publicapp/stuleaveform.html', {})


def staffleaveform(request):
    return render(request, 'publicapp/staffleaveform.html', {})


def stufeedback(request):
    return render(request, 'publicapp/stufeedback.html', {})


def stusuggest(request):
    return render(request, 'publicapp/stusuggest.html', {})


def staffprofile(request):
    if request.method == "POST":
        staff_name = request.POST["staff_name"]
        staff_email = request.POST["staff_email"]
        staff_phone = request.POST["staff_phone"]
        staff_address = request.POST["staff_address"]
        staff_job = request.POST["staff_job"]
        staff_exp = request.POST["staff_exp"]
        staff_qualify = request.POST["staff_qualify"]
        staff_salary = request.POST["staff_salary"]
        staff_password = request.POST["staff_password"]
        staff.objects.create(staff_name=staff_name, staff_email=staff_email, staff_phone=staff_phone,
                             staff_address=staff_address, staff_job=staff_job, staff_exp=staff_exp,
                             staff_salary=staff_salary, staff_password=staff_password)
        return render(request, 'publicapp/staffprofile.html', {"test": user})


def clientprofile(request):
    datas = client.objects.get(clients=request.user)
    return render(request, 'publicapp/clientprofile.html', {"profile": datas})


def stuprofile1(request):
    if request.method == "POST":
        stu_name = request.POST["stu_name"]
        stu_email = request.POST["stu_email"]
        stu_phone = request.POST["stu_phone"]
        stu_address = request.POST["stu_address"]
        stu_age = request.POST["stu_age"]
        stu_college = request.POST["stu_college"]
        stu_course = request.POST["stu_course"]
        stu_language = request.POST["stu_language"]
        pro_due = request.POST["pro_due"]
        stu_fee = request.POST["stu_fee"]
        stu_password = request.POST["stu_password"]
        student.objects.create(stu_name=stu_name, stu_email=stu_email, stu_phone=stu_phone, stu_address=stu_address,
                               stu_age=stu_age, stu_college=stu_college, stu_course=stu_course,
                               stu_language=stu_language, stu_due=stu_due, stu_fee=stu_fee, stu_password=stu_password)
        return render(request, 'publicapp/stuprofile1.html', {"test": user})


def viewstaff(request):
    return render(request, 'publicapp/viewstaff.html', {})


def viewstu(request):
    return render(request, 'publicapp/viewstu.html', {})


def viewfac(request):
    return render(request, 'publicapp/viewfac.html', {})


def viewclient(request):
    return render(request, 'publicapp/viewclient.html', {})


def viewclient2(request):
    return render(request, 'publicapp/viewclient2.html', {})


def adstaffleaveform(request):
    return render(request, 'publicapp/adstaffleaveform.html', {})


def adstuleaveform(request):
    return render(request, 'publicapp/adstuleaveform.html', {})


def addstu(request):
    return render(request, 'publicapp/addstu.html', {})
    # if request.method == "POST":
    # form = studentForm(request.POST)
    # if form.is_valid():
    # try:
    # form.save()
    # return redirect('/adindex1')
    # except:
    # pass
    # else:
    # form = studentForm()


def addfac(request):
    if request.method == "POST":
        form = facultyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/adindex1')
            except:
                pass
            else:
                form = facultyForm()
    return render(request, 'publicapp/addfac.html', {})


def addstaff(request):
    # u=staff.objects.create(staff_name=staff_name,staff_email=staff_email,staff_phone=staff_phone,staff_address=staff_address,staff_job=staff_job,staff_exp=staff_exp,staff_qualify=staff_qualify,staff_salary=staff_salary,staff_password=staff_password)
    # formset=staffForm(request.POST)
    # if formset.is_valid():
    # formset.save()
    #  return HttpResponse("Success")
    # else:
    # return HttpResponse(formset.errors)
    if request.method == "POST":
        form = staffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/adindex1')
            except:
                pass
            else:
                form = staffForm()
    return render(request, 'publicapp/addstaff.html')


def view_staff(request):
    all_staff = staff.objects.all()
    return render(request, 'publicapp/viewstaff.html', {'Staffs': all_staff})


def get_studentdata(request):
    all_student_data = student.objects.all()
    return render(request, 'publicapp/viewstu.html', {'allstudentdata': all_student_data})


def get_facultydata(request):
    all_faculty_data = faculty_det.objects.all()
    return render(request, 'publicapp/viewfac.html', {'allfacultydata': all_faculty_data})


def get_studleave(request):
    all_studleave_data = stu_leave.objects.all()
    return render(request, 'publicapp/adstuleaveform.html', {'studleave': all_studleave_data})


def get_staffleave(request):
    all_staffleave_data = staff_leavedata.objects.all()
    return render(request, 'publicapp/adstaffleaveform.html', {'staffleave': all_staffleave_data})


def get_adprosts(request):
    all_adprosts_data = proj_company.objects.all()
    return render(request, 'publicapp/adindex1.html', {'alladprostsdata': all_adprosts_data})


def get_clientdata(request):
    all_client_data = client_request.objects.all()
    return render(request, 'publicapp/viewclient.html', {'allclientdata': all_client_data})


def get_client2data(request):
    all_client2_data = client.objects.all()
    return render(request, 'publicapp/viewclient2.html', {'allclient2data': all_client2_data})


def services(request):
    return render(request, 'publicapp/services.html', {})


def test_clientreq(request):
    company_name = request.POST["company_name"]
    project_title = request.POST["project_title"]
    client_quotation = request.POST["client_quotation"]
    client_duedate = request.POST["client_duedate"]
    client_meet = request.POST["client_meet"]

    datas = client_request(company_name=company_name, project_title=project_title, client_quotation=client_quotation,
                           client_duedate=client_duedate, client_meet=client_meet)
    datas.save()
    return render(request, 'publicapp/clientreq.html')


def stu_leaveform(request):
    stu_name = request.POST["stu_name"]
    # stu_email=request.POST["stu_email"]
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    reason = request.POST["reason"]
    comment = request.POST["comment"]

    data = stu_leave(stu_name=stu_name, from_date=from_date, to_date=to_date, reason=reason, comment=comment)
    data.save()

    return render(request, 'publicapp/stuleaveform.html')


def staff_leaveform(request):
    staff_name = request.POST["staff_name"]
    # stu_email=request.POST["stu_email"]
    staff_dept = request.POST["staff_dept"]
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    reason = request.POST["reason"]
    leave_type = request.POST["leave_type"]
    comment = request.POST["comment"]

    data = staff_leavedata(staff_name=staff_name, staff_dept=staff_dept, from_date=from_date, to_date=to_date,
                           reason=reason, leave_type=leave_type, comment=comment)
    data.save()

    return render(request, 'publicapp/staffleaveform.html')


def stu_remark(request):
    stu_feedback = request.POST["stu_feedback"]
    date = request.POST["date"]

    data = remark(date=date, stu_feedback=stu_feedback)
    data.save()

    return render(request, 'publicapp/stuprofile1.html')


def proj_companysts(request):
    project_title = request.POST["project_title"]
    type_of_proj = request.POST["type_of_proj"]
    proj_sts = request.POST["proj_sts"]
    start_date = request.POST["start_date"]
    proj_duedate = request.POST["proj_duedate"]
    remarks = request.POST["remarks"]

    data = proj_company(project_title=project_title, type_of_proj=type_of_proj, proj_sts=proj_sts,
                        start_date=start_date, proj_duedate=proj_duedate, remarks=remarks)
    data.save()

    return render(request, 'publicapp/staffprofile.html')


def test_fac(request):
    fac_name = request.POST["fac_name"]
    fac_email = request.POST["fac_email"]
    fac_post = request.POST["fac_post"]
    fac_exp = request.POST["fac_exp"]
    fac_qualify = request.POST["fac_qualify"]
    faculty = faculty_det(fac_name=fac_name, fac_email=fac_email, fac_post=fac_post, fac_exp=fac_exp,
                          fac_qualify=fac_qualify)
    faculty.save()
    return render(request, 'publicapp/adindex1.html')


def test_client(request):
    client_name = request.POST["client_name"]
    client_email = request.POST["client_email"]
    client_phone = request.POST["client_phone"]
    client_password = request.POST["client_password"]

    datas = client(client_name=client_name, client_email=client_email, client_phone=client_phone,
                   client_password=client_password)
    datas.save()
    return render(request, 'publicapp/clientreq.html')


# Create your views here.
def test_test(request):
    staff_name = request.POST["staff_name"]
    staff_email = request.POST["staff_email"]
    staff_phone = request.POST["staff_phone"]
    staff_address = request.POST['staff_address']
    staff_job = request.POST['staff_job']
    staff_exp = request.POST['staff_exp']
    staff_qualify = request.POST['staff_qualify']
    staff_salary = request.POST['staff_salary']
    staff_password = request.POST['staff_password']

    alldata = staff(staff_name=staff_name, staff_email=staff_email, staff_phone=staff_phone,
                    staff_address=staff_address, staff_job=staff_job, staff_exp=staff_exp, staff_qualify=staff_qualify,
                    staff_salary=staff_salary, staff_password=staff_password)
    alldata.save()
    return render(request, 'publicapp/adindex1.html')


def test_stu(request):
    stu_name = request.POST["stu_name"]
    stu_email = request.POST["stu_email"]
    stu_phone = request.POST["stu_phone"]
    stu_address = request.POST["stu_address"]
    stu_age = request.POST["stu_age"]
    stu_college = request.POST["stu_college"]
    stu_course = request.POST["stu_course"]
    stu_language = request.POST["stu_language"]
    pro_due = request.POST["pro_due"]
    stu_fee = request.POST["stu_fee"]
    stu_password = request.POST["stu_password"]

    alldata = student(stu_name=stu_name, stu_email=stu_email, stu_phone=stu_phone, stu_address=stu_address,
                      stu_age=stu_age, stu_college=stu_college, stu_course=course, stu_language=stu_language,
                      pro_due=pro_due, stu_fee=stu_fee, stu_password=stu_password)
    alldata.save()

    return render(request, 'publicapp/adindex1.html')


from django.conf import settings
from django.core.mail import send_mail


def test_test(request):
    staff_name = request.POST["staff_name"]
    staff_email = request.POST["staff_email"]
    staff_phone = request.POST["staff_phone"]
    staff_address = request.POST['staff_address']
    staff_job = request.POST['staff_job']
    staff_exp = request.POST['staff_exp']
    staff_qualify = request.POST['staff_qualify']
    staff_salary = request.POST['staff_salary']
    staff_password = request.POST['staff_password']

    alldata = staff(staff_name=staff_name, staff_email=staff_email, staff_phone=staff_phone,
                    staff_address=staff_address, staff_job=staff_job, staff_exp=staff_exp, staff_qualify=staff_qualify,
                    staff_salary=staff_salary, staff_password=staff_password)
    alldata.save()
    return render(request, 'publicapp/adindex1.html')


def approve(request):
    print("inside approve")
    # employee = client_request.objects.get(id="1")
    # employee.approved = True
    # employee.save()
    subject = 'welcome to Praveen world'
    message = f'Hi thank you for registering in Excellence Academy.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["praveenmv93@gmail.com", ]
    context = {
        "d": "d",
    }
    send_mail(subject, message, email_from, recipient_list)
    # return redirect('/get_clientdata/')
    return HttpResponse("d")


def clientprojects(request):
    print("inside projects")
