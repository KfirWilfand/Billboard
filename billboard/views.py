from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    return HttpResponse("Hello world")


# def login(request):
#     template = loader.get_template("registration/login.html")
#     return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse("main"))
    else:
        form = UserCreationForm()
    return render(request,
                  "registration/register.html", {"form": form})
