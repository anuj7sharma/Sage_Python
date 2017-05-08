import urllib
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.response import Response

from mobile.serializers import UserSerializer
from .models import users, InterestsContent, Post, Interests


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


# GET INTERESTS from polls_interestscontent
@api_view(['GET'])
def get_interests(request):
    if request.method == 'GET':
        data = InterestsContent.objects.all()
        response = {
            'Message': 'success',
            'Code': '1',
            'Data': data.values()
        }
        return Response(response)


# Save Interests selected by user to table polls_interests
@api_view(['POST'])
def save_interests(request):
    if request.method == 'POST':
        # Get string of interest ID
        req_uID = request.POST.get('user_id')
        req_interestID = request.POST.get('interest_id')

        if req_uID != None and req_interestID != None:
            # Check if user id is valid or not
            isValidUser = users.objects.filter(uid=req_uID)
            if not isValidUser:
                response = {
                    'Message': "User Id is not valid",
                    'Code': '0',
                }
                return Response(response)

            # check if data is already there then update
            try:
                isAlreadyExist = Interests.objects.get(user_id=req_uID)
                print("user already exists with userID-> " + str(isAlreadyExist.user_id))
                isAlreadyExist.interest_content = req_interestID
                isAlreadyExist.save()
            except  ObjectDoesNotExist:
                print("User does not exist create new record")
                # Save Intersts Id to polls_follow_interest table
                data = Interests(user_id=req_uID, interest_content=req_interestID)
                data.user_id = req_uID
                data.interest_content_id = req_interestID
                data.save()
                print(data)

            response = {
                'Message': 'Your interests saved successfully',
                'Code': '1'
            }
            return Response(response)
        else:
            response = {
                'Message': 'Please enter required parameters',
                'Code': '0'
            }
            return Response(response)


# Add New Posts or Edit Posts
@api_view(['POST'])
def add_post(request):
    if request.method == 'POST':
        # Get string of interest ID
        req_uID = request.POST.get('user_id')
        req_interestID = request.POST.get('interest_id')
        req_desc = request.POST.get('description')
        req_tag = request.POST.get('tag')
        req_image = request.FILES['post_image']

        print(req_image)

        if req_uID != None and req_interestID != None:
            # Check if user id is valid or not
            isValidUser = users.objects.filter(uid=req_uID)
            if not isValidUser:
                response = {
                    'Message': "User Id is not valid",
                    'Code': '0',
                }
                return Response(response)
            # handleUploadedFile(req_image)
            query = Post(user_id=req_uID, interest_id=req_interestID, description=req_desc, tag=req_tag,
                         image=request.FILES['post_image'])
            query.save()

            print('info saved -> ' + str(query.id))
            # postObj = Post.objects.get(id=query.id).image.save('first_img.jpg',request.FILES['post_image'])
            # postObj = Pos/,t.objects.get(id=query.id)
            response = {
                'Message': 'Your post saved successfully',
                'Code': '1'
            }

            # check if data is already there then update
            # try:
            #     isAlreadyExist = Interests.objects.get(user_id=req_uID)
            #     print("user already exists with userID-> " + str(isAlreadyExist.user_id))
            #     isAlreadyExist.interest_content = req_interestID
            #     isAlreadyExist.save()
            # except  ObjectDoesNotExist:
            #     print("User does not exist create new record")
            #     # Save Intersts Id to polls_follow_interest table
            #     data = Interests(user_id=req_uID, interest_content_id=req_interestID)
            #     data.user_id = req_uID
            #     data.interest_content_id = req_interestID
            #     data.save()
            #     print(data)


            return Response(response)
        else:
            response = {
                'Message': 'Please enter required parameters',
                'Code': '0'
            }
            return Response(response)


# Get Posts on TimeLine
@api_view(['POST'])
def get_timeline(request):
    if request.method == 'POST':
        req_uid = request.POST.get('user_id')

        if req_uid != None and users.objects.filter(uid=req_uid):
            # Write logic to send timeline data as in which user is interested
            Data = Post.objects.all()
            domain = request.get_host()
            # print(Post.objects.image)
            # fullurl = urllib.parse.urljoin(domain, Post.objects.filter('image'))
            # print(fullurl)
            # print(Data.values('image'))

            response = {
                'Message': 'Success',
                'Code': '1',
                'Data': Data.values()
            }
            return Response(response)
        else:
            response = {
                'Message': 'Please enter required/valid parameters',
                'Code': '0'
            }
            return Response(response)
