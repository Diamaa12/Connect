from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session

from ConApp.models import MyUser


# Create your views here.
class UserPersonnaliser(UserCreationForm):
    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields
def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mail = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'app.html', {'error':'Les mot de passe ne correspond pas'})
        MyUser.objects.create_user(username=username, email=mail, password=password1)
        user = f"Bienvenu {username}, vous venez de finaliser votre compte."
        return render(request, 'project.html', {'user':user})
    return render(request, 'app.html', {'user':'Inscription efferuer avec succés.'})


def connection(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username, password=password1)
        if user is not None:
            request.session['username'] = username
            print(request.session['username'])
            perso = f"Bienvenu {user}, vous êtes connecté sur votre space Admin."
            return render(request, 'project.html', {'perso':perso})

        else:
            error = f"Userneme ou mot de passe incorrect! "
            return render(request, 'connection.html', {'error':error})
    return render(request, 'connection.html')



def myproject(request):
        return render(request, 'project.html')