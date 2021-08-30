from django.shortcuts import render

# Create your views here.

def profile(request):
#    Show the User's Profile

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)