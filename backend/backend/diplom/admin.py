from django.contrib import admin
from .models import *

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Dict_Group)
# admin.site.register(Executor)
admin.site.register(Course)
admin.site.register(Lab)
admin.site.register(User_Has_Labs)
admin.site.register(User_Has_Courses)
