from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('home/', views.home, name="home"),
	path('logout/',views.logout_view,name='logout'),
 	path('about/',views.about,name='about'),
 	path('FILE/',views.FILE,name='FILE'),
  path('dashboard/',views.dashboard,name='dashboard'),
  path('viewDoctor/',views.viewDoctor,name='viewDoctor'),
  path('Doctorhome/',views.Doctorhome,name='Doctorhome'),

  path('homebefore/', views.homebefore, name="homebefore"),
  path('Doctorregister/', views.Doctorregister, name="Doctorregister"),
  path('Doctorlogout_view/',views.Doctorlogout_view,name='Doctorlogout_view'),
  path('Doctorlogin/', views.Doctorlogin, name="Doctorlogin"),
  path('confirmForm/', views.confirmForm, name="confirmForm"),
   


	
    ]
