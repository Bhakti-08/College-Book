from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
import csv,io
from main.models import TestSubject, TestQuestions, Subjects, Branch, Tests, Professors, Students, QuestionBank
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
#from django.db import models
#from . import models
#from django.contrib.auth.decorators import permission_required

def index(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        role = request.POST.get('role')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            if role=='Professor':
                    #obj = Professors.objects.get(subjectID=username,password=pass1)
                    return render(request,'profHome.html',{'data':username})
            if role=='Student':
                    #obj = Students.objects.get(email=username,password=pass1,role=role)
                    return render(request,'studentHome.html',{'data':username})
        else:
            return HttpResponse('Enter valid login details...')
    else:
        return render(request, 'index.html',{'data':''})

def addingTest(request,email):
    if request.method=='POST':
        obj1 = Professors.objects.get(email=email,role='Professor')
        subject = obj1.subject
        obj2 = Subjects.objects.get(subject=subject)
        branch = obj2.branch
        testName = request.POST.get('tname')
        new_test = Tests(branch=branch,subject=subject,testName=testName)
        new_test.save()
        return redirect('profHome')
    return render(request,'addingTest.html')

def profRegistrationForm(request):
    if request.method=='POST':
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        branch = request.POST.get('branch')
        subjectID = request.POST.get('subjectID')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(password==pass2):
            new_user = Professors(firstName=firstName,lastName=lastName,branch=branch,subjectID=subjectID,email=email,password=password)
            new_user.save()
            # username = email
            my_user = User.objects.create_user(subjectID,email,password)
            my_user.save()
            return redirect('login')
        else:
            data = '</br><b>Provide valid details!!</b>'
            return render(request, 'profRegistrationForm.html',{'data':data})
    else:
        return render(request, 'profRegistrationForm.html',{'data':''})
    
def studentRegistrationForm(request):
    if request.method=='POST':
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        branch = request.POST.get('branch')
        registrationNum = request.POST.get('registrationNum')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(password==pass2):
            new_user = Students(firstName=firstName,lastName=lastName,branch=branch,registrationNum=registrationNum,email=email,password=password)
            new_user.save()
            # username = email
            my_user = User.objects.create_user(email,email,password)
            my_user.save()
            return redirect('login')
        else:
            data = '</br><b>Provide valid details!!</b>'
            return render(request, 'studentRegistrationForm.html',{'data':data})
    else:
        return render(request, 'studentRegistrationForm.html',{'data':''})

@login_required(login_url='login')
def profHome(request,subID):
    obj = Professors.objects.get(subjectID=subID)
    return render(request,'profHome.html',{'data':obj.subjectID})

@login_required(login_url='login')
def studentHome(request,email):
    return render(request,'studentHome.html',{'data':email})

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def upload_questionBank(request,subID):
    # defining order of content in csv file
    prompt = {
        'order': '<b>NOTE:</b> Order of CSV file contents should be test id, question, option_1, option_2, option_3, option_4, correct_option'
    }
    # checking whether the method is POST or not
    if request.method == 'GET':
        return render(request,'upload_questionBank.html',prompt)
    csv_file = request.FILES['file']    # 'file' is name given to that uploaded file in test-arranged.html 
    data = ''
    # checking whether uploaded file is CSV or not
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Uploaded file is not CSV File !!!')
        return render(request, 'upload_questionBank.html', {'data':data})
    #temp = Professors.objects.get(subjectID=subID)
    #subID = temp.subjectID
    obj = QuestionBank(subjectID=subID,questionBank=csv_file)
    obj.save()
    data = '</br><b>Your File Is Sucessfully Uploaded :)</b>'
    return render(request, 'upload_questionBank.html', {'data':data})

@login_required(login_url='login')    # only logined person can visit the questions
def test_subject(request):
    subject = TestSubject.objects.all()
    return render(request, 'test-subject.html',{'data':subject})

@login_required(login_url='login')    # only logined person can visit the questions
def selectBranch(request):
    branch = Branch.objects.all()
    return render(request, 'selectBranch.html',{'data':branch})

def selectTest(request,branchID):
    branch = Branch.objects.get(id=branchID)
    obj = Tests.objects.filter(branch=branch).order_by('id')
    return render(request,'selectTest.html',{'data':obj})

# Displaying questions according to subject
@login_required(login_url='login')     # only logined person can visit the questions
def test_question(request,test_id):
    subject = TestSubject.objects.get(id=test_id)
    question = TestQuestions.objects.filter(subject=subject).order_by('id')
    output = {'final_questions' : question, 'subject' : subject}
    '''paginator = Paginator(question,1)
    page_number = request.GET.get('page')
    final_questions = paginator.get_page(page_number) 
    total_page = final_questions.paginator.num_pages
    output = {
            'question' : question, 
            'subject' : subject, 
            'final_questions' : final_questions, 
            'last_page' : total_page,
            'totalPagelist' : [n+1 for n in range(total_page)]
         }'''
    return render(request, 'test-question.html',output)

@login_required(login_url='login')
def add_test(request):
    obj = None
    check = True
    if request.method=='POST':
        test_name = request.POST.get('test_name')
        obj1 = TestSubject.objects.all()
        for i in obj1:
            if i.test_name==test_name:
                obj = i.id
                check = False
                break
        if check:
            obj2 = TestSubject(test_name=test_name)
            obj2.save()
            obj = obj2.id
    return render(request, 'add-test.html', {'data':obj})

# @permission_required('admin.can_add_log_entry')  => admin i.e. superuser can access this page 
@login_required(login_url='login')
def test_arranged(request):
    # defining order of content in csv file
    prompt = {
        'order': '<b>NOTE:</b> Order of CSV file contents should be test id, question, option_1, option_2, option_3, option_4, correct_option'
    }
    # checking whether the method is POST or not
    if request.method == 'GET':
        return render(request,'test-arranged.html',prompt)
    csv_file = request.FILES['file']    # 'file' is name given to that uploaded file in test-arranged.html 
    data = ''
    # checking whether uploaded file is CSV or not
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Uploaded file is not CSV File !!!')
        return render(request, 'test-arranged.html', {'data':data})
        #return HttpResponseRedirect("{% url 'test_arranged' %}")
        #return HttpResponseRedirect('test-arranged.html')
    # decoding it for data set model
    data_set = csv_file.read().decode('UTF-8')
    lines = data_set.split('\n')
    for line in lines:
        records = line.split(',')
        sub = TestSubject.objects.get(id=records[0])
        TestQuestions.objects.update_or_create(
            subject = sub,
            question = records[1],
            opt_1 = records[2],
            opt_2 = records[3],
            opt_3 = records[4],
            opt_4 = records[5],
            right_opt = records[6]
        )
    # this will udate table with all row values provided in tuple form => can't use save()
    data = '</br><b>Your File Is Sucessfully Uploaded :)</b>'
    return render(request, 'test-arranged.html', {'data':data})
