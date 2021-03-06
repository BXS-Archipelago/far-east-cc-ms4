## This document will record bugs and how they were fixed. 

1. Getting to the point where I need to use custom CSS and JS, I am getting an error message in the borwser console :
Failed to load resource: the server responded with a status of 404 ()
net::ERR_ABORTED 404

The Terminal gave this message:
[18/Jul/2021 14:15:39] "GET /static/js/base.js HTTP/1.1" 404 1789
[18/Jul/2021 14:15:42] "GET /static/css/base.css HTTP/1.1" 404 1795 

In not being able to connect with the JS and CSS files, I checked the paths were correct in the project. Checking in Slack, previous students had either not had the correct file paths, or there was a problem with STATIC_URL. However, these were all correct in the FECC project. 

After re-tracing the tutorials, everything was matching the Boutique Ado process with installations and layout. I couldn't find a suitable answer on Stackoverflow as the suggestions were all the same and I couldn't pin down the actual source of the issue. I eventually searched online using "STATIC_URL problems" paired up with the error messages and found the solution.

Time spent on this bug: 1 day.
Solution source: https://learndjango.com/tutorials/django-static-files 
Article Credit: Will Vincent

Solution Snippet: 
# settings.py
"STATIC_URL = '/static/'
This means that static files will be stored in the location http://127.0.0.1:8000/static/ or http://localhost:8000/static/. In order to notify Django of our new top-level static folder, we must add a configuration for STATICFILES_DIRS telling Django to also look within a static folder.

# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),) # new "

Adding the final line fixed the bug after a long search. 

2. As per previous bug, the Media folder was not presenting images properly. 
Found the answer on Slack. The urls.py file needed updating with :
- from django.conf import settings
- from django.conf.urls.static import static

    and adding to the end: 
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

3. Shopping cart is still inserting the Shipping Cost when the items quantity is less than or equal Zero?
    - I wanted a flat delivery rate under ???50 order value and removed the percentage rate from the tutorial instruction. I added a further elif statement for when the cart total is zero, delivery should be zero. 
    - Following more trials in the logic, I discovered the free_delivery_delta statement was also required in both the if and the elif statement. 


4. Shopping Cart product is inserting the product SKU into the Quantity box? 
    - I initially thought the issue was in the back-end code and was chasing this through the views and contexts. In the end it turned out that I had been using value="{{ item.item_id }}" for id="id_qty_{{ item.item_id }}" 
    but obviously (now!)  value="{{ item.quantity }}".  
    - Solution discovered with the patient assistance of Sheryl in Tutor Support. 

5. At stripe implementation, the card-element would not open as an input box. 
- Console returned : "Uncaught IntegrationError: Please call Stripe() with your publishable key. You used an empty string."  
- Solution after a search was a missing # key in the stripe_elements.js ! 

6. Testing checkout with sample order, the delivery charge is incorrect in the Order Admin Checkout.  The Cart Contexts are correct, but I altered the project settings.py with a "standard_delivery_cost = 7" to carry across to checkout>models.py so a cleaner instruction of "self.delivery_cost = settings.STANDARD_DELIVERY_COST" . The previous version was using a percentage of order_total as the delivery cost.

7. Logging in locally (not heroku) gives the error message : 
    django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the NAME value.
Solution : there has been a problem with Gitpod over past 24hrs. Somehow DATABASE_URL has been set by Gitpod. 
- typed in terminal: echo $DATABASE_URL
 The response was: postgresql://gitpod@localhost
- typed in the terminal:  unset DATABASE_URL
This seems to have worked. Advice was kindly gained from the CI slack channel from Igor Basuga. 
The issue might have stemmed from an update done by CI in their template halfway through the project. 

8. In Blog, when a post is updated, it is saving the update as a comment instead. It is also displaying the editor's tags such as <p> </p> around each paragraph. Searching for a misplaced variable or jinja.... I couldn't find the solution alone, and it also took a bit of exploration by the always-helpful guys in tutor-support but the problem and a possible solution was found

- Solution... Thanks to Kevin in CI tutor support for spotting the issue and course mentor Maranatha Ilesanmi for offering the best solution. I had set the post_create.html to perform both creating and updating of posts. I had set the form action to a simple "." but Kevin spotted that there was too much stress on that dot for the action and recommended it be changed to "./update" but also to create a separate post_update.html. 

This was further explored with Maranatha where it was suggested instead to use ".{{ action }}"  and to modify the context in each view. The create view context "action":"" the empty string, and the update view context "action":"/update". 

9. I wanted to use Django send_mail to power the contact form, but many documents such as https://docs.djangoproject.com/en/3.2/topics/email/#send-mail
and stackoverflow advisors were not getting the email format right for me. The message-text wasn't being received, the email address was the message instead, or else the name was the message!  Everything was half-working but the Youtube tutorial from "Scottish Coder" gave me better ideas on how empty dictionaries and empty strings within the view can be used to achieve what was required in the actual incoming mail.  
Credit : https://youtu.be/1DcySa35fXw



