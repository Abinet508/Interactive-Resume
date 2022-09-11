from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer, EducationSerializer, ExprienceSerializer, ResumeSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import check_password
import json
from .models import Resume, Exprience, Education

User = get_user_model()



@api_view(['GET',])
def home(request):
    route = {
        "Register": "/api/register",
        "Login": "api/login",
        "get_resume": "api/resume",
        "get_education": "api/education",
        "get_exprience": "api/exprience",
        "add_resume": "api/add_resume",
        "add_education": "api/add_education",
        "add_exprience": "api/add_exprience"
    }

    return Response(route)


@api_view(['POST',])
def register_user(request):
    serilizer = RegisterSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)
    return Response(serilizer.errors)

@api_view(['POST',])
# @permission_classes([AllowAny,])
def login_user(request):
        data = {}
        reqBody = json.loads(request.body)
        username1 = reqBody['username']
        print(username1)
        password = reqBody['password']
        try:
            user= User.objects.get(username=username1)
            # Account = User.objects.get(username=username1)
        except BaseException as e:
           return Response({"400": f'{str(e)}'})

        
        if user:
            if not check_password(password, user.password):
                return Response({"message": "Incorrect Login credentials"})

            else:
                if user.is_active:
                    login(request, user)
                    request.session['user_id'] = request.user.id
                    data["message"] = "user logged in"
                    data["username"] = user.username

                    Res = {"data": data}

                    return Response(Res)

                else:
                    return Response({"400": f'Account not active'})

        else:
            return Response({"400": f'Account doesnt exist'})



@api_view(['GET'])
def get_resume(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    print(resume)
    serializer = ResumeSerializer(resume, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_education(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    edu = Education.objects.filter(resume=resume)
    # print(print(resume.id))
    serializer = EducationSerializer(edu, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_exprience(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    exp = Exprience.objects.filter(resume=resume)
    print(exp)
    serializer = ExprienceSerializer(exp, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_education(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    serializer = EducationSerializer(data=request.data, many=True)
    if serializer.is_valid():
        # serializer.objects.user = user
        serializer.save(resume=resume)
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def add_exprience(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    serializer = ExprienceSerializer(data=request.data, many=True)
    if serializer.is_valid():
        # serializer.objects.user = user
        serializer.save(resume=resume)
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT'])
def add_resume(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    resume = Resume.objects.get(user=user)
    serializer = ResumeSerializer(instance=resume, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)