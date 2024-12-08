from django.urls import path
from myapp1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('main/',views.main,name='main'),
    path('register/<int:id>',views.register,name='register'),
    path('appoint/',views.appoint,name='appoint'),
    path('success/',views.success,name='success'),    
]