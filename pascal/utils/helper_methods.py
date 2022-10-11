import json
import os

import requests
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from config.settings.base import env


def get_normalize_date(date_obj):
    date_string = date_obj.strftime("%Y-%m-%d %H:%M")
    return date_string


def check_required(request, keys):
    valid = True
    missing_fields = []
    for key in keys:
        if not request.data.get(key) and not request.query_params.get(key):
            missing_fields.append(key)
            valid = False
    error_text = "Please Provide " + ", ".join(missing_fields)
    return valid, error_text


def error_response(message):
    return_obj = {
        "message": message,
    }
    return Response(return_obj, status=HTTP_400_BAD_REQUEST)


def get_user_obj(user_id=None):
    from pascal.users.models import User
    user_obj = User.objects.filter(id=user_id).first()
    if user_obj:
        return True
    else:
        return False


def send_otp_via_sms(number, code):
    url = "https://www.fast2sms.com/dev/bulk"

    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'FastSM',

        # Put your message here!
        'message': f'This is a test message {code}',

        'language': 'english',
        'route': 'p',

        # You can send sms to multiple numbers
        # separated by comma.
        'numbers': f'{number},'
    }

    # create a dictionary
    headers = {
        'authorization': os.getenv("FAST2SMS_API_KEY"),
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST",
                                url,
                                data=my_data,
                                headers=headers)
    print(response.text)
    returned_msg = json.loads(response.text)

    # print to send message
    print(returned_msg['message'])


def send_otp_via_mail(email, code):
    try:
        subject = "YOUR ACCOUNT NEEDS TO BE VERIFIED"
        message = f"""Your OTP is {code}"""
        email_from = env.get("EMAIL_HOST_USER")
        recipient_mail = [email, ]
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_mail)
    except Exception as e:
        print(e)

