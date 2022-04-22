from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

TeamRegex = RegexValidator(
    r'(\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b){1,}',
)
NameRegex1 = RegexValidator(
    r'(\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b)\s.{1,}',
)
NumberRegex = RegexValidator(r'^([0-9]{10}|[0-9]{11})$')
CMNDandCCCD = RegexValidator(r'^([0-9]{9}|[0-9]{12})$')

NameRegex = RegexValidator(
    r'^([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,}\s{0,}){2,7}$'
)

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=50, null=False, blank=False)
    logo_path = models.CharField(max_length=100)
    
    def __str__(self):
        return self.school

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[TeamRegex])

    member1 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
    cmnd1 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
    phone1 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
    school1 = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school1', default='')

    member2 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
    cmnd2 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
    phone2 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
    school2 = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school2', default='')

    member3 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
    cmnd3 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
    phone3 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
    school3 = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school3', default='')

    email = models.EmailField(null=False, blank=False, unique=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.team
    