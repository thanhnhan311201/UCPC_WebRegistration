import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from flask import jsonify
import re

def export_2_sheet(request):
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
    
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Max-Age': '3600'
    }

    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_args and 'informations' in request_args:
        informations = request_args['informations']
    elif request_json and 'informations' in request_json:
        informations = request_json['informations']
    else:
        return (jsonify({"message": "Request has no Informations!"}), 404, headers)

    if informations is None:
      return (jsonify({"message": "Informations is empty!"}), 404, headers)

    TeamRegex = re.compile(
        r'(\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b){1,}',
        )
    NumberRegex = re.compile(r'^([0-9]{10}|[0-9]{11})$')
    CMNDandCCCD = re.compile(r'^([0-9]{9}|[0-9]{12})$')
    NameRegex = re.compile(
        r'^([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,}\s{0,}){2,7}$'
        )
    PasswordRegex = re.compile(r'^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$')
    EmailRegex = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE
        )

    if not re.fullmatch(TeamRegex, informations['team']):
        return (jsonify({"message": "Team name is not valid!"}), 404, headers)
    elif not re.fullmatch(NameRegex, informations['member1']) or re.fullmatch(NameRegex, informations['member2']) or re.fullmatch(NameRegex, informations['member3']):
        return (jsonify({"message": "Member name is not valid!"}), 404, headers)
    elif not re.fullmatch(CMNDandCCCD, informations['cmnd1']) or re.fullmatch(CMNDandCCCD, informations['cmnd2']) or re.fullmatch(CMNDandCCCD, informations['cmnd3']):
        return (jsonify({"message": "CMNDis not valid!"}), 404, headers)
    elif not re.fullmatch(NumberRegex, informations['phone1']) or re.fullmatch(NumberRegex, informations['phone2']) or re.fullmatch(NumberRegex, informations['phone3']):
        return (jsonify({"message": "Phone is not valid!"}), 404, headers)
    elif not re.fullmatch(PasswordRegex, informations['password']):
        return (jsonify({"message": "Password is not valid!"}), 404, headers)
    elif not re.fullmatch(EmailRegex, informations['email']):
        return (jsonify({"message": "Email is not valid!"}), 404, headers)

    scope =["https://spreadsheets.google.com/feeds",
          'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account, scope)

    _name = "List_of_teams"
    client = gspread.authorize(creds)

    spreadsheet = client.open(_name)
    wks = spreadsheet.worksheet("demo1")

    idx = f'A{str(len(wks.get_all_values()) + 1)}'
    data = np.array([[informations['team'],
                      informations['email'],
                      informations['password'], 
                      informations['member1'],
                      informations['cmnd1'],
                      informations['phone1'],
                      str(informations['school1']),
                      informations['member2'],
                      informations['cmnd2'],
                      informations['phone2'],
                      str(informations['school2']),
                      informations['member3'],
                      informations['cmnd3'],
                      informations['phone3'],
                      str(informations['school3'])]])
    wks.update(idx, data.tolist())
    
    return (jsonify({"message": "Successful!"}), 200, headers)