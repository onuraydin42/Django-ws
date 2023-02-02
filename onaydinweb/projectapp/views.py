from django.shortcuts import render
from django.http import HttpResponse
from .models import Professional_second, Feature, Destlast, Featurepricing

def home(request):

    professionals = Professional_second.objects.all()
    features = Feature.objects.all()
    destlasts = Destlast.objects.all()
    return render(request, 'index.html',{'professionals':professionals, 'features':features, 'destlasts':destlasts})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
def signin(request):
    email = request.GET.get('email')
    return render(request, 'signin.html', {'email':email})
def base(request):
    return render(request, 'base.html')
def pricing(request):
    professionals = Professional_second.objects.all()
    featurepricings = Featurepricing.objects.all()
    return render(request, 'pricing.html',{'professionals':professionals, 'featurepricings':featurepricings})

def payment(request):
    return render(request, 'payment.html')

