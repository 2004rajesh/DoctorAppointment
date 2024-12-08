from django.contrib import admin
from .models import Userdata,Doctor,Patient
admin.site.register(Userdata)
admin.site.register(Doctor)
admin.site.register(Patient)

# Register your models here.
#username:admin
#password:12345678