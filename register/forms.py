from django import forms
from .models import Team
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

PasswordRegex = RegexValidator(r'^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$')

class teamForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Tên đội',widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos1', 'placeholder': 'Ví dụ: Team01' }))
    
    member1 = forms.CharField(max_length = 30, label = 'Tên thành viên 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn A' }))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'Ví dụ: 0912345678'}))
    school1 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member2 = forms.CharField(max_length = 30, label = 'Tên thành viên 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn B' }))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'Ví dụ: 0912345678'}))
    school2 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member3 = forms.CharField(max_length = 30, label = 'Tên thành viên 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn C' }))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'Ví dụ: 0912345678'}))
    school3 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    email = forms.CharField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'cmnd1', 'phone1', 'school1', 'member2', 'cmnd2', 'phone2', 'school2', 'member3', 'cmnd3', 'phone3', 'school3', 'email']
    password = forms.CharField(max_length = 20, label = 'Mật khẩu', validators=[PasswordRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos5'}))

    def __init__(self, *args, **kwargs):
        super(teamForm, self).__init__(*args, **kwargs)

        self.fields['school1'].label = "Trường"
        self.fields['school2'].label = "Trường"
        self.fields['school3'].label = "Trường"

        # add custom error messages
        self.fields['team'].error_messages.update({
            'invalid': '⚠️ Tên đội không hợp lệ!',
        })
        self.fields['member1'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['cmnd1'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 số)',
        })
        self.fields['phone1'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        })
        self.fields['member2'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['cmnd2'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 số)',
        })
        self.fields['phone2'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 số)',
        })
        self.fields['member3'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['cmnd3'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 số)',
        })
        self.fields['phone3'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 số)',
        })
        self.fields['email'].error_messages.update({
            'invalid': '⚠️ Địa chỉ email không hợp lệ!',
        })
        self.fields['password'].error_messages.update({
            'invalid': '⚠️ Mật khẩu không hợp lệ! (Mật khẩu hợp lệ có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số)',
        })

class loginForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class editForm(forms.ModelForm):
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'example: 0912345678'}))
    school1 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'example: 0912345678'}))
    school2 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'example: 0912345678'}))
    school3 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'cmnd1', 'phone1', 'school1', 'member2', 'cmnd2', 'phone2', 'school2', 'member3', 'cmnd3', 'phone3', 'school3', 'email']
    