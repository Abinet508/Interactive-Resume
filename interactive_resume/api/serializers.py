from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Resume, Exprience, Education


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ["id", "first_name", "last_name", "username"]


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
      model = User
      fields = ['username', 'email', 'password', 'password2']
      extra_kwargs = {
        'password': {'write_only':True},
        'password2': {'write_only':True}
      }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
          raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


# class ChoiceField(serializers.ChoiceField):

#     def to_representation(self, obj):
#         if obj == '' and self.allow_blank:
#             return obj
#         return self._choices[obj]

#     def to_internal_value(self, data):
#         # To support inserts with the value
#         if data == '' and self.allow_blank:
#             return ''

#         for key, val in self._choices.items():
#             if val == data:
#                 return key
#         self.fail('invalid_choice', input=data)

class ResumeSerializer(serializers.ModelSerializer):
    gender = serializers.CharField()
    educations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    expriences = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # educations = educationsSerializer()
    # expriences = expriencesSerializer()
    # gender = ChoiceField(choices=.Resume.gender_choices)
    # language = ChoiceField(choices=.Resume.language_choices)
    class Meta:
      model = Resume
      fields = ['full_name', 'profile_pic', 'resident', 'skills', 'job_des', 'language', 'gender', 'educations', 'expriences']


class ExprienceSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(queryset=Resume.objects.all(),
                                                  many=False)  
    # resume = ResumeSerializer()
    class Meta:
      model = Exprience
      fields = ['job', 'date_started', 'date_ended', 'resume']

class EducationSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(queryset=Resume.objects.all(),
                                                  many=False) 
    # resume = ResumeSerializer
    class Meta:
      model = Education
      fields = ['college', 'date_started', 'date_ended', 'resume']
      

  

