from xml.etree.ElementTree import Comment
from django.contrib import admin

from home.views import viewDoctor
from .models import User
from .models import Cbc
from  .models import Comments
from .models import Doctor,ViewDoctor,ConfirmDoctor

#Register your models here.
admin.site.register(User)
admin.site.register(Cbc)
admin.site.register(Doctor)
admin.site.register(ViewDoctor)
admin.site.register(ConfirmDoctor)
admin.site.register(Comments)
