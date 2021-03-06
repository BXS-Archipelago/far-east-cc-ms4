## Far East Car Care Website Record of Build
- Using HTML, CSS, Javascript, Python, Django Framework, deployed on Heroku utilising AWS S3 
### By Brian Smyth

The Build record is to keep a track of the steps followed in the creation of this project. This happens for two reasons :
-1. To support version control and track the progress and/or current status of the project.
-2. For future record to keep a log of the events involved in creating the site. 

I hope it may help others who wish to create a similar website, but it should be noted that it is bullet point summary of events, not a concise notation of every minutae. 
Thank you, 
Brian Smyth
________________
________________
## Chapter 1
- create git repository using code institute template
- create initial mock-up wireframes on Balsamiq as guidelines
- Select color scheme and font choices for project
- Create style.html and colors.css to display color chart and fonts. 
- Begin Readme file
- Initial Commit
- pip3 install Django
- django-admin startproject far_east_cc .
- touch .gitignore to safely hold *.sqlite and *.pyc and __pycache__  
- python3 manage.py runserver to view the server opening on port 8000
- python3 manage.py migrate to run the initial migrations
- python3 manage.py createsuperuser to create an Admin log-in and password.
- Commit work thus far. 

## Chapter 2
- Django Allauth for creating user authentication, registration and account management.
- pip3 install django-allauth
- update settings.py with allauth requirements in INSTALLED_APPS
- under authentication backends, add : SITE_ID = 1 
- add : "import path, include" & path('accounts', include ('allauth'.urls)) to urlpatterns in urls.py 
- runserver
- Navigate to admin (ignoring the first error message)
- Under Sites change name to fecc.example.Com
- Change Display name to FarEast CarCare for social media referencing
- settings.py ... set EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'   (to temporarily log emails to console)
- add email authentication for usernames & emails, mandatory email registration, minimum username length etc.
- login redirect to "/success"
- runserver, navigate to /accounts/login and try log in. Email Verification Message should be present. 
- Return to admin login to enter and select email verified. 
- navigate to /accounts/login and repeat. You will  get 404 but path sill be success in url
- LOGIN_REDIRECT_URL = '/'  (remove success from url)
- pip3 freeze > requirements.txt 
- create templates/ allauth directories
- Commit work thus far. 

## Chapter 3
- cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth 
- with the Allauth templates installed, remove tests and openid folders.
-in the Templates folder, create base.html
- include bootstrap starter template and the following meta in the head :
-  <meta http-equivalent="X_UA-Compatible" content="ie=edge">
- put {% load static %} at the top to load static files.
- Commit work thus far
- Create block/endblock jinja for core css and js in base.html
- Also create blocks for page_header, content, postloadjs
- Create if messages/endif in base.html
- Commit work thus far
- Create HOME app using python3 manage.py startapp home 
- Create templates directory inside home with new index.html file
- add extends 'base.html' and load static
- Test: Create tester h1 to check bootstrap, etc is working. 
- Test Result: Succesful, H1 is displayed.
- In views.py define index view to render index template.
- create a new urls.py in the home app and copy in all from the project urls.py 
- in home urls.py use *urlpatterns = [path('', views.index, name='home') ]*
- in project urls.py include the *path('', include('home.urls'))*
- add home to installed apps in Settings. 
- In Template Dirs setting, add home app and templates directory. 
        os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'templates', 'allauth')
- Commit work thus far. 

## Chapter 4
- create static/css/base.css 
- Move css color palette and fonts to main css file. 
- Delete colors.css and style.html as no longer required
- create templates/home/index.html 
- Begin Sliding nav-bar 
- attach Font Awesome CDN in style links
- Add global site styles to Headings, Paragraphs, Body etc for responsiveness. 
- Commit work thus far. 
- Base.html : Create Header bar to contain site tools such as search, shopping cart, login
- Base.Html : Create Side-Sliding navbar separately for links.  
- Retaining some Bootstrap for now, create Search form on header bar. 
- Font Awesome User icon, create My Account link as bootstrap dropdown
- Use logout, signup, login jinja on base.html to adopt Allauth URLs in the url.py file at project level.
- Create shopping Cart icon with IF Grand Total jinja sequences to check for shopping activity. 
-runserver shows all text and links, but no css yet.
*See bugs.txt #1 for fix.
- fixed CSS and JS bug. 
- updated base.html with less Bootstrap dependencies.
- Commit work thus far


## Chapter 5
- added CSS for index page.
- fixed sliding side Nav bar with JS
- Corrected urls.py to show content of MEDIA folder
- Update base.html
*See bugs.txt #2 for the fix details.
- Uploaded video for Landing page.
- Test Sideslide Navbar
- Test result: Succesful
- Creating JS to display video with On/Off Switch
- Commit Work thus far
- Invoke responsiveness for headers and fonts and buttons on index page.
- Adjust colors away from Bootstrap Default.
- Upload background video
- Wire up On/Off Switch to JS and adjust Z-Index.
- Commit Work thus far

## Chapter 6
- Adjust Burger-Icon for sidebar-toggle on mobile small screen.
- Replace video file with compressed version.
- Test for responsiveness
- Test Result Successful
- Commit Work thus far.
- * Design Contention Point - Drop Down menu for categories doesn't suit.
- Redesigning Drop-down menu for better UX, delete CSS and JS code.
- Commit Work thus far. 
- Add Button for dropdown menu to show product Collection options
- Remove Font-Awesome icon for Account, change to button to match above.
- Create dropdown-menu for product collection. 3 columns.
- Collection dropdown will be full screen width.
- Adjust Bootstrap column sizes for responsiveness in different screens.
- Overwrite bootstrap Element.Style with !important for dropdown-menu transform.
- Commit Work thus far. 
- Update dropdown-menu class with additional ID to Overwrite bootstrap Element. Style with !important for dropdown-menu transform. Otherwise all classes affected!
- Test Navbar and dropdown so far. 
- Test result: successful
- Commit Work thus far.

## Chapter 7
- Add Row to hold "Free Delivery" text area
- Add CSS to provide text colors, style and size.
- Add JS to animate text in rotation
- Test Rotating Text in index.html
- Test result successful but requires modifying for size and responsiveness
- Commit Work thus far. 
- Modify text size and layout for smaller screens
- Modify bars icon size for small screen
- Modify Free-Delivery Banner for size and position.
- Modify Padding on Shopping Cart Icon
- Test page for functionality. 
- Test result: Succesful
- Commit Work thus far.

## Chapter 8
- Copy across product images to media folder
- Create Products App : python3 manage.py startapp products.
- Add 'products' to INSTALLED_APPS in the main settings.py file
- Add Fixtures folder to products app : mkdir products/fixtures
- Add categories.json and products.json to fixtures folder
- Populate 8 categories and 14 products (so far) with json data 
- Commit Work thus far
- Add more items to products.json. 20 items, but more needed progressively.
- Add more images to media folder & shorten file names.
- Commit Work thus far.

