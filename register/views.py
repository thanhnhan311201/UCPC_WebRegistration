from django.shortcuts import render, redirect
from .forms import teamForm, loginForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import Team
from django.contrib.auth.decorators import login_required

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("List_of_teams")
wks = spreadsheet.worksheet("demo")

# Create your views here.
def home(request):
    context = {}
    return render(request, 'register/home.html', context)

class register(View):
    def get(self, request):
        context = {'tf': teamForm}
        return render(request, 'register/register.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            tf = teamForm(request.POST)
            if tf.is_valid():
                Username = request.POST['team']
                Email = request.POST['email']
                Password = request.POST['password']
                tf.save()

                idx = len(wks.get_all_values()) + 1
                wks.update_cell(idx, 1, request.POST['team'])
                wks.update_cell(idx, 2, request.POST['email'])
                wks.update_cell(idx, 3, request.POST['password'])
                wks.update_cell(idx, 4, request.POST['school'])
                wks.update_cell(idx, 5, request.POST['member1'])
                wks.update_cell(idx, 6, request.POST['cmnd1'])
                wks.update_cell(idx, 7, request.POST['phone1'])
                wks.update_cell(idx, 8, request.POST['member2'])
                wks.update_cell(idx, 9, request.POST['cmnd2'])
                wks.update_cell(idx, 10, request.POST['phone2'])
                wks.update_cell(idx, 11, request.POST['member3'])
                wks.update_cell(idx, 12, request.POST['cmnd3'])
                wks.update_cell(idx, 13, request.POST['phone3'])

                user = User.objects.create_user(Email, Email, Password)
                Team = tf.cleaned_data.get('team')
                messages.success(request, '✔️ Tài khoản '+Team+' đã đăng ký thành công!')
                return redirect('register:login')
            else:
                ctx = {"tf":tf}
                messages.error(request, '❌ Thông tin không hợp lệ!')
                return render(request, 'register/register.html', ctx, status=422)
                

class login(View):
    def get(self, request):
        ctx = {'lf': loginForm}
        return render(request, 'login/login.html', ctx)
    def post(self, request):
        if request.method == 'POST':
            Username = request.POST['email']
            Password = request.POST['password']

            user = authenticate(request, username=Username, password=Password)

            if user is not None:
                auth_login(request, user)
                return redirect('register:profile')
            else:
                messages.error(request, '🙁 Email hoặc mật khẩu chưa chính xác!')
                return redirect('register:login')

@login_required         
def profile(request):
    data = Team.objects.filter(email=request.user.username)
    args = {'data':data, 'user':request.user}
    return render(request, 'login/profile.html', args)

# class edit(View):
#     def get(self, request):
#         emp = Team.objects.get(email=request.user.username)
#         ef = editForm(initial={'member1':emp.member1, 'cmnd1': emp.cmnd1, 'phone1': emp.phone1, 'member2':emp.member2, 'cmnd2': emp.cmnd2, 'phone2': emp.phone2,'member3':emp.member3, 'cmnd3': emp.cmnd3, 'phone3': emp.phone3,'school':emp.school})
#         return render(request, 'login/edit.html', {'ef':ef})
#     def post(self, request):
#         if request.method == 'POST':
#             ef = editForm(request.POST)
#             if ef.is_valid():
#                 emp = Team.objects.get(email=request.user.username)
#                 emp.member1 = ef.cleaned_data.get('member1')
#                 emp.member2 = ef.cleaned_data.get('member2')
#                 emp.member3 = ef.cleaned_data.get('member3')
#                 emp.cmnd1 = ef.cleaned_data.get('cmnd1')
#                 emp.cmnd2 = ef.cleaned_data.get('cmnd2')
#                 emp.cmnd3 = ef.cleaned_data.get('cmnd3')
#                 emp.phone1 = ef.cleaned_data.get('phone1')
#                 emp.phone2 = ef.cleaned_data.get('phone2')
#                 emp.phone3 = ef.cleaned_data.get('phone3')
#                 emp.school = ef.cleaned_data.get('school')
#                 emp.save()
#                 messages.success(request, '✔️ Update success! ')
#                 return redirect('register:profile')
#             else:
#                 ctx = {"ef":ef}
#                 messages.error(request, '❌ You entered an invalid value!')
#                 return render(request, 'login/edit.html', ctx)
            

def logout(request):
    auth_logout(request)
    return redirect('register:home')





