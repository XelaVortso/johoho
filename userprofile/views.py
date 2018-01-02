from django.shortcuts import render
from django.views import generic
from .models import Profile

# Create your views here.


def index(request):
    user_list = Profile.objects.all()
    context = {'user_list':user_list}
    return render(request, 'index.html', context)

class detail(generic.DetailView):
    model = Profile
