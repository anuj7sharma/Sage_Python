from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.response import Response

from mobile.serializers import UserSerializer
from .models import users


# Create your views here.
def index(request):
    return HttpResponse("Index File")


# Login API
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        # If user send data through query params
        # req_email = request.query_params.get('email')
        # req_password = request.query_params.get('password')
        # If user send data through form fields
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        if req_email != None and req_password != None:
            # Fetch data from DB and check if user exists
            isValidUser = users.objects.filter(email=req_email, password=req_password)
            if isValidUser:
                print(isValidUser.values())
                # serializedDate = UserSerializer(users.objects.filter(email=req_email, password=req_password),
                #                                 many=False)
                response = {
                    'Message': 'success',
                    'Code': '1',
                    'Data': isValidUser.values('uid', 'first_name', 'last_name', 'email', 'profile_pic', 'gender')
                }
            else:
                response = {
                    'Message': 'User not found',
                    'Code': '0',
                }

            return Response(response)
        else:
            response = {
                'Message': 'Please enter email and password',
                'Code': '0'
            }
            return Response(response)


# Register API
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        req_firstname = request.POST.get('first_name')
        req_lastname = request.POST.get('last_name')
        req_email = request.POST.get('email')
        req_gender = request.POST.get('gender')
        req_password = request.POST.get('password')

        print("firstname is %s lastname is %s email is %s gender is %s password is %s" % (
            req_firstname, req_lastname, req_email, req_gender, req_password))

        if req_firstname != None and req_lastname != None and req_email != None and req_gender != None and req_password != None:
            # Push all details to polls_user table using users model
            # check if user with email exists
            isUserExist = users.objects.filter(email=req_email)
            if (isUserExist):
                response = {
                    'Message': 'User already exists with this email',
                    'Code': '0',
                }
                return Response(response)
            else:
                data = users(first_name=req_firstname, last_name=req_lastname, email=req_email, password=req_password,
                             gender=int(float(req_gender)),
                             join_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), is_active=1)
                data.save()
                response = {
                    'Message': 'success',
                    'Code': '1',
                    'Data': users.objects.filter(uid=data.uid).values('uid', 'first_name', 'last_name', 'email',
                                                                      'profile_pic', 'gender')
                }
                return Response(response)
        else:
            print('enter all fields')
            response = {
                'Message': 'Please enter all fields',
                'Code': '0'
            }
            return Response(response)

@api_view(['GET'])
def timeline(request):
    pass