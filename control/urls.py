from django.urls import path
from . import views
from vege.views import *


# for media directory
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),

    path('car/',views.car,name="car"),
    path('add_car/',views.add_car,name="add_car"),
    path('delete_car/<id>/',views.delete_car,name="delete_car"),
    path('update_car/<id>/',views.update_car,name="update_car"),

    path('student/',views.student,name="student"),
    path('add_student/',views.add_student,name="add_student"),
    path('delete_student/<id>/',views.delete_student,name="delete_student"),
    path('update_student/<id>/',views.update_student,name="update_student"),

    path('login/',login_page,name="login"),
    path('register/',register,name="register"),
    path('logout/',logout_page,name="logout"),
    

    path('receipes/',receipe,name="receipe"),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('receipes/update_receipe/<id>/',update_receipe,name="update_receipe"),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
