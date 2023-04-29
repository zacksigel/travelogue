from django.shortcuts import render, redirect
from .models import City, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'travelogue-ga-project'

@login_required
def index(request):
    city = City.objects.all()
    return render(request, "cities/index.html", {"city": city})

@login_required
def detail(request, city_id):
    city = City.objects.get(id=city_id)

    return render(request, "cities/detail.html", {
        "city": city
    })

@login_required
def allusers(request):
    all_users= get_user_model().objects.all()
    for user in all_users:
        print(user.username, user.id)        
    return render(request, "cities/allusers.html", {
        'allusers': all_users
    })

@login_required
def userprofile(request, user_id):
    user_profile= get_user_model().objects.get(id=user_id)
    city = City.objects.filter(user=user_profile)
    return render(request, "cities/user.html", {
        'userprofile': user_profile,
        'city': city
    })

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            error_message ="Invalid signup, try again"
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form,
                                                         "error": error_message})

@login_required
def add_photo(request, city_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, city_id=city_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect("detail", city_id=city_id)

class NewTrip(LoginRequiredMixin, CreateView):
    model = City
    fields = ("city", "country", "description", "date")
    template_name = "cities/new.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateTrip(LoginRequiredMixin, UpdateView):
    model = City
    fields = "__all__"
    template_name = "cities/new.html"

class DeleteTrip(LoginRequiredMixin, DeleteView):
    model = City
    success_url = "/"
    template_name = "cities/confirm_delete.html"