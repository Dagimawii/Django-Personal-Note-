from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth. decorators import login_required
from . form import RegisterForm , NoteForm
from . models import Personal
from django.shortcuts import get_object_or_404
from django.db.models import Q


def home_view(request):
    return render(request, 'account/home.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username = username , password = password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form' : form})


def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'mainpage'
            return redirect(next_url)
        else:
            error_message = "Invlaid username or password"
    return render(request, 'account/login.html', {'error' : error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('mainpage')


@login_required
def main_page(request):
    query  = request.GET.get('q','')
    form = NoteForm()
    notes = Personal.objects.filter(user = request.user).order_by('-date')

    if query:
        notes = notes.filter(
            Q(title__icontains=query) | 
            Q(text__icontains =query)
        )

    context = {'notes' : notes, 'form' : form, 'query' : query}
    return render(request, 'main/mainpage.html' , context)


def createNote_view(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('mainpage')
    else:
        form = NoteForm()
    return render(request, 'main/home.html',{'form' , form})


def updateNote(request, note_id):
    note = Personal.objects.get(id = note_id, user = request.user)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = NoteForm(instance=note)
    context = {
        'form' : form,
        'editing_note' : note

        }
    return render(request, 'main/mainpage.html', context)

def deleteNote(request, note_id):
    note = Personal.objects.get(id = note_id , user = request.user)
    note.delete()
    return redirect('mainpage')

        







