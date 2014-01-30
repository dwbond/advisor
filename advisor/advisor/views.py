from django.shortcuts import render

# page render functions

# homepage
def index(request):
    return render(request, 'index.html', {
    },
    )

# this is where all users not signed in are redirected
def login(request):
    return render(request, 'login.html', {
    },
    )

# search

# SRCT, how to contribute information, how Advisor works
def about(request):
    return render(request, 'about.html', {
    },
    )

# privacy policy
def privacy(request):
    return render(request, 'privacy.html', {
    },
    )