## Chapter 9
- Populate products>models.py django product/category relationships
- Perform python3 manage.py makemigrations --dry-run 
- Dry Run fails due to Pillow not being installed (as per tutorial)
- pip3 install pillow
- Migration dry run successful.
- Check models before migrations with python3 manage.py migrate --plan
- All successful. ... so perform python3 manage.py migrate
- Register Product and Category models in admin.py
- Implement fixtures for categories and products using the following
- python3 manage.py loaddata categories
- python3 manage.py loaddata products 
- Test : Run Server and log in to Admin panel  
- Test result: Successful Admin panel shows Products and Categories are populated.
- Commit Work thus far. 

## Chapter 10
- in models.py change to correct plural spelling of categories
- in admin.py, register the ProductAdmin and CategoryAdmin classes
- Order the columns by SKU (note: tuple)
- Commit Work thus far
- Build products views in products>views.py
- Create products>urls.py and import view for path to all_products
- Add url paths to project level urls.py for 'products/' & products.urls
- Create products template directory: mkdir -p products/templates/products
- Create products.html in templates/products folder
- Copy html from home>templates index.html and do runserver
- Test products page
- Test result: Succesful The /products page shows the products 
- Commit Work thus far

## Chapter 11
- Updated index.html, base.html and products.html.
- Adjusted CSS and background colour. 
- Created initial card system for displaying product info.
- Test display for layout
- Test result: Succesful, page looks more structured. 
- Commit Work thus far. 
- Updated links to Store in main menu and button link.
- Add product_detail view to products>views.py
- Create URL in products>urls.py
- Create product_detail.html template
- Update image links in template
- Adjust padding to body container 
- Commit Work thus far

## Chapter 12
- Insert search url to searchbar, action = GET.
- Update products>views.py with search function
- Use : from django.db.models import Q  for django Q keyword arguments.
- Test Search function :  
- Test Result: Succesful - Search function displays with keywords from either Name or Description
- Commit Work thus far
- Insert url links to dropdown categories for Interior & Exterior
- Test filtering for all categories. 
- Test successful - products are displayed accordingly
- Commit Work thus far.
- Add url links to sort by Price, Rating & Category in main dropdown
- In products>views.py provide Sort and Direction functionality if request.GET
- Test sorting by price, by rating & by category. 
- Test successful.
- Commit Work thus far.
- Add jinja for Category display to products.html.
- Commit Work thus far

## Chapter 13
- Product sorting created with Sort-Selector at top of products page
- Sorting objectives created with 10 main criteria for user to select
- Display number of products available at top of products page
- Return text confirming result of search with search-term mentioned
- Commit work thus far
- Update product>view.py to force sortkey to sort by name instead of ID
- Test sorting using products displayed by asc, desc. Test successful
- Test search for number of products in result and search term. Test successful.
- Commit Work thus far 
- Add JQuery to products.html to enable the mechanics of the sort functionality.
- Test Sort function
- Test result: Failed - reveals that sorting by name exposes an error.
- To products>views.py add "from django.db.models.functions import Lower"
- Test all sorting categories individually. 
- Test Result - Successful.
- Commit Work thus far

## Chapter 14
- Add Arrow-Up to top of screen for product page. HTML & CSS
- Create JS for Arrow Up.
- Test Arrow Up.. 
- Test successful. Click returns user to the top of screen
- Modify Arrow Up for small screens
- Commit Work thus far
- Create Cart App : python3 manage.py startapp cart
- Add cart app to project settings.py
- Create folders template>cart and inside these create cart.html
- Create cart>urls.py.  Update view and name.
- Update cart url link in main.html
- Test Cart.html
- Test result: Succesful
- Commit Work thus far

## Chapter 15
- Add Form to product_detail.html below product.description
- Apply csrf_token for cross-site request forgery protection
- create new view add_to_cart in cart>views.py
- Commit Work thus far.
- Create cart>urls.py create URL using item_id & return add_to_cart view. 
- Test by printing Cart with print(request.session['cart']) in cart>views.py
- Test product quantity by both entering the number & add to cart repeats.
- Testing successful, relevant product id and quantity shows in terminal.
- Commit Work thus far
- Create contexts.py, allow users to add items into the cart.
- Create threshold for free delivery if less than specified Total
- Create free delivery delta figure to display how much more needs be spent
- Create the context for all items which will be available across the project
- Test pages, the home page displays the delivery threshold. Test successful.
- Commit Work thus far.

## Chapter 16
- Render items to shopping cart in cart>contexts.py with context processor
- Use get or initialize into empty dictionary.
- iterate through items and tot up total cost and product count
- Test context processor by adding products to the cart. 
- Results show currently as product ID and quantities in the Cart template.
- Test successful.
- Test Grand Total displayed at shopping cart icon.  
- Grand Total if statement in base.html works. Test result successful.
- Commit Work thus far

## Chapter 17
- Create tables and rows to hold Cart info, product info, price, grand total.
- Update shopping cart template. 
- Commit Work thus far
- Add has_sizes to products>models.py in the Product models
- Need to run migrations because of change to Model.
- python3 manage.py shell :Use Shell to add sizes to products
- from products.models import Product 
- accessories = ['accessories']  : Variable to exclude from sizes
- chems = Product.objects.exclude(category__name__in=accessories) -Excludes
- chems.count()  - gives the amount of items ready for sizes
- This for-loop iterates through query set and sets has_sizes to True 
- for item in chems:     item.has_sizes = True    item.save()
-  Product.objects.filter(has_sizes=True).count()
- Add size Selector box to Product details with strings as Options
- Add size info to product info in the shopping cart page
- Commit Work thus far

## Chapter 18
** Change decision ** Removing Product Size features. The product listing is single size only as smaller retail-packaging for the product range.
- remove size selector and options from product_detail page. 
- Make Migration
- Commit Work thus far
- Create products>includes>quantity_input_script.html to host JS for task
- Create JS for increment and decrement controls
- Create limiter for quantity to disallow anything below Zero or above 99
- Create function to iterate through limiter for manual number entry
- Test on page. 
- (Test failed due to using single-quotes instead of back-tick!)
- Fix bug & test again. Test Successful.
- Commit Work thus far.

## Chapter 19
- ** Change Decision. Original landing page had video background.
- Delete video with HTML CSS and JS associated with it for better UXP and less demand on load time. 
- Redesign Nav Bar with Drop Down menus. 
- Redesign Icons for User Account and Shopping Cart
- Commit Work thus far
- Update Index page with photos
- Add style to dropdown menus.
- Update photo sizing in media and link at products.json
- Test index.html
- Test result: Successful but more styling and design required.
- Commit Work thus far

## Chapter 20
- Item 4 in bugs.txt 
- Chasing a bug. The item_id from cart>contexts.py and views.py is putting the product pk number into the quantity box in the Shopping Cart. 
- Bug fixed thanks to Sheryl in Code Institute support,
- Testing bug solution : Test successful after fixing incorrectly placed variable in cart.html at the quantity box.
- Commit Work thus far
- Create Bootstrap Toasts in folder templates>includes>toasts for pages.
- Create toast_error, toast_info, toast_success & toast_warning html pages.
- Create CSS for toasts to appear at top right of screen
-Commit Work thus far
- Chasing a bug. Toasts not appearing; Message in console: Toasts is not a function. This was related to the versions of Jquery and Bootstrap listed in the base.html.  With the correct versions in place, ajax requests now work.
- Test toasts: Test successful
- Commit Work thus far.


## Chapter 21 - Checkout
- Create Checkout App using python3 manage.py startapp checkout
- Create Models class called Order. Fields are for name, address info, etc. 
- Create defs in Models 
- Chasing a bug. Item 3 in bugs.txt
- Checkout link in header always shows deliverys cost. This required an extra elif statement, but after trial and error, I discovered I needed to include the free_delivery_delta statement in both as well. 
- Make migrations and migrate
- Commit Work Thus far
- Add models to the checkout> admin.py 
- Admin requires ability to update order total, delivery cost and grand total
- Create checkout>signals.py to iterate through each time a line is added to an order
- Import post_save and post_delete
- Create defs for update_on_save and update_on_delete
- In checkout>apps.py create def ready(self) so the custom update total model method will be called 
- Commit Work thus far
- Create forms.py for class(OrderForm)
- Add placeholders & classes, remove auto-generated labels and set autofocus on first field
- Commit Work thus far

## Chapter 22 : Checkout Template
- In Checkout>views.py create the URL and the basic template to call the cart contents
- Create urls.py and path for checkout views
- Create template>checkout>checkout.html 
- Use new css file in link within {% block extra_css %}
- Create folders and file static>checkout>checkout.css 
- installation : pip3 install django-crispy-forms
- In project settings.py add crispy_forms to apps
- add CRISPY_TEMPLATE_PACK = "bootstrap4"
- add built-ins under the context processors
- freeze the new installs in requirements.txt 
- Populate the checkout.html with form
- include {% csrf_token %}
- access the form and pipe them with as-crispy_field
- Add the submit button for credit card entry
- As per tutorial, settings.py requires a media context processor for where there are no images.
- Test Checkout.html 
- Test result: Succesful to current progress. 
- Commit Work thus far


## Chapter 23 : Stripe
- Activate stripe account. 
- Add stripe js link on base.html in corejs
- In checkout.html, add postloadjs at bottom with block.super
- add json_script as filter because Django temp variables can't render externally
- In checkout>views add stripe_public_key to context
- Test Checkout page for Stripe, inspecting checkout.html shows two new script tags stripe_public_key and client_secret
- Add stripe CSS to checkout.css for themed styling
- Create stripe_elements.js and obtain public & client keys as .text
- Create js variables and elements to create card element and mount it in the div setting in checkout.html
- Link the stripe_elements.js in checkout.html postloadjs at bottom of page.
- Test checkout.html  
- Test Unsuccessful
- Chasing a bug. Item 5 in bugs.txt
- "Uncaught IntegrationError: Please call Stripe() with your publishable key. You used an empty string." 
- The key is not being recognised but seems to be in the correct places and format. Views context is correct. 
- Solution : found a missing # key in the JS file for '#id_stripe_public_key'
- Test Checkout.html : Test successful.  
- Commit Work thus far

## Chapter 24: Stripe functionality
- Checkout>views.py from cart.contexts import cart_contents which is a dictionary
- create variables for stripe to access cart contents and grand total
- installation of stripe :  pip3 install stripe
- import stripe in checkout>views.py
- in project settings.py, set the stripe currency and public & secret keys
- in terminal, export STRIPE Public and Secret keys.
- Save keys in workspace settings Environment Variables
- Create payment intent in checkout>views.py
- Test print(intent) in views.py
- Test successful, keys are all displayed in terminal
- In checkout>views.py, re-set stripe_public_key and client_secret in context
- Set alert message in case public key has not been set
- Commit Work thus far
- Copy Handle Form Submit data from stripe website to stripe_elements.js
- Disable submit button to avoid multiple card submissions
- Test Checkout page using Stripe fake card number and submit
- Stripe dashboard advises that in the events the payment was received.
- Test result : successful
- Commit Work thus far

## Chapter 25: Stripe payments
- Create POST handling for checkout in views.py
- Create code to retrieve product ID from the cart, iterate through items.
- Create error message in case of eventuality
- Delete order upon completion, returning user to shopping page
- Import Product and OrderLineItem at top.
- Create checkout_success view in checkout>views.py
- Also import get_object_or_404 and Order to accomodate
- Create path for checkout_success in urls.py
- Commit Work thus far
- Create checkout>templates>checkout> checkout_success.html 
- Update checkout>__init__.py by add default config class to check for app
- Test sample order through checkout, stripe events, order admin
- Test result : Unsuccessful - incorrect Delivery charge. 
- Addressed the inconsistent variables in project>settings.py and checkout>models.py for fluid recognition of delivery charge.
- Test sample order through checkout, stripe events, order admin
- Test signals for update on save & delete.
- Test results successful
- Commit Work thus far

## Chapter 26 : Checkout Protocols
- checkout_success.html requires order summary form.
- Summary form requires Order info, details, delivery & billing info.
- checkout.html requires overlay
- Commit Work thus far
- Create webhook_handler.py
- Add functions to recognise that a stripe webhook has been received.
- Commit Work thus far
- Create url webhook_handler in checkout>urls.py, assign path, function, name.
- import webhook 
- Create webhooks.py in checkout folder
- Set webhook secret key and stripe API key paired with settings data
- import settings and httpResponse, StripeWH_handler, required_POST, CSRF_exempt
- In project settings, assign STRIPE_WH_KEY as environment variable
- Test Webhooks are working: Print "Webhook Test" as httpResponse 200
- In Stripe -> developers -> Webhooks -> add endpoint, the project url
- Retrieve Signing Secret, and export stripe webhook secret from terminal
- Test result : test success
- Modify webhook view to use webhook handler, passing request and dictionary event_map
- Test : Change payment failed response in webhook_handler.py.
- Stripe Send Test Webhook, add ????? to payment failed message.
- Test result: Webhook received: ?????payment_intent.payment_succeeded : test successful
- Commit Work thus far

## Chapter 27 : database objects in webhook handler
- In stripe_elements.js, with the card , add billing details object
- Add shipping details object AND billing details object. Trim white space.
- Create metadata as a view to apply whether the user has save-info box ticked
- Create url to access cache_checkout_data view
- Modify stripe_elements.js to accomodate save info, csrf token, etc
- Response must be updated before the confirmed payment intent method can be called so the stripe function will be placed inside the callback function
- Attach a failure function if view sends a 400 bad request response. (See  comments at top of stripe_elements.js)
- Test progress with order using print(intent) within handle_payment_intent_succeeded function.  
- Observed : Country was entered as Ireland, but message returned to say not recognised, it should be IE so that is positive. 
- Test result : Order successfully processed & Terminal displays the Payment Intent information as required ; Test successful
- Commit Work thus far. 

## Chapter 28 - Also securing error orders
- in webhook_handler, add intent, pid, bag, save_info, billing, shipping & grand total to handle_payment_intent_succeeded function.
- Replace any empty strings with none (instead of null)
- Check if order exists -> set to false
- use __iexact but case not sensitive to search for exact match
- return 200 message to stripe if order exists
- Iterate through cart items loading cart from json version in payment intent
- use order.objects.create for the form to be saved with the webhook using payment intent data
- Place within a Try block so if anything is wrong, any order will delete.
- Create the attempt variable as 1 and use While to iterate 5 times, but sleep for 1 second so the WH handler will try find the order 5 times over 5s or break.
- In the order model, create original_cart and stripe_pid so we can allow for recognition of repeat orders through use of unique character fields.
- Migrate new model fields, then add the fields to admin.py
- In Checkout.html, add hidden input to the form containing client_secret.
- Get pid in views.py using split for recognition
- original_cart added to model via dumping to JSON string
- Add Cart and stripe PID to attributes so order can be found and completed using those criteria
- Into webhook_handler.py import Order, OrderLineItem, Product models.
- Into webhook_handler.py also import from python time and json modules. 
- Test: create sample order to verify the Webhook event in Stripe.
- Test failed : Stripe : 400 (bad request) & Terminal: ???Bad Request: /checkout/wh/???
- Solution : The STRIPE_WH_KEY saved into the workspace Environment Variables was incorrect.  Once changed to the right one, everything processes fine. 
- Test result: Successful
- Test : temporarily remove form.submit() from JS in stripe_elements to simulate a page close after payment but before form submissions. 
- Test result: successful. Payment is still received, unhandled webhook received by stripe. 
- Commit Work thus far

## Chapter 29 : User profile App
- Update Country field in address to a dropdown
- pip3 install django-countries
- pip3 freeze > requirements.txt
- Models, need to import CountryField, and modify class field for Country
- Migrate changes
- Update CSS to make Country text grey
- Remove country placeholder from forms.py 
- update if field != country to avoid error
- Commit Work thus far
- python3 manage.py startapp profiles
- Add profiles to installed apps in project settings
- Create new model in profiles>models.py to create a source for order history, addresses, etc
- Create Receiver for each time a user object is saved, it will create either profile or save to profile as an update.
- In checkout>models.py import UserProfile, update class with user_profile
- In profiles>views.py show users profile
- Create urls.py and add the path, import views.
- Include the profiles url in the project urls.py
- create templates folder for profile.html in profiles. 
- create static/profiles/css/profile.css
- Test checkout.html ; logout of site, go to the url
- Test successful, checkout.html is visible. 
- Commit Work thus far

## Chapter 30 : Profile & Templates style
- Update page style for templates>allauth>account pages for uniformity
- Update static base.css 
- Test registration process
- Test result: successful. New Testuser1 profile created.
- Update Nav link in base.html for profile page
- In profile>views.py import profile model & return user profile in the template
- In profile.html template, render {{ profile }} to display user's name
- Commit Work thus far
- Update profile.html to show crispy form for delivery and order history 
- Create static>templates>profiles>js>countryfield.js
- Create JS and CSS to ensure that drop-down country is grey but country list is black
- Test CSS and JS for country
- Test result: success ; list appears as black but the first field, "country" is grey
- Create POST handler for profile view for successful update of profile
- Modify to show update message only when on profile page. Not cart contents.
- Update toast_success to display correctly when on_profile_page 
- Commit Work thus far.

## Chapter 31 : Order History in Profile
- In profile.html, create bootstrap table for order num, date, products, total.
- Iterate through orders to show user's history, display items in unordered list
- give order history a set dimension since list of orders might be lengthy. 
- In profiles>view.py create a view for order_history, import orders from checkout.models
- Create url in profiles>urls.py 
- Commit Work thus far.
- In Checkout>views.py, use checkout function to pre-fill the profile information into the order address.
- Test: Create new order and go to checkout. Confirm if saved Profile address is pre-filling the fields. 
- Test result: Successful. The saved details are already in the checkout.
- Commit Work thus far

## Chapter 32 - Webhook handler and profiles
- In webhook_handler, within handle_payment_intent_succeeded : 
- initiate profile, get username from intent.metadata.username
- Update profile by adding shipping details, only if save_info is ticked
- import UserProfile from profiles.models 
- Test wh handler by temporarily suspending form.submit() in js
- Create order, check that order remains on spinning overlay at checkout
- Test result : Successful ; Order reaches Order history in User Profile . Stripe Posts to the webhook url in the terminal and in the Admin section, the order is listed.
- Commit Work thus far

## Chapter 33 - Confirmation emails
- in Checkout>templates  create confirmation_emails>confirmation_email_subject.txt 
- in Checkout>templates  create confirmation_emails>confirmation_email_body.txt 
- in webhook_handler.py create private method _send_confirmation_email(self, order).
- Imports required for render_to_string, settings, send_mail for functionality
- Call the method to send emails from two potential sources: first before returning form response to stripe, or second after the order was created by webhook_handler.
- Add default Email in Settings.py
- Test email with sample purchase order.
- Test result: successful ;  The order is processed and the confirmation email is observed in the terminal output. 
- Commit Work thus far. 

## Chapter 34 : Product Admin
- Create products>forms.py and import django forms, also Product, Category from .models.
- Create the class ProductForm which extends forms.model form. 
- Use friendly_names for categories but super() will override the init method and allow changes to fields
- Use list comprehension syntax to call friendly_names and associated category id to loop into a list. 
- Set the new class on the fields so they match the rest of the store.
- Commit Work thus far. 
- Product>views.py create add_product view.
- In products>urls.py create new path for add_product, also update product_id path for integer. (Django needs to know difference between product number and a string) 
- In products>templates>products create add_products.html with header title and sub-header.
- Create cripsy form in a form element and give method of POST with url for add_product.
- Form requires a cancel button also a submit button for the form.
- Test form in website
- Test result: successful. 
- Commit Work thus far

## Chapter 35 : product admin
- Create POST handler for add product view
- Ensure previous empty form instantiation is moved into Else block
- Test Add Product page first using price with too many digits.
- Test result: successful. Error message appeared with correct warning
- Test Add product with sku 023, correct dategory, data and an image.
- Test result: successful New product appears in correct format.
- Test Add product without an image
- Test result: Product adds to product list as per expectation, but product will not be added to the shopping cart because success notification requires image with url
- In templates toast_success, create IF statement about whether to render image.
- In cart.html, create IF statement about whether to render image.
- Test add product without image and order this product. 
- Test result: successful
- Add link to the product page in the base.html user header
- Commit Work thus far

## Chapter 36 : Editing/Delete products
- Create edit_product.html with heading and submit heading and buttons
- In products>views.py create a view called edit_product 
- In urls.py create url for edit_product
- Test : edit_product.html is working, but no updates until post handler exists.
- Create POST handler for edit_product
- Attach success and error messages within handler for user notification
- Test page functionality
- Test result: Check Error Message when excess characters are used: Successful
- Test result: Check Success with correct input : Successful
- Commit Work thus far
- In products>urls.py create a path for delete_product
- In products>views.py create a delete view, returning to products list when it performs its function.
- Test :  Add new product, then delete it
- Test result: success - new product is added but observing that new product page layout requires attention. When directing the new product to delete url using its product ID, the new product deletes successfully
- Add active links to products.html and product_detail.html for Update and Delete
- Test : Add new test products to check for both update and delete functionality 
- Test results : New products added and both update and delete options are functioning correctly
- Commit Work thus far

## Chapter 37 : login_required for secure urls
- In products>views.py use :  from django.contrib.auth.decorators import login_required
- Add the @login_required decorator to add_, edit_ and delete_products functions for security
- In profiles>views.py also import login_required and add decorator to user profile
-In products>views.py only superusers can add, edit and delete. Create conditions that anyone not a superuser will not be able to access to add, edit or delete.
- Commit Work thus far

## Chapter 38 : Image input fields
- In products create widgets.py and import ClearableFileInput and gettext_lazy as _   (note: to use _() as an alias for gettext_lazy())
- Create class CustomClearableFileInput  with required values
- In project, create in product>templates>custom_widget_templates>custom_clearable_file_input.html
- Retrieve Django>forms>templates>widgets> clearable_file_input.html and past contents to project
- Modify the widget to achieve desired layout with further styling and margins, including bootstrap classes.
- In product>forms.py, from .widgets import CustomCelarableFileInput 
- Set image to new forms.imagefield so it utilizes the widget
- Test progress : Access a product in edit model
- Test result : successful, but styling issues still apparent. 
- Commit Work thus far
- Create styling for image input in base.css
- Remove label for Image rendered by Crispy Forms using If statement in Add and Edit page templates
- Add Javascript to Add and Edit product templates to listen for change event on new image input
- When it is changed, set the filename in the widget template to the new file name.
- Test: Add new Product with proper details, price and an image. 
- Test result Successful. Image filename is observed before saving. 
- Test: Edit product by changing text and removing image
- Test result: Successful. Update description and default image is observed. 
- Test: Try to add product as a non-admin user
- Test result: successful - Message appears that only admin can access that
- Test: Try to access add or edit urls while not logged in.
- Test result: Successful - redirected to login page
- Commit Work thus far

## Chapter 39 - Heroku setup
- Access heroku.com, create new app : bxs-fecc-ms4
- Add-On Heroku Postgres
- Install at terminal : pip3 install dj_database_url
- Secondly, install : pip3 install psycopg2-binary
- Freeze Requirements.txt
- In project settings.py import dj_database_url 
- Comment out original DATABASES block
- Update databases in settings.py with call to dj_database_url.purchase
- Retrieve database_url config var from heroku settings and attach to parse
- Run python3 manage.py showmigrations  
- Bug : the Operational Error: Fatal appeared but as tutorial suggested, running
unset PGHOSTADDR command in the terminal fixed this. 
- Show Migrations command reveals the list of migrations that are required. 
- Run python3 manage.py migrate
- Run  python3 manage.py loaddata categories
- Run  python3 manage.py loaddata products
- Create superuser and password
- Remove parsed database config in settings.py and restore original DATABASES.
- Commit Work thus far

## Chapter 40 : Deploy to heroku
- in project settings.py use : if 'DATABASE_URL' in os.environ to use as database setting, otherwise use default default.
- As webserver, install :  pip3 install gunicorn
- then : pip3 freeze > requirements.txt
- create new file : Procfile
- In Procfile : web: gunicorn far_east_cc.wsgi:application ; so Heroku can create a web dyno to run unicorn and serve the django app
- At Terminal :  heroku login -i
- At Terminal, disable collecstatic with :
heroku config:set DISABLE_COLLECTSTATIC=1 --app bxs-fecc-ms4 
- In project settings.py add local host and heroku app hostname to ALLOWED_HOSTS
- Commit Work thus far (to deploy)
- After normal git push, initialise heroku git remote if app created in website: heroku git:remote -a bxs-fecc-ms4
- Then : git push heroku main
- Test Heroku App for deployment
- Test result: successful but lack of static files for styling Observed
- In Heroku, connect app to Github and set to automatically deploy whenever a git push occurs
- Use www.https://miniwebtool.com/ to generate a django SECRET key
- Add new key to heroku config variables
- In settings.py, configure the secret key setting to retrieve from environment, using empty string as a default
- Set DEBUG = 'DEVELOPMENT' in os.environ 
- Commit Work thus far 

## Chapter 41 : Amazon Web Services S3
- in AWS s3, create new bucket : bxs-fecc-ms4 
- in bucket settings, enable static website hosting
- Use the provided CORS configuration: 
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
- Edit Bucket Policy for S3 Bucket Policy, Pricipal *, Action : Get object
- Retrieve ARN from bucket policy editor and paste into policy generator 
- Click Add Statement, then Generate Policy
- Copy Policy and pasted into bucket policy editor
- Add /* onto the end of the resource key to allow access to all resources
- Click Save 
- In Access Control Lists ACL allow everyone access to List Objects

## Chapter 42 : Identity Access Management in AWS 
- Access IAM from AWS services dashboard or the history
- First Create Group for the user to reside: manage-fecc-ms4
- then create Policy :  go to the JSON tab, use import managed policy 
- Search for S3FullAccess Policy and import that.
- Open in a separate tab, S3 from the services dropdown. 
- Navigate to bucket policy editor and retrieve ARN 
- Paste ARN into create policy json field replacing the Resource. Use [] here
- Secondly, also include the ARN again but with the /* . The first is the bucket itself, the second is another rule for all files/folders within.
- Click next, (no tags) and next again for Policy naming: bxs-fecc-ms4-policy.
- Give description : "Access to S3 bucket for FECC static files"
- Click Create Policy
- Test Success : In Policies Page, AWS confirms "The policy bxs-fecc-ms4-policy has been created."
- Go to User Groups for "manage-fecc-ms4"
- Under Permissions, click Add Permissions > Attach Policy
- Find the relevant policy (bxs-fecc-ms4-policy) and click Add Permissions
- In Users section, click Add User and name it : fecc-staticfiles-user
- Give Programmatic Access and click next
- Add the Correct user to group and click next to the end
- On the Sucess page, download the CSV file which contains access and secret access keys

## Chapter 42 : connect Django to AWS
- installation : pip3 install boto3
- installation : pip3 install django-storages
- Freeze installations : pip3 freeze > requirements.txt
- In project settings.py, add storages to installed apps
- Also in settings, set an IF statement for USE_AWS in the environ to control the bucket, region, access key and secret key.
- In Heroku config vars, add the csv access key and secret key, also remove disable collecstatic
- In settings.py, set the aws custom domain variable to storage bucket name 
- Create new file: custom_storages.py and import django config settings and S3Boto3Storage 
- Create classes for StaticStorage and MediaStorage to inherit from django storages.
- In settings.py, now set the Static and Media Files for the storage classes just created.
- Set the Static and Media file new location URLs to override the URLS in production
- Now Commit Work thus far and issue a git push to deploy into heroku.
- Monitor Activity in build-log in Heroku.  Initial build FAILED due to typo (
    used django.config instead of django.conf to import settings! )
- Test again with git add, commit & push. Build Finalised Successfully. 
- In AWS S3, the static file is now present.
- In the website, the CSS and JS are functioning. Images are yet to be transferred in. 
- Testing Successful this far. 

## Chapter 43 : Handling Media Files
- In Settings.py add AWS_S3_OBJECT_PARAMETERS in USE_AWS to allow browser to cache static files for extended periods as required
- Commit Work thus far and push into Heroku
- In S3, create a new folder : "media" and upload all images into it
- Test : Login to project page as Admin and verify email address 
- Test result : Initially, Admin refused login so the page login was used to force allauth to create the email
- Test Login to admin: Success. Email address observed and verifiable.
- Add Stripe Keys to the Heroku Config Vars : Public and Secret Keys
- Create new Webhook Endpoint for Herokuapp url
- Add the new Webhook signing secret key to Heroku config vars
- Test: Send test Webhook from Stripe
- Test result: Webhook failed. Reason :  no final trailing / at the endpoint.
- Test result: Successful once the endpoint had the correct format.
- Test: Process dummy order.
- Test result: Successful - Product selected and added to cart, in checkout, the credit card is accepted and the order processed and confirmed. More testing required for new client. 

## Chapter 44 - Emails with Django
- Using GMAIL account, in account settings > accounts & import, use 2-step verification. 
- Create App Password for Django app, using Mail & Other (name it 'Django")
- Retrieve 16-digit password 
- In Heroku config vars EMAIL_HOST_PASS holds the password key
- EMAIL_HOST_USER is set as the email account
- In project settings.py find and cut EMAIL_BACKEND variable
- Use if 'DEVELOPMENT in os.environ statement and add settings for emails for Defaults and port, smtp, host options, etc
- Commit Work thus far and deploy changes to heroku
- Test: Heroku build failed due to typo in settings.py (missing quotation mark)
- Test : Build and deploy successful. 
- Test : Create new user using new email address and details in webstore. 
- Test result: Inconclusive. No confirmation email received into inbox initially. Revision of code shows no errors. Gmail setup for Django seems correct at this time.  Test run with several email addresses but no automatic response received and no error messages either. 
- Test register again
- Test result : successful -  The solution to the email bug is not clear. It may have been a delay with the Gmail account settings as no meaningful changes occurred in the code. After 2 hours, the registration confirmation email was working fine with two successful registrations. 
- More email testing to be done for orders, passwords, etc. 

## Chapter 45 - Refactoring HTML, CSS and JS
- update url link for home in base.html 
- update links for {{ URL_MEDIA }} in base.html images and logo
- update transition times for nav and drop-down menu animations
- Update buttons in Allauth pages to match. 
- Login page, removed home button, added text links.
- Logout page, button updated and heading style added. 
- Password change page, updated button.
- Commit Work thus far
- Update Cart page.
- Update Checkout & Checkout Success 
- Update add_product, edit product, product detail and products pages. 
- Commit work thus far.

## Chapter 46 - Create Ratings and Reviews section
- In products>models.py create model for Review with user, product, date, review, rated, likes
- In the interim, create STAR_RATING from 1 to 5. This will be checked later to possibly use the django star rating app
- In products>forms.py create RateForm for the users input fields.
- In products>views.py create the view  rate_product with product and user
- Import model Review and form RateForm
- Create new template rate.html for user to add the review.
- run migrations due to model change
- Commit Work thus far
- Add form to rate.html 
- Show review output at the bottom of product_detail.html using cards
- Add CSS and styling to product_detail.html and rate.html
- Test user reviews functionality. # Review Input
- Test result : initial testing failed due to incorrect Fields in Forms.py
- Test 2 - failed due to not creating ReviewAdmin class in Admin.py!
- In Admin.py create ReviewAdmin class. 
- Test 3 - success. Review is being saved & observed in admin panel Review  
- Test Review display in product_detail.html
- Test result - failed. Need to add review variable and context to the actual product_detail view. 
- Test 2 - failed. Incorrect {{}} template syntax in product_detail.html. 
- Test result - success after properly fixing the output variables.
- Commit Work thus far.



## Chapter 47 : Review Stars using Django
*************
Not using the steps in Chapter 47 as at this point, I am not sure of the process in the Django documentation for the Star ratings django app. 
Please see Chapter 47b. Due to trial and error, the git commits were delayed with these steps with several deletions. 
*************
## Chapter 47 : Review Stars using Django
- Using https://django-star-ratings.readthedocs.io/en/latest/
- Installation : pip3 install django-star-ratings
- Project settings installed apps : 'star_ratings'
- sync the database by migrating
- python3 manage.py makemigrations --dry-run
- python3 manage.py migrate --plan
- python3 manage.py migrate 
- In products.urls.py add : url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
- In settings.py at context_processors, add 'django.core.context_processors.request',

**********
In chapter 47b, I am adapting the review's numeric rating system to display both as the rating in the review, but also to give average rating from number of reviews in the original product detail card. 
**********
**********
## Chapter 47b : Ratings App
- in Product_detail.html  Within a review in reviews condition, add a card to display the review.
- Create reviews as test users
- Test review in product_detail page.
- Test result - some products not showing due to incorrect jinja calling model. 
- Test result 2 - Success. Reviews are observed under the product details but the page does need CSS styling
- Commit Work thus far
- In products>views.py in product_detail view add variables to call reviews, reviews_count, reviews_avg
- reviews_avg will be calculated by adding the rated review score and dividing by the number of reviews. 
- add reviews, reviews_count and reviews_avg to the context
- In product_detail.html call the reviews_avg and reviews_count to display in the product information. 
- Test : Manually add the number of reviews and check against reviews_count display
- Test result : Successful. 
- Test : Manually sum up the ratings and divide by reviews_count. 
- Test result : In comparison to reviews_avg, the average rating is correct. 
- Modify layout of rate.html and product_detail page to display average review rating and number of reviews. 
- Commit Work thus far. 

## Chapter 48 : Simple Django Blog from Home page
- update home page html and css for images and text
- create blog.html in home>templates folder *(later moved into Posts templates)
- for blog posts, create app : python3 manage.py startapp posts
- In project settings add posts to installed apps
- In Posts>models.py create classes for Author, Category and Posts
-  For the new model attributes, make migrations and migrate
- Create Posts>templates>posts folder for blog.html and posts.html 
- In index.html create blog features code. 
- in Posts>admin.py register the Author, Category and Posts sections
- Test create 3 example blog posts, check and select category, add text, add photo
- Test result: successful for admin panel. 3 posts are observed
- Need index to display featured posts so update model with featured check, so update index view where queryset will filter for featured=True, give context.
- Update the index.html with the relevant statements and jinja templating. 
- Test for the 3 example blog posts in index.html
- Test result successful but images are observed to stack below themselves instead of alternating
- Create conditional statement to determine if images are in first or last item to display on the right. 
- Create conditional statement to determine if images are NOT in first AND NOT last item to display on the left.
- Test for image/text alternation
- Test result successful but noted that further styling and padding is required.
- Commit Work thus far 


## Chapter 49 : Latest Blog posts featured on index.html 
- In home>views.py add variable latest to hold timestamp in reverse display
- In index.html create the section for latest posts and provide jinja templating and conditions for the correct fields.
- Test latest blog postings by creating a new blog entry. 
- Test result : Successful. The three newest of the four are displayed and timestamp is in ascending order
- commit work thus far. 

## Chapter 50 : Marketing app for Email Subscribers
- Create new App :  python3 manage.py startapp marketing
- Add to project settings apps
- In marketing>models.py create class Signup for email and timestamp
- In admin.py create admin site register Signup
- Test : Login in to the admin control panel to find Marketing > Signups
- Test result : Can't open the Signup category due to not migrating! 
- Perform makemigrations and then migrate new model set.
- Test result 2 - accessing Signup but it is empty due to Form having no method set. 
- Test result 3 - Successful. Added method POST to form and now the email address is saved and observed in the admin panel 
- Commit Work thus far

## Chapter 51 - Blog main page
- using blog.html within the posts app, create the bootstrap blog code blocks
- In posts>views.py create the Blog view 
- Test if view.html is working. 
- Test result : failed due to not adding "posts" to project urls setting
- Test result 2: Successful
- In posts>views.py import paginator, emptyPage, pageNotAnInteger 
- Under the blog view, add the paginator sequences, setting to 4 entries per page. 
- Commit Work thus far
- Add code for column on right of blog.html for recent posts. 
- Update blog view for most_recent showing latest 3 objects using negative timestamp
- In models.py add view_count to Post model
- Post model needs to be defined in models.py with get_absolute_url 
- Perform makemigrations and migrate for changes in models.py (using dry-run and plan first to check for any issues)
- Commit Work thus far

## Chapter 51 - Category Count to show occurence of each category per blog
- in posts>views.py create new view get_category_count 
- Import Count from django.db.models
- Pass category_count through the blog view, and call at the context.
- Test : print the category_count and refresh the page
- Test Result : successful - categories information is displayed in terminal, but instead of the categories id, change to catories__title to more accurately display the title and count. 
- Test : Run the admin panel and count the occurence of the categories for the  display in blog page. 
- Test result - successful. The number of times each category is selected in posts matches the dictionary at terminal output. 
- Remove print statement 
- Commit Work thus far
- In blog.html add the jinja templating for cat.categories__title and cat.categories__title__count
- Test : Verify the live display shows the title and count of each category currently being used. 
- Test : Successful. The categories and count are accurately

## Chapter 52 : Search the Blog
- in posts>templates>posts Create a new search_results.html to display results
- In posts>views.py create new View for search
- Search view will use django Q imported from django.db.models
- Use Q __icontains to search in both titles and in the overview
- The search_results.html will iterate through the results displaying each result with <a> tags.
- Test : obtain keywords from titles and overviews to search
- Test result : Successful. Keywords return the query result as links
- Test result : Successful. Where keyword appears repeatedly through the title and body, only one result is returned through the use of .distinct()
- Commit Work thus far

## Chapter 53 : creating and displaying blog content with TinyMCE
* Instructions for TinyMCE at https://pypi.org/project/django-tinymce/ 
- Display blog entries on post.html with bootstrap code
- Use free Tiny MCE editor to render form fields
- Installation : pip install django-tinymce
- In project settings installed apps add tinymce
- In project URLS update with path('tinymce/', include('tinymce.urls')),
- Update models.py with TinyMCE required imports 
- In Models.py update Post model with content=htmlField()
- Perform makemigrations and migrate
- Test: Check Admin panel 
- Test result : Result partially successful. In one of the posts, basic text editor is observed but missing some options such as file bar, insert image, etc
- From docs, adding the TINYMCE_DEFAULT_CONFIG into project settings
- Test result 2 - The more complete editor menu is now displayed. 
- Commit Work thus far

## Chapter 54 : Posts on the blog
- Test TinyMCE text editor on one of the existing posts
- Test Result : Successful - text appears as h3 and bold and italic, etc. 
- Test images uploaded from TinyMCE editor
- Test Result : Successful - however the photos needed to be resized by setting the em img tags in CSS with width 100% height auto. 
- On post.html page, hook up the buttons for previous post and next post : 
- In models.py add previous_post and next_post to Post model
- these need foreignkey 'self', on_delete with related names, etc 
- Perform makemigrations and migrate
- Commit Work thus far
- On post.html add the jinja templates for the title, post, author, etc.
- Test post.html for correct post information
- Test result successful but sidebar is not correct. 
- Create sidebar.html and copy in same sidebar html and code as is in blog.html
- Remove sidebar from blog.html and replace with Include for sidebar
- include sidebar.html with most_recent=most_recent category_cunt=cattegry_count
- In post.html, also remove the sidebar and replace with Include for sidebar
- In posts>view.py the Post view will need the same variables as the blog view for the Include sidebar
- Add category_count and most_recent to post view and context. 
- Test blog list for the sidebar
- Test result: Successful, the sidebar is displaying latest posts in order and the categories used. - Test a post for the sidebar
- Test post page for the sidebar
- Test result: Successful, here also the sidebar is displaying latest posts in order and the categories used. The variables in the view are effective.
- Commit Work thus far

## Chapter 55 - Blog post comments input
- In Posts>models.py create a Comment class for user, timestamp, content, post. 
- In forms create CommentForm class
- This takes the model Comment and uses the content as field only. Import Comment. 
- In posts>views.py import the CommentForm
- Inside the Post view, assign the form to be saved with user and post from the model before saving form.
- Add form to post view context 
- In post.html in the comments form, make method POST and add CSRF token
- The active text area uses class form-control. Update CommentForm to use this class for smooth reproduction. 
- Test the comment input form 
- Test result: Successful but wrong size, no placeholder, etc. 
- Test result 2 :Successful. Added placeholder and id to form CommentForm to better style the input box. 
- Commit Work thus far

## Chapter 56 : Viewing previous comments
- in posts>models.py under the Post model, specify @ property to get comments related to that post ... def get_comments
- In the other class Comment, add related name to post as 'comments'
- Model change : Perform makemigrations and migrate
- In post.html, iterate through post.get_comments and place jinja templates for username, timestamp and content
- Test : go to admin and create a comment. 
- Test result : Succesful - the comment appears under the post, with user name and timestamp showing. 
- Commit Work thus far
- Check if author has a profile pic or generic image will be displayed
- Test: Check if Admin photo is displayed at the comment.
- Test Result: successful after adding the avatar-img class to the images for size. 
- Test : Create a new Comment in the post.html input. 
- Test Result: Successful. The new comment made by admin shows up. 
- In models.py at function get_comments, add order_by('-timestamp) to show newest first. 
- In post.html add  post.comments.count for the number of counts on screen.
- Test:  Add more comments and check for corresponding count. 
- Test Result: Successful - the comment count functions well but have wrapped in brackets and needs further styling. 
- Add a Return Redirect Reverse statement to offer a clear page once the comment has been made and no duplications will occur. 
- Commit Work thus far

## Chapter 57 : CRUD Admin for blog posts
- In post.html add <a> tags for edit and delete
- In posts>models.py create get update url and get delete url functions within Post class
- In urls.py, create the paths still within post for post-create, post-update and post-delete
- In views.py, begin the views for create, update and delete 
- In forms.py, PostForm already exists from earlier 
- In views.py, the create view will use the imported PostForm with form.instance.id and using the context form
- Make a new post_create.html and extend the base.html and load crispy forms
- implement csrf_token and form | crispy
- Test post_create.html that the form is displayed. 
- Test result: Successful - form displays but further bootstrap styling shaped it better
- Due to every field showing in the form, access the PostForm Meta and apply only 'title', 'overview', 'content', 'thumbnail', 'categories', 'featured', 'previous_post', 'next_post'
- Test result 2 : Successful - only the relevant fields are displayed. 
- Commit Work thus far

## Chapter 58 : Creating Posts with TinyMCE text editor functionality
- The create form needs to integrate the PostForm with the TinyMCE editor
- In create_form.html, with TinyMCE Editor the form will be passing text, images and other files so form enctype is specified as "multipart/form-data" 
- Above the form tag add form.media in jinja to allow us to see media in the form
- Test post_create.html for Content editor
- Test result : Successful however the content box is far too expansive for the page. 
- The project settings.py has preset sizes for TinyMCE Default Config. Remove these and the content input will take the size of its parent container. 
- Test TinyMCE content box for responsiveness
- Test result: Successful in removing both height and width but the height default, even though mouse-adjustable, was returned at 300px to offer some balance and initial working space. 
- Before creating a test post, the post needs to have an assigned author. 
- In views.py, from models import author
- In the views.py create new get_author function 
- In the existing post_create view, add the author from the get_author view, and the form must also have PostForm request FILES or none
- Test the post_create.html page with a new sample blog post. 
- Test Successful.  Post was created using different heading, p and span paragraphs, image upload, overview and content. 
- Test 2 Successful - Checked in the blog.html list of posts and new post does display with thumbnail and with overview text correct. 
- Commit Work Thus far 

## Chapter 58 - Superuser blog Admin links
- Create Nav Bar link in Account drop-down as Superuser under Product Manager : "Create Blog"
- In posts.html add links for Edit and Delete. 
- Finish the Edit and Delete views in views.py
- Use 'title' in both create and update to alternate on the post_create page as {{ title }}
- The edit function is very similar to the post_create view but requires the id and the instance as post. 
- The delete function will have the simple but effect format of getting the object, deleting it and returning to the list page. 
- Test the delete function 
- Test result - Successful - example blog posts deleted and redirected to the right page
- Test the update/edit function
- Test result : Failed - The updated text is saving as a comment. More investigation required. 
- Test result : Success - Needed to amend the form action from a simple "." using {{ action }} while modifying the context for the post_update and post_create and post_update views. See bugs.txt
- Commit Work thus far

## Chapter 59 - Counting views and Comments of each blog-post
- In post models.py, create class PostView to keep track or the user and the post using foreignkey. 
- in the Post model, change the view_count to instead exist in a @property function within the model. This will grab all the PostView objects and count them.
- In the views.py, import the PostView model. 
- add PostView to get objects user and post
- Make migrations and migrate
- Commit Work thus far
- Test views count
- Test result: Successful. Views count increases with different logged-in accounts. 
- For Comment count, in models.py the class Comment already exists. Move it to above the Post model. 
- In Post model, create a property def for comment_count(self) and this will count the occurence of Comment. 
- Test comment count
- Test result : Succesful. The number of comments displayed in the comment_count fields are accurate in the index page, the blog page and the post itself. 
- Commit Work thus far

## Chapter 60 - Refactoring the pages.
- Index page CSS update. Modify margins and padding for headings. 
- product_detail.html update background colors for reviews. Box-shadow for image. Rate Now Button padding. Move product title to top of page as header.
- rate.html modify label styles and box-shadow for image. 
- Take Search function out of large drop down, put in Navbar. 

## Chapter 61 - Contact us
- Create contact.html in the home>templates>home folder
- Divide the page into col-8 for the form and col-4 for the address
- In home>urls.py add the path for contact
- In home>views.py add a new view for contact
- View takes Name, Email and Message
- Confirmation of receipt Message returned to user upon submissions
- Test Contact Form functionality 
- Test Result : Successful. Using {{ message_name }} on the page also the display of Success-Message in the top, the form is working well
- Commit Work thus far. 
- In home>views.py from django.core.mail import send_mail
- Use send_mail() within the contact view for the subject, message, sender and my receiving email. 
- Test email functionality
- Test fail : SMTPSenderRefused error message. 
- Commit Work thus far
- Perform heroku migrations and pushes, etc. Changed DEBUG for Development. 
- Test2 email functionality 
- Test Result : Success. But change required as email address of sender not in message. 
- Reworking of Contact view required to add extra dictionaries and empty strings. Credit for the correct view : "Scottish Coder" at https://youtu.be/1DcySa35fXw

## Chapter 62 : About us & FAQ pages
- in Home>templates>home create about.html
- Add to urls.py
- in Views.py create def about(request) to lead the page.
- Copy the contact page html as a template and modify for the About Us text
- Add url to nav bar links
- in Home>templates>home create faq.html
- Add to urls.py
- in Views.py create def faq(request) to lead the page.
- Copy the about page html as a template and modify for the FAQ text
- Add url to nav bar links
- Commit Work thus far
- Attach buttons and text to the FAQ pages. 
- Create JS to toggle the question-text from the button in the FAQ page. 
- Commit Work thus far

## Chapter 63 - Refactoring & Restyling
- products.html  - In small screen there is no way to navigate the products.
- Added 3 columns to show Interior, Exterior Products and Currently Viewing to make the page easier to follow in small screen. 
- Index.html - move free-delivery notification above hero-image
- Change font sizes for headings and paragraph text in mid-hero 
- Padding and margins around blog imagery and category headings. 

- Blog Post page, change previous post and next post into row and 2 cols, add border-radius and shadowing.
- Re-align avatar and author above view & comment count in small screen
- Fix sidebar positioning for categories in posts. 


## Chapter 64 : Email Subscribers 
- Subscription input is on Index.html
- In home>views.py the index view already allows for the subscribers emails to be saved to the admin of Marketing app 
- In marketing> models.py create Signup model for email and date.
- In marketing> models.py create MailMessage model for title and message
- marketing>admin.py requires register for Signup 
- Migrate changes to models.py
- In marketing>forms.py create Signup form for Signup Model and emails
- Test Sign-up form in index.html
- Test Successful : Subscription form works, message is displayed. In the admin panel, the email addresses have been received in several tests. 
- Commit Work thus far. 

## Chapter 65 : Email Marketing
- In marketing>templates>marketing create mail_letter.html 
- Update project URLs for marketing url requirements
- Insert crispy form for passing email messages with submit button
- In marketing>views.py create mail_letter view
- marketing>admin.py requires register for  MailMessage
- In marketing>forms.py create Mailmessage form for emails
- In marketing>models.py create MailMessage model for emails outward.
- In views.py import django send_mail
- Insert block formatted for send_mail function subject, message, from, to mail_list
- for better handling of email addresses as a library, install django-pandas.
- run pip3 freeze > requirements.txt 
- In the mail_letter view, the dataframe df will handle the email fields and convert the mail_list emails into a functioning list. 
- In the event of incorrect emails being submitted, use fail_silently=false to prevent the list from crashing
- Commit Work thus far. 
- Test on deployed site for functionality. 
- Test Result : Successful - Added my 3 email addresses and sent a test email shot to the list. The message was received immediately.  


## End of Record