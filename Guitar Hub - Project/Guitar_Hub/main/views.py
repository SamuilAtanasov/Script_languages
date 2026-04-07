from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

def home_page(request):
    return render(request, "main/home.html")

def types_page(request):
    return render(request, "main/types.html")

def chords_page(request):
    return render(request, "main/chords.html")

def tips_page(request):
    return render(request, "main/tips.html")

def facts_page(request):
    return render(request, "main/facts.html")

def forum_page(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"/accounts/login/?next={request.path}")

        text = request.POST.get("text")

        Message.objects.create(
            username=request.user.username,
            text=text
        )
        return redirect('forum')

    messages = Message.objects.all().order_by('-date')
    return render(request, "main/forum.html", {"messages": messages})
