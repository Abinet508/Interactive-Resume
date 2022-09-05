from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import check_password
import json

User = get_user_model()


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
                    print(request.user)
                
                    login(request, user)
                    data["message"] = "user logged in"
                    data["username"] = user.username

                    Res = {"data": data}

                    return Response(Res)

                else:
                    return Response({"400": f'Account not active'})

        else:
            return Response({"400": f'Account doesnt exist'})
