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
        name = request.POST['message-name']
        email = request.POST['message-email']
        subject = request.POST['message-subject']
        message = request.POST['message']

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message : {}
        From: {}
        '''.format(data['message'], data['email'])

        # sending email!
        send_mail(
            data['subject'],
            message,
            '',
            ['bxs@tutanota.com']
        )
        
        messages.success(request, 'Message sent')
        return render(request, 'home/contact.html', {})
    else:    
        return render(request, 'home/contact.html', {})
