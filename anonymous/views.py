from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.


def home(request):
    notes = Note.objects.all().order_by("-id").values()
    context = {"notes": notes}
    return render(request, "home.html", context)


def form(request):
    form = NoteForm()
    if request.method == "POST":
        print(request.POST)
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "form.html", context)
