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
from django.views.decorators.csrf import csrf_exempt

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np

service_account = {
  "type": "service_account",
  "project_id": "ucpc-348205",
  "private_key_id": "af504fb8a704748449b463fedafed11a0271f7a2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC086LL39q8GiHV\nkEzGa8GHBwrQA/vXGyH0sWT8G5SbiL863oHJ43PO/+Eya1z+russpm65pWadboJo\n2nMdWgkeyMns0B0tg8rMkeyH/gx6OIbYtIarBMMIIVViI34Ckci0YlMsnj1PQd51\nu8NojcKHkwgNOtRAAHvG3d6xvmJDDkO788AngjJp561bU2BME4yYGbLHbaAKtAws\nXW49mTNO5y0cfHZCxyGlvd6JrteTh4AR6owr2aPPqwI2xOLdzz5Og4eHTwiQP1En\nQpXWArMlYOCI/lyJ5KxHkOjXvGVzyqy6pQprCHd16rfGmDH0z8nzLNfZLDe5Fzs2\nqMacfEabAgMBAAECggEAJl7XcZXpYyPDcu7jaNvmsMRMhamimI13WNTZDiCnFYgc\nzNXr/ayOnSFjVnavxI3A7rnoFtO8+7s4ShWwfVPfRTjcoKvM1B7zPQfgeUHk0XH1\nHjTBrbgXxzySR3oxOUhCoAWNj5OKeqkEDEEhgaU1z9vcxDlqUpwHozbfBx/Q5Fjh\npP+iLYGXkXTNP2mi/jtEZ1JwjTk0xEhzr3jvLiMMMe0A9Wb3TsCYU74LYI79VM2g\n9jfEvdRE0IdMlQQvmD41At45g5YiYJ+67/0zefzDYlW7q06PaIjAK+N5GmXoO/DQ\nJ5Gth3YtU+Pid9kag5JGxrRXUiRxAchbNoizeWsNaQKBgQDgrao6HTvgsR6+dx05\nyCSi5t9fEzHVSJQoIll1aODiVkJ706IV07Li7o1LNSzfnlbwpdZcj279F9m0rr8B\nKa7PTm5krqkuxnwMpXccwi5UT0mXozbHmwPmfgjgUzub6uUSnqjVWkTPqrrc4oJu\nmVBikY9oKr7vlUOqGpAsIzLR/QKBgQDOLXNpBivF2TMQOt3/UUBqR7a/EbnP2hrh\net79EQblK69XlYYMsjU3sN1KdoZkR0s9EEpv8gUZ+8V+KFjp0cneFDsmiLTFyYC8\n9/uizFBbY8Q94YUkP6b44EBWg/f6vZ4bfjqPtr69qJHLT78jx7nwrNhdhwvw8rVu\nBPEzQeJydwKBgQC+z35kQHObzZCYnTx62BkVKBHIAtstkagRtapX5iwmzK9FzmQ3\nOUURKRtiJdToTOb1FUJJ9Z6C34CKzGV2rVnCwY9LfnI8QWEUtGnGSLtj6rpLR9e8\nCVB0rdEIAmf7cK/+8jPcjf8mho6QDOZM23PDYm9yPetOOWvvyQNsGLCOWQKBgAH3\nWv9oaKh1XtBLz2ws6TFaR7rgv2XlDZaS5meBbxBmb0Clk2axmGJUlHeuU6/HIkeN\nzTfuFfBef06psddhAczVYo8GhLrSJiEnOEYgLrAAbpGsgemLldsPwG1Syt2gS061\n0HcoZf9HCUToGMmNkQ9jhpi1vf5pQiOvdmFnwnIXAoGADfnkLFvLkigl+4UeNgDG\nePWAn2CCpDBg6MXxe4BUprjZG9kG/HoeoIokBu8diSQ3QmSr/fockBRAe+38z7n9\nNVjWVVXSRZEJKcI9xQB6qWRcrxJ2VGJP5/hb3u9SSieItfMrfCHC/x/THy5lqUIu\nU+QnbxA35Vypxftzvkn/zfg=\n-----END PRIVATE KEY-----\n",
  "client_email": "ucpc-2022@ucpc-348205.iam.gserviceaccount.com",
  "client_id": "115168807477433594795",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ucpc-2022%40ucpc-348205.iam.gserviceaccount.com"
}
scope =["https://spreadsheets.google.com/feeds",
      'https://www.googleapis.com/auth/spreadsheets',
      "https://www.googleapis.com/auth/drive.file",
      "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account, scope)

_name = "List_of_teams"
client = gspread.authorize(creds)
spreadsheet = client.open(_name)
wks = spreadsheet.worksheet("demo1")

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
                tf.save()

                Username = request.POST['team']
                Email = request.POST['email']
                Password = request.POST['password']
                user = User.objects.create_user(Email, Email, Password)
                user.save()

                data = np.array([[request.POST['team'],
                                  request.POST['email'],
                                  request.POST['password'], 
                                  request.POST['member1'],
                                  request.POST['cmnd1'],
                                  request.POST['phone1'],
                                  request.POST['school1'],
                                  request.POST['member2'],
                                  request.POST['cmnd2'],
                                  request.POST['phone2'],
                                  request.POST['school2'],
                                  request.POST['member3'],
                                  request.POST['cmnd3'],
                                  request.POST['phone3'],
                                  request.POST['school3']]])
                try:
                    idx = f'A{str(len(wks.get_all_values()) + 1)}'
                    wks.update(idx, data.tolist())
                except:
                    pass

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





