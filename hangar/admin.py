from django.contrib import admin
from .models import Feature,Latest
# Register your models here.
class Ftr(admin.ModelAdmin):
    list_display=['image','type','name','price']

admin.site.register(Feature,Ftr)    

class Ltr(admin.ModelAdmin):
    list_display=['image','type','name','price']

admin.site.register(Latest,Ltr)    