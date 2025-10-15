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

  ## Design Documentation

 For detailed information about the UX design process, including:
 - Color scheme and typography choices
 - Layout decisions and reasoning
 - User flow documentation
 - Accessibility considerations

 **See: [DESIGN.md](DESIGN.md)**

---

 ## User Stories by Role

 ### Client User Stories
 
 #### User Story #1: Register & Login
 **As a** Client  
 **I want to** register and log in/out  
 **So that I can** securely use the application

 **Acceptance Criteria:**
 - I can create an account using a username and password
 - I can log in and log out securely
 - I see an error if the login fails

 **Tasks:**
 - Create user registration form
 - Set up login/logout views and templates
 - Test and validate flow

 **Status:** ✅ Completed  
 **Implementation:** Django authentication system, signup/login templates, redirect flows

 ---

 #### User Story #2: View Available Services
 **As a** Client  
 **I want to** see a list of approved services  
 **So that I can** choose which one to book

 **Acceptance Criteria:**
 - I can view service title, category, and rate
 - I can see services that are approved by an admin
 - I can search or filter services

 **Tasks:**
 - Show list of services
 - Only show services that are approved (is_approved=True)
 - Create a view template
 - Allow unauthenticated users to view

 **Status:** ✅ Completed  
 **Implementation:** `/services/all/` page with service cards, filtered by is_approved=True

 ---

 #### User Story #3: Book a Service
 **As a** Client  
 **I want to** book a listed service  
 **So that I can** request help from a provider

 **Acceptance Criteria:**
 - I can choose a service and date
 - I can submit a booking with a message
 - The booking is marked as pending
 - The provider is notified

 **Tasks:**
 - Create 'BookingRequest' model
 - Build a booking form and validation
 - Add pending status on submission

 **Status:** ✅ Completed  
 **Implementation:** BookingRequest model, booking form modal, dashboard view for tracking

 ---

 ### Service Provider User Stories 

 #### User Story #4: Post New Service
 **As a** Provider  
 **I want to** create a new service listing  
 **So that** clients can find and book me

 **Acceptance Criteria:**
 - I can input a service name, description, category, and price
 - My service is saved with a "pending approval" status
 - I see a confirmation message after submitting

 **Tasks:**
 - Build SkillService model
 - Use SQLite database (default)
 - Migrate model to database
 - Create service submission form
 - Auto-flag services submission form
 - Restrict form to logged-in users
 - Save service with 'is_approved=False'

 **Status:** ✅ Completed  
 **Implementation:** SkillService model with is_approved field, `/services/submit/` form, @login_required decorator

 ---

 #### User Story #5: Edit/Delete My Service
 **As a** Provider  
 **I want to** edit or delete my services  
 **So that I can** manage my offerings easily

 **Acceptance Criteria:**
 - I can see a list of my services
 - I can edit or delete each one
 - I cannot access other's services

 **Tasks:**
 - Build views for update/delete
 - Add confirmation modal before deleting
 - Restrict access to owner only

 **Status:** ✅ Completed  
 **Implementation:** Edit/Delete buttons in dashboard, confirmation modal, owner validation in views

 ---

 #### User Story #6: View My Bookings
 **As a** Provider  
 **I want to** view client booking requests  
 **So that I can** manage my schedule and respond

 **Acceptance Criteria:**
 - I can view a list of pending, accepted, or rejected bookings
 - I can change the status of each request
 - I see client message and details

 **Tasks:**
 - Build booking dashboard for providers
 - Add status update actions
 - Filter bookings by provider

 **Status:** ✅ Completed  
 **Implementation:** Dashboard "Client Requests" tab showing bookings on provider's services

 ---

 ### Admin User Stories

 #### User Story #7: Approve or Reject Services
 **As an** Admin  
 **I want to** approve or reject service listings  
 **So that** only quality services are available to clients

 **Acceptance Criteria:**
 - I see a list of unapproved services
 - I can approve or reject them
 - Approved services appear to the public

 **Tasks:**
 - Add admin-only dashboard
 - Build approve/reject buttons 
 - Update service status on action

 **Status:** ✅ Completed  
 **Implementation:** Django admin panel with SkillService management, is_approved toggle

---

 ### Developer User Stories

 #### User Story #8: Frontend CRUD (No Admin Panel)
 **As a** user  
 **I want to** manage all my data from UI  
 **So that I don't** have to use Django admin panel

 **Acceptance Criteria:**
 - I can create, read, update, and delete services/bookings
 - All operations happen from the frontend
 - Admin panel is hidden from regular users

 **Tasks:**
 - Build CRUD views and templates
 - Add delete confirmation modals
 - Enforce role-based access control

 **Status:** ✅ Completed  
 **Implementation:** Complete CRUD functionality via web interface, confirmation modals, permission checks

 ---

 #### User Story #9: Production-Ready Setup
 **As a** Developer  
 **I want to** ensure the application is secure and production-ready  
 **So that** it can be deployed safely

 **Acceptance Criteria:**
 - DEBUG = False in production settings
 - GitHub project is public
 - Testing write up is included
 - Secure user input validation is in place

 **Tasks:**
 - Update settings for production
 - Write testing documentation
 - Run tests and validate inputs

 **Status:** ✅ Completed  
 **Implementation:** Environment variables, DEBUG=False on Heroku, security settings, form validation

 #### User Story #10: Setup Project Infrastructure
 **As a** Developer  
 **I want to** set up the Django project and environment correctly  
 **So that** the foundation is ready for future development

 **Acceptance Criteria:**
 - A Django project is initialized and running
 - The main app (services) is created and registered
 - Server runs successfully on localhost
 - Virtual environment is activated and Django is installed

 **Tasks:**
 - Create virtual environment and install Django
 - Start Django project and services app
 - Add 'services' app to INSTALLED_APPS
 - Run initial makemigrations and migrate

 **Status:** ✅ Completed  
 **Implementation:** Complete Django project structure with skillbridge_project and services/accounts apps

 ---

 ## Summary

 ### Total User Stories: 10
 - **Client Stories:** 3
 - **Provider Stories:** 3
 - **Admin Stories:** 1
 - **Developer Stories:** 3

 ### All Stories Status: ✅ Complete

 All user stories were tracked in GitHub Issues and have been successfully implemented and closed. The project demonstrates full CRUD functionality, authentication, authorization, and production deployment.

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


  ## Agile Process

  - GitHub Projects board used to manage tasks and user stories  
  - Clear milestones and labels applied  
  - User stories written from user perspective (e.g. "As a provider, I want to...")  
  - All commits follow small, meaningful messages.

  ### Manual Testing

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

 ## Validation Tools

  - **W3C CSS Validator**: No errors found  
  - **JSHint**: JavaScript passes with no major issues  
  - **W3C HTML Validator**:  
    - Shows template errors due to Django `{% %}` syntax  
    - Rendered HTML (using browser "View Source") is valid and passes W3C checks  

  
 ## Security & Configuration

 ### Environment Variables

 This project uses environment variables to keep sensitive information secure. All secrets are stored outside the codebase.

 **Required environment variables:**
 - `SECRET_KEY` - Django secret key for cryptographic signing
 - `DEBUG` - Debug mode (True for development, False for production)
 - `ALLOWED_HOSTS` - Comma-separated list of allowed host/domain names

 ### Local Development Setup

 1. Create a `.env` file in the project root:
 SECRET_KEY=your-secret-key-here
 DEBUG=True
 ALLOWED_HOSTS=localhost,127.0.0.1


 2. Never commit the `.env` file to Git (it's protected by `.gitignore`)

 ### Production Deployment (Heroku)

 Environment variables are set using Heroku config vars:
 heroku config:set SECRET_KEY='your-secret-key'
 heroku config:set DEBUG=False
 heroku config:set ALLOWED_HOSTS='your-app.herokuapp.com'


 ### Security Features

 - **Environment-based configuration:** Secrets are never hardcoded in source code
 - **DEBUG mode disabled in production:** Prevents sensitive information leakage
 - **CSRF protection:** All forms use Django's CSRF tokens
 - **Authentication required:** Service submission and bookings require login
 - **User permissions:** Users can only edit/delete their own content
 - **Admin approval:** Services require admin approval before going public


  ### Deployment:

  - This project was deployed using github and Heroku:
  - Fork or clone this repo
  - Create a new Heroku app
  - Set buildingpacks to Python
  - Link the Heroku app to Github, searching repo
  - Deploy Branch
  - live link is here: https://skillbridge-ba237edbd42e.herokuapp.com/

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