from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Queue)
admin.site.register(Map)
admin.site.register(Price)
admin.site.register(Mill)
admin.site.register(Farmer)
admin.site.register(Ownermill)
