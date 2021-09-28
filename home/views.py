from django.shortcuts import render
from posts.models import Post

from marketing.models import Signup, MailMessage
from marketing.forms import SignMeUp

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
        messages.success(
                    request, 'Your address is now on our list. Nice!')
    context = {
        'object_list': featured,
        'latest': latest,
    }

    return render(request, 'home/index.html', context)

# Contact Email form : Many different docs were failing me with this view for the format the email was received in. Credit to YT Tutorial from "Scottish Coder" for sharpening up the desired result. 
# https://www.youtube.com/watch?v=1DcySa35fXw


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
        
        messages.success(request, 'Your Message has been sent')
        return render(request, 'home/contact.html', {})
    else:    
        return render(request, 'home/contact.html', {})

# ****Return the About page
def about(request):
     return render(request, 'home/about.html', {})

# ****Return the FAQ page
def faq(request):
     return render(request, 'home/faq.html', {})