from django.shortcuts import render
from .models import Feature,Latest
# from django.contrib.auth.views import LoginView

# Create your views here.
def index(request):
    a=Feature.objects.all()
    b=Latest.objects.all()
    data={
        'feature':a,
        'ftr':b,
    }
    return render(request,'index.html',data)


def shop(request):
    a=Feature.objects.all()
    b=Latest.objects.all()
    data={
        'feature':a,
        'ftr':b,
    }
    return render(request,'shop.html',data)


# def latest(request):
#     b=Latest.objects.all()
#     data1={
#         'ftr':b
#     }
#     return render(request,'index.html',data1)


# login_view = LoginView.as_view(template_name='hangar/login.html')

# def login(request):
#     return render(request,'login.html')
# # /* for aboutus page */
def aboutUs(request):
    return render(request,'aboutus.html')

