from django.shortcuts import render
from posts.models import Post

from marketing.models import Signup
from django.contrib import messages

from django.core.mail import send_mail

def index(request):
    """
    A view to return the index page and blog features
    """
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest,
    }

    return render(request, 'home/index.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # sending email!
        send_mail(
            'New message from ' + message_name, 
            message,
            message_email,
            ['bxs@tutanota.com'],
            # Please add your email in quotes after comma to receive a test message. 
        )
        context = {
            'message_name':message_name 
            }
        messages.success(request, 'Message sent')
        return render(request, 'home/contact.html', context )
    else:    
        return render(request, 'home/contact.html', {})
