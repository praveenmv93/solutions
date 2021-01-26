from django.urls import path

from .views import sample, index, about, software, digital, android, adindex1, adprosts, form_elements, proindex, \
    instructor, course, testimonial, stureg, stuprosts, stufacdet, contact, stulogin, stafflogin, clientlogin, \
    clientreg, clientreq, approve, stuleaveform, staffleaveform, stufeedback, stusuggest, clientprofile, staffprofile, \
    stuprofile1, viewstaff, viewstu, viewfac, viewclient, viewclient2, adstaffleaveform, adstuleaveform, addstu, \
    addstaff, view_staff, get_studentdata, get_facultydata, get_studleave, get_staffleave, get_adprosts, get_clientdata, \
    get_client2data, services, test_clientreq, staff_leaveform, stu_leaveform, stu_remark, proj_companysts, test_client, \
    test_fac, test_test, suggestions, clientprojects

urlpatterns = [

    path('test/', sample, name='home'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('software/', software, name='software'),
    path('digital/', digital, name='digital'),
    path('android/', android, name='android'),
    path('adindex1/', adindex1, name='adindex1'),
    path('adprosts/', adprosts, name='adprosts'),
    path('form_elements/', form_elements, name='form_elements'),
    path('proindex/', proindex, name='proindex'),
    path('instructor/', instructor, name='instructor'),
    path('course/', course, name='course'),
    path('testimonial/', testimonial, name='testimonial'),
    path('stureg/', stureg, name='stureg'),
    path('stuprosts/', stuprosts, name='stuprosts'),
    path('stufacdet/', stufacdet, name='stufacdet'),
    path('contact/', contact, name='contact'),
    path('stulogin/', stulogin, name='stulogin'),
    path('stafflogin/', stafflogin, name='stafflogin'),
    path('clientlogin/', clientlogin, name='clientlogin'),
    path('clientreg/', clientreg, name='clientreg'),
    path('clientreq/', clientreq, name='clientreq'),
    path('stuleaveform/', stuleaveform, name='stuleaveform'),
    path('staffleaveform/', staffleaveform, name='staffleaveform'),
    path('stufeedback/', stufeedback, name='stufeedback'),
    path('stusuggest/', stusuggest, name='stusuggest'),
    path('approve/', approve, name='approve'),
    path('staffprofile/', staffprofile, name='staffprofile'),
    path('clientprofile/', clientprofile, name='clientprofile'),
    path('stuprofile1/', stuprofile1, name='stuprofile1'),
    path('viewstaff/', viewstaff, name='viewstaff'),
    path('viewstu/', viewstu, name='viewstu'),
    path('viewfac/', viewfac, name='viewfac'),
    path('viewclient/', viewclient, name='viewclient'),
    path('viewclient2/', viewclient2, name='viewclient2'),
    path('adstaffleaveform/', adstaffleaveform, name='adstaffleaveform'),
    path('adstuleaveform/', adstuleaveform, name='adstuleaveform'),
    path('addstu/', addstu, name='addstu'),
    path('addstaff/', addstaff, name='addstaff'),
    path('view_staff/', view_staff, name='view_staff'),
    path('get_studentdata/', get_studentdata, name='get_studentdata'),
    path('get_facultydata/', get_facultydata, name='get_facultydata'),
    path('get_studleave/', get_studleave, name='get_studleave'),
    path('get_staffleave/', get_staffleave, name='get_staffleave'),
    path('get_adprosts/', get_adprosts, name='get_adprosts'),
    path('get_clientdata/', get_clientdata, name='get_clientdata'),
    path('get_client2data/', get_client2data, name='get_client2data'),
    path('services/', services, name='services'),
    path('test_clientreq/', test_clientreq, name='test_clientreq'),
    path('stu_leaveform/', stu_leaveform, name='stu_leaveform'),
    path('staff_leaveform/', staff_leaveform, name='staff_leaveform'),
    path('stu_remark/', stu_remark, name='stu_remark'),
    path('proj_companysts/', proj_companysts, name='proj_companysts'),
    path('test_fac/', test_fac, name='test_fac'),
    path('test_client/', test_client, name='test_client'),
    path('test_test/', test_test, name='test_test'),
    path('suggestions/<int:id>/', suggestions, name='suggestions'),
    path('clientprojects/', clientprojects, name='clientprojects'),

    # path('login', login_view, name='login'),
    # path('register', register, name='register'),
    # path('logout', logout_request, name='logout'),
    #
    # path('api/post/', PostCreate.as_view(), name='post_create'),
    # path('api/post/<int:id>', RetrieveUpdateDestroyView.as_view(), name='post_operatons'),

]
