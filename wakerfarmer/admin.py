from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Mill)
admin.site.register(Farmer)
admin.site.register(Carqueue)
admin.site.register(Ownermill)
