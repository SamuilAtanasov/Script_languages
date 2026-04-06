from django.shortcuts import render, redirect
from .models import Message

def home_page(request):
    return render(request, "forum/home.html")

def types_page(request):
    return render(request, "forum/types.html")

def chords_page(request):
    return render(request, "forum/chords.html")

def tips_page(request):
    return render(request, "forum/tips.html")

def facts_page(request):
    return render(request, "forum/facts.html")

def forum_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        text = request.POST.get("text")

        Message.objects.create(
            username = username,
            text = text
        )
        return redirect('forum')
    
    messages = Message.objects.all().order_by('-date')
    return render(request, "forum/forum.html", {"messages": messages})
