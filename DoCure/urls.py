"""Auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views

from django.contrib.auth import views as auth_views
urlpatterns = [
        path('admin/', admin.site.urls),
    path('', views.homebefore, name="homebefore"),
    path('home/', views.home, name="home"),
    path('homebefore/', views.homebefore, name="homebefore"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	# path('sign/', views.sign, name="sign"),
	path('logout/',views.logout_view,name='logout'),
    path('about/',views.about,name='about'),
    path('viewDoctor/',views.viewDoctor,name='viewDoctor'),
 	path('FILE/',views.FILE,name='FILE'),
   path('Doctorlogin/', views.Doctorlogin, name="Doctorlogin"),
   path('Doctorhome/', views.Doctorhome, name="Doctorhome"),
path('Doctorlogout_view/',views.Doctorlogout_view,name='Doctorlogout_view'),
  path('dashboard/<int:rid>',views.dashboard,name='dashboard'),
  path('Doctorregister/', views.Doctorregister, name="Doctorregister"),
   path('confirmForm/', views.confirmForm, name="  confirmForm"),
   path('base/', views.Comment, name="base"),
  path('docRequest/<str:doc_id>', views.docRequest, name="docRequest"),
  path('viewPatients/', views.ViewPatients, name="viewPatients"),
  path('pendingReq/<str:user_id>/<int:ar>/', views.pendingReq, name="pendingReq"),
  path('viewmyreports/', views.reports, name="viewmyreports"),
  path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='HtmlFiles/password_reset_done.html'),name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='HtmlFiles/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='HtmlFiles/password_reset_Complete.html'),name='password_reset_complete'),
     path('userProfile/', views.userProfile, name="userProfile"),
  path('editProfile/', views.editProfile, name="editProfile"),
  path('getEditProfile/', views.getEditProfile, name="getEditProfile"),
  path('docViewReports/<int:user_id>/', views.docViewReports, name="docViewReports"),
  path('docDashboard/<int:rid>/', views.docDashboard, name="docDashboard"),
  path('doctorProfile/', views.doctorProfile, name="doctorProfile"),
   path('deditProfile/', views.dEditProfile, name="deditProfile"),
  path('dgetEditProfile/', views.dgetEditProfile, name="dgetEditProfile"),
 path('removePatient/<int:user_id>', views.removePatient, name="removePatient"),
  path('removeDoctor/<int:doc_id>', views.removeDoctor, name="removeDoctor"),
  path('addComment/', views.addComment, name="addComment"),
  path('redocDashboard/', views.redocDashboard, name="redocDashboard"),
  path('deletePatient/<int:rid>', views.deleteReport, name="deleteReport"),
  path('allreports/', views.allreports, name="allreports"),
  path('fileData/', views.fileData, name="fileData"),


]