from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm


def Register(request):
    if request.user.is_authenticated:
        return redirect('/api/')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = form.cleaned_data
            user = authenticate(username=form['username'], password=form['password1'])
            login(request, user)
            return redirect('/api/')
        else:
            return render(request, 'main/login_page.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'main/login_page.html', {'form': form})
