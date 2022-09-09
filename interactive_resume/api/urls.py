from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('register', views.register_user, name='register'),
   path('login', views.login_user, name='login'),
   path('resume', views.get_resume, name='resume'),
   path('add_education', views.add_education, name='add_educatio'),
   path('add_exprience', views.add_exprience, name='add_exprience'),
]