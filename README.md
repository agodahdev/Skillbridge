#  SkillBridge

SkillBridge is a platform that connects service providers with users looking for their skills — from tutoring to tech support. Providers can submit their services, and users can browse, book, and manage appointments, all without accessing the admin panel.

##  Project Overview

SkillBridge allows registered users to either:

- Offer a service (e.g. tutoring, design)
- Or request services by browsing, filtering, and booking

Admins approve submitted services before they go public.

## Features

Custom Model: `SkillService` and `BookingRequest`  
Service submission form (CRUD for providers)  
Booking request form (CRUD for users)  
Frontend delete/edit buttons for user records  
Admin approval system  
Filter services by title and category  
Responsive design (mobile, tablet, desktop)  
User registration, login, logout  
Custom 404 page  
Testing with Django + validation tools

## How to Use the Website

### For New Users:
1. Click on **"Sign Up"** to create a new account.
2. Log in using your credentials.
3. As a regular user, you can:
   - Browse approved services.
   - Use filters to find services by category or keyword.
   - View service details and submit a **booking request**.
   - Manage your bookings from the **dashboard**.

### For Providers:
1. After signing up and logging in:
   - Go to **"Submit a Service"** to offer a new service.
   - Fill out the form with title, description, category, rate, and availability.
   - Wait for admin approval (you’ll see it in the dashboard once approved).
   - Edit or delete services directly from the dashboard.
   - View and manage incoming **booking requests**.

### Admin Functionality:
- Admin can log into the Django admin panel.
- Review submitted services and approve or reject them.
- Only **approved** services are shown to public users.

### Device Compatibility:
- The site is responsive and works on mobile phones, tablets, and desktop browsers.

## Technologies Used

- Python  
- Django  
- HTML5  
- CSS3 
- JavaScript (JSHint-tested)  
- Bootstrap  
- SQLite (can be configured)  
- Git & GitHub  


## 📅 Agile Process

- GitHub Projects board used to manage tasks and user stories  
- Clear milestones and labels applied  
- User stories written from user perspective (e.g. "As a provider, I want to...")  
- All commits follow small, meaningful messages.

### 🔧 Manual Testing

We tested the following features manually to ensure they work as expected:

- Registering and logging in/out as a user or provider  
- Submitting services and viewing the provider dashboard  
- Booking a service as a user  
- Canceling bookings from the dashboard  
- Editing and deleting services  
- Admin approval system for submitted services  
- Custom 404 page display  
- Responsive layout on mobile, tablet, and desktop devices  

### Automated Testing

We used Django's `TestCase` to verify key functionality:

- Service submission requires login  
- Dashboard renders correctly  
- Booking form processes correctly  

To run the tests:
python manage.py test 

### Errors and Bugs We Overcame

Throughout the project, we encountered some issues and fixed them. Here are some examples:

-  **Booking form not saving**  
  - The test failed because the booking form required a field named `message`, but the form used `messages`.  
  -  *Fix:* Corrected the field name in the form and test.

- **Django test failure: 0 != 1**  
  - A test was expecting one booking to be saved, but none was.  
  -*Fix:* Ensured the booking form was valid and that the user was logged in.

-  **ImportError for a view not found**  
  - Tried to import `delete_service` from `views.py`, but the function was either missing or renamed.  
  -*Fix:* Added or renamed the view to match the import correctly.

-  **W3C HTML validator showing errors**  
  - Validator showed errors due to Django template syntax (`{% %}`), which is not valid HTML.  
  - *Fix:* Confirmed that the final rendered HTML (using “View Page Source”) is valid and passes W3C checks.

- **Responsive layout not working well on all devices**  
  - Some sections didn’t look right on mobile or tablets.  
  - *Fix:* Added media queries to adjust layout for different screen sizes.

These issues were fixed with careful testing and debugging during development.

🧹 Validation Tools

- **W3C CSS Validator**: No errors found  
- **JSHint**: JavaScript passes with no major issues  
- **W3C HTML Validator**:  
  - Shows template errors due to Django `{% %}` syntax  
  - Rendered HTML (using browser "View Source") is valid and passes W3C checks  


### Deployment:

- This project was deployed using github and Heroku:
- Fork or clone this repo
- Create a new Heroku app
- Set buildingpacks to Python
- Link the Heroku app to Github, searching repo
- Deploy Branch
- live link is here: https://skillbridgeapp-815e04f8d2e3.herokuapp.com/

- Github deployment:
- Go to the Settings tab in your GitHub repo.
- In the Source drop-down menu, select the main branch.
- Save the changes under Branch settings.
- Return to the Code tab, and under Deployments on the right, you will see the live page.

### Credits:

- Code institute Python Essentials Template
- Code institute deployment terminal
- PEP8 Style Guide for Python Code:

Tutorial link: PEP 8 Style Guide: https://peps.python.org/pep-0008/