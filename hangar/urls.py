from django.contrib import admin
from django.urls import path
from . import views
# from .views import login_view
urlpatterns = [
    path('/',admin.site.urls),
    path('index/',views.index,name='index'),
   
    path('shop/',views.shop,name='shop'),
    # path('login/', views.login_view, name='login'),
    path('aboutus/',views.aboutUs,name='aboutus'),
   

]