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

# SkillBridge - UX Design Documentation

## Design Overview

SkillBridge is designed for simplicity and trust, connecting service providers with clients through a clean, professional interface.

## Color Scheme

- **Bootstrap Primary Blue (#0d6efd):** Primary actions and links - conveys trust
- **White Background:** Clean, uncluttered interface
- **Success Green:** Approved services and positive feedback
- **Danger Red:** Delete/cancel actions and warnings
- **Dark Text (#212529):** High contrast for readability

**Accessibility:** All colors meet WCAG 2.1 AA contrast standards (4.5:1 minimum).

## Typography

- **System Font Stack:** Uses native device fonts for fast loading and familiarity
- **Font Sizes:** Clear hierarchy with h1-h6 for headings, 16px body text
- **Readability:** High contrast between text and backgrounds

## Layout Decisions

### Navigation
- **Fixed navbar** with logo, main navigation, and user actions
- **Responsive collapse** to hamburger menu on mobile

### Key Pages

**Homepage**
- Hero section with clear value proposition
- Prominent call-to-action buttons
- Simple three-column feature layout

**Service List**
- Card-based grid layout for easy scanning
- Responsive: 3 columns → 2 → 1 based on screen size
- Status badges for quick recognition (Pending/Approved)

**Dashboard**
- Tabbed interface separating:
  - My Services (what I offer)
  - My Bookings (what I've booked)
  - Client Requests (bookings on my services)
- Reduces clutter by showing relevant content only

**Forms**
- Single-column layout for clear progression
- Labels above fields
- Validation feedback on submission

## User Flow

### Service Provider Journey
Sign Up → Submit Service → Admin Approval → Manage Services → View Client Bookings


### Client Journey
Browse Services → Sign Up/Login → Book Service → Track Bookings in Dashboard


## Key UX Principles

1. **Progressive Disclosure:** Browse without login, authenticate for actions
2. **Clear Feedback:** Success/error messages and confirmation modals
3. **Consistency:** Uniform button styles, card layouts, and spacing
4. **Mobile-First:** Responsive design works on all devices

## Accessibility Features

- Semantic HTML with proper heading hierarchy
- Keyboard navigation support
- ARIA labels on interactive elements
- Form labels associated with inputs
- High color contrast throughout

## Bootstrap Components Used

- Navbar, Cards, Tabs, Modals, Forms, Alerts, Badges, Buttons

## Responsive Breakpoints

- **Mobile:** < 576px (1 column)
- **Tablet:** 576-992px (2 columns)
- **Desktop:** > 992px (3 columns)

---

**Result:** A professional, accessible platform that prioritizes clarity and ease of use for both service providers and clients.



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