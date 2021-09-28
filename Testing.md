# Project Testing 

#### Testing was completed at three points in the project. Throughout the creation of the website, each step was documented and every stage was tested and noted for progress or potential bugs. This amounted to over 62 chapters in the build-record.md document. 

#### Secondly, testing was documented according to the user stories using the format "As a User" or "As an Admin" , "I want to.." , "So that I can..." with test results and observations. Please see the two images below for these: 

![story](media/project_media/user_story1.jpg)

![story](media/project_media/user_story2.jpg)

During the build, there were some changes made for better site performance or simply because some directions were not working out. For example, I initially wanted the landing page to have a video background with JS play and pause button. However, even though it was very appealing it was a little too demanding for the site. Also, in spite of following directions for the django-star-rating app, it would not work out for me. And this seemed to be a common point among peers in Stack Overflow. With the very limited documentation and support for the module, I deferred to using a simple numeric rating system for the products instead. 

#### The final testing for the site is the pre-submission, fine-toothed comb manual testing of functionality and features. 


# Final Test 

#### Navigation Links : 

- Top Navigation Bar 
    - Home 
    - Blog
    - Store
    - Help
        - FAQ
        - About
        - Contact
    - Account
        - Login
        - Register
        - Product Manager
        - Create Blog
        - My Profile
        - Logout
    - Shopping Cart 

#### Links test result : Successful - All links redirect to the correct page. 

- Sliding Side-Navigation Bar
    - Burger-Bars Actuator 
    - Home
    - Store
    - Blog
    - About
    - FAQ
    - Contact
    - X to close 

#### Links test result : Successful - Sidebar links redirect to the correct page and buttons perform as desired.

- Top Search bar in navigation 

#### Search function test : Successful

- Sidebar Search 

#### Search function test : Successful

- Test Landing page Buttons - Visit Store and Visit Blog 
    - Test Successful

- Blog Features links 
    - Test Successful : all three links work

- Test Feature blog data :
    - Timestamp, Number of comments : Test successful

- Mid-page Hero link to All Products in Store
    - Test Successful

- Landing page latest Blogs links 
    - Links repaired and now work successfully

- Gallery photos open in new page

#### Testing Admin pages from addresses while not logged in. 
- Test Add Products in Product Manager
    - Test result successful

- Test Create Blog 
    - Test Failed - Needed to add @login_required decorators to view. 
    - Test 2 Successful
- Test Create Email 
    - Test Failed - Needed to add @login_required decorators to view. 
    - Test 2 Successful 

- Test Access Profile 
    - Test Successful, redirected to login instead

- Test Access Control Panel
    - Test Successful, redirect to django login

- 
-