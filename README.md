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

 ## User Stories

 This project was developed using Agile methodology with user stories for clients, service providers, and admins.

 **See: [USER_STORIES.md](USER_STORIES.md)** for complete user story documentation including:
 - Acceptance criteria for each story
 - Implementation details
- GitHub Issue tracking

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



### Model Relationships

**User → SkillService (One-to-Many)**
- One user (provider) can create multiple services
- Field: `SkillService.provider` (ForeignKey to User)
- Delete behavior: CASCADE (if user deleted, their services are deleted)

**User → BookingRequest (One-to-Many)**
- One user (client) can make multiple booking requests
- Field: `BookingRequest.client` (ForeignKey to User)
- Delete behavior: CASCADE (if user deleted, their bookings are deleted)

**SkillService → BookingRequest (One-to-Many)**
- One service can have multiple booking requests
- Field: `BookingRequest.service` (ForeignKey to SkillService)
- Delete behavior: CASCADE (if service deleted, bookings are deleted)

### Model Details

#### SkillService Model
**Purpose:** Stores service offerings from providers

| Field | Type | Description |
|-------|------|-------------|
| `id` | Primary Key | Auto-generated unique identifier |
| `title` | CharField(100) | Service name/title |
| `description` | TextField | Detailed service description |
| `category` | CharField(50) | Service category (choices from predefined list) |
| `rate_per_hour` | DecimalField(6,2) | Price per hour |
| `provider` | ForeignKey(User) | User who created the service |
| `is_approved` | BooleanField | Admin approval status (default: False) |
| `created_at` | DateTimeField | Timestamp of creation (auto_now_add) |

**Business Rules:**
- Services are hidden from public until `is_approved=True`
- Only the provider can edit/delete their services
- Admin can approve/reject via Django admin panel

---

#### BookingRequest Model
**Purpose:** Stores client booking requests for services

| Field | Type | Description |
|-------|------|-------------|
| `id` | Primary Key | Auto-generated unique identifier |
| `service` | ForeignKey(SkillService) | The service being booked |
| `client` | ForeignKey(User) | User making the booking |
| `requested_date` | DateField | Requested service date |
| `messages` | TextField | Message/details from client |
| `status` | CharField(10) | Booking status (default: 'Pending') |
| `created_at` | DateTimeField | Timestamp of booking creation (auto_now_add) |

**Business Rules:**
- Clients must be authenticated to create bookings
- Status defaults to "Pending"
- Both client and provider can cancel bookings
- Bookings appear in provider's dashboard

---

### Category Choices
Services can be categorized into:
- **Tutoring:** Educational services
- **Tech Help:** Technical assistance and IT support
- **Sewing:** Clothing alterations and repairs
- **Gardening:** Garden maintenance and landscaping
- **Other:** Any other service type

---

### Status Choices
Booking requests can have these statuses:
- **pending:** Awaiting provider response (default)
- **accepted:** Provider has accepted the booking
- **rejected:** Provider has declined the booking

---

### Data Integrity
- All foreign keys use `on_delete=CASCADE` to maintain referential integrity
- User deletion cascades to their services and bookings
- Service deletion cascades to associated bookings
- Database constraints ensure required fields are populated
- `auto_now_add=True` automatically sets timestamps on creation


  ## Agile Process

  - GitHub Projects board used to manage tasks and user stories  
  - Clear milestones and labels applied  
  - User stories written from user perspective (e.g. "As a provider, I want to...")  
  - All commits follow small, meaningful messages.

 # SkillBridge - Testing Documentation

## Overview

This document covers all the testing we did on SkillBridge to make sure everything works properly. We tested manually, validated our code, and fixed bugs along the way.

---

## Manual Testing

We tested the following features manually to ensure they work as expected:

### Authentication
- **Registration:** Created new accounts with username and password - worked correctly
- **Login:** Logged in with valid credentials - successfully logged in and navbar updated
- **Invalid Login:** Tried logging in with wrong password - got error message as expected
- **Logout:** Clicked logout button - logged out successfully
- **Unauthorized Access:** Tried accessing /services/submit/ without logging in - correctly redirected to login page

### Service Management
- **Submitting Services:** Logged in as a provider and submitted a new service - service created with "pending" status
- **Viewing Services:** Browsed /services/all/ page - only approved services showed up (unapproved ones stayed hidden)
- **Editing Services:** Went to dashboard and edited my own service - changes saved successfully
- **Deleting Services:** Used delete button with confirmation modal - service removed from database
- **Preventing Unauthorized Edits:** Tried to edit someone else's service by changing the URL - got error message and redirected

### Booking System
- **Booking a Service:** Logged in as a client and booked a service with a date - booking created and showed in dashboard
- **Viewing Bookings:** Checked "My Bookings" tab - all my bookings listed
- **Provider View:** Logged in as provider and checked "Client Requests" - saw bookings on my services
- **Canceling Bookings:** Used cancel button (both as client and provider) - booking deleted successfully
- **Modal Confirmation:** Clicked delete/cancel but then clicked "Cancel" in modal - action was cancelled, nothing deleted

### Admin Features
- **Admin Approval:** Logged into Django admin panel and approved a service - it appeared publicly on /services/all/

### Responsive Design
- **Desktop (1920x1080):** All pages display correctly with 3-column card layout
- **Laptop (1366x768):** Everything works, cards adjust properly
- **Tablet (768px):** Cards show in 2 columns, navbar collapses to hamburger menu
- **Mobile (375px):** Single column layout, all features accessible, forms stack vertically

All manual tests passed successfully!

To run the tests:
```bash
python manage.py test
```

All automated tests pass.

---

## Code Validation

### HTML Validation
We used the W3C Markup Validation Service to check our HTML.

**Important Note:** The validator shows errors when checking Django template files directly because of template syntax like `{% csrf_token %}` and `{{ variable }}`. These aren't actual errors - they're just Django template code. We validated by viewing the rendered HTML source (right-click → View Page Source) instead.

**Pages Validated:**
- Homepage - No errors
- Service List - No errors
- Submit Service Form - No errors
- Dashboard - No errors
- Login/Signup Pages - No errors

### CSS Validation
Used W3C CSS Validation Service (Jigsaw) on our custom stylesheet.

**Result:** No errors found in static/css/style.css

### JavaScript Validation
Checked our JavaScript with JSHint.

**Result:** No errors in dashboard modal script (used ES6 syntax)

### Python Code
Checked Python code follows PEP8 style guide.

**Files Checked:**
- views.py - Clean
- models.py - Clean
- forms.py - Clean
- urls.py - Clean

All code is properly formatted and readable.

---

## Browser Testing

We tested the site on different browsers to make sure it works everywhere:

- **Chrome (latest version):** Everything works perfectly
- **Firefox (latest version):** All features functional
- **Safari (latest version):** Works well on Mac
- **Edge (latest version):** No issues found

The site works consistently across all major browsers.

---

## Bugs We Found and Fixed

Throughout the project, we encountered some issues and fixed them. Here are the main ones:

### Fixed Issues

**Bug 1: Booking form not saving**
- **Problem:** Form submission wasn't creating bookings
- **Cause:** Field mismatch - model used `messages` but form expected `message`
- **Fix:** Updated field name to match between model and form
- **Status:** ✅ Fixed

**Bug 2: Django test failure (0 != 1)**
- **Problem:** Test expected one booking but found zero
- **Cause:** Form validation failing silently
- **Fix:** Made sure all required fields were provided in test and user was logged in
- **Status:** ✅ Fixed

**Bug 3: ImportError for view not found**
- **Problem:** Import statement looking for `delete_service` view that didn't exist
- **Cause:** View was named differently or missing
- **Fix:** Created the view function with correct name
- **Status:** ✅ Fixed

**Bug 4: W3C HTML validator showing template errors**
- **Problem:** Validator flagged Django template syntax as errors
- **Cause:** Validator doesn't understand Django templates (`{% %}` and `{{ }}`)
- **Fix:** Validated using rendered HTML (View Page Source) instead of template files
- **Status:** ✅ Resolved (not actually a bug, just how validators work)

**Bug 5: Responsive layout issues**
- **Problem:** Some sections didn't look right on mobile devices
- **Cause:** Missing responsive styles
- **Fix:** Added media queries and used Bootstrap classes properly
- **Status:** ✅ Fixed

**Bug 6: SECRET_KEY exposed in code**
- **Problem:** Secret key was hardcoded in settings.py and visible on GitHub
- **Cause:** Didn't use environment variables initially
- **Fix:** Moved to .env file using python-decouple library
- **Status:** ✅ Fixed (Critical security fix)

**Bug 7: Cancel/Delete buttons not working**
- **Problem:** Clicking cancel or delete buttons did nothing
- **Cause:** Missing modal HTML and JavaScript for form submission
- **Fix:** Added complete modal with JavaScript to handle form submission
- **Status:** ✅ Fixed

**Bug 8: Heroku deployment crashes**
- **Problem:** App wouldn't start on Heroku with module errors
- **Cause:** Incorrect import paths (missing `skillbridge.` prefix)
- **Fix:** Updated all imports and file paths to match nested structure
- **Status:** ✅ Fixed

---

## Known Issues

### Issue 1: Past Date Bookings
**Problem:** Users can select dates in the past when booking services  
**Impact:** Low - providers can simply decline these bookings  
**Why Not Fixed:** Would require custom date validation in the form  
**Future Fix:** Add JavaScript or Django form validation to block past dates

### Issue 2: Admin Panel Styling on Heroku
**Problem:** Admin panel lacks CSS styling on live site  
**Impact:** Low - admin panel still works, just looks plain  
**Why Not Fixed:** Would require WhiteNoise configuration (optional for this project)  
**Future Fix:** Configure WhiteNoise properly for static file serving

These issues are minor and don't affect the main functionality of the site for regular users.

---

## Testing User Stories

We tested each user story to make sure it was implemented correctly:

**Client Stories:**
- ✅ Can register and login
- ✅ Can view list of approved services
- ✅ Can book services with date selection

**Provider Stories:**
- ✅ Can submit new services (go to pending status)
- ✅ Can edit and delete own services
- ✅ Can view client booking requests

**Admin Stories:**
- ✅ Can approve/reject services via admin panel

**Developer Stories:**
- ✅ Full CRUD functionality works from website (not just admin panel)
- ✅ Project deployed securely to Heroku

All user stories pass their acceptance criteria.

---

## Performance Notes

- Pages load quickly (under 2 seconds on average)
- Used Bootstrap CDN for fast loading
- Minimal custom CSS keeps site fast
- Database queries are efficient (Django ORM handles this)

---

## Accessibility

We made sure the site is accessible:
- All buttons and links work with keyboard navigation
- Forms have proper labels for screen readers
- Colors have good contrast (easy to read)
- Used semantic HTML (proper heading structure)

---

## Conclusion

SkillBridge has been thoroughly tested and all major features work correctly. We fixed all critical bugs during development. The two minor known issues don't impact normal use of the site. All user stories pass, code is validated, and the site is responsive across all devices.

---

## Automated Testing

We used Django's `TestCase` to verify key functionality:

- **Service submission requires login** - Test passes, unauthenticated users redirected
- **Dashboard renders correctly** - Test passes, returns 200 status
- **Booking form processes correctly** - Test passes, booking saved to database

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


 ## 🔐 Security Features & Rationale

### Environment Variables
**What:** Store SECRET_KEY, DEBUG, and ALLOWED_HOSTS in `.env` file (local) and Heroku config vars (production).

**Why:** 
- Keeps secrets out of GitHub where anyone can see them
- Allows different settings for local testing vs. live site
- If SECRET_KEY is exposed, hackers can access user sessions

**How:** Used `python-decouple` library, `.env` protected by `.gitignore`

---

### DEBUG Mode Off in Production
**What:** DEBUG=True locally, DEBUG=False on Heroku

**Why:**
- DEBUG=True shows detailed error messages with file paths and settings
- Hackers can use this information to find weaknesses
- Users should only see friendly error messages

**How:** Set via environment variables (different for local vs. Heroku)

---

### Login Required
**What:** Users must log in to submit services, book services, and access dashboard

**Why:**
- Stops spam and fake submissions
- Makes users accountable for their actions
- Protects against bots

**Protected pages:** Submit service, book service, edit/delete, dashboard

---

### Owner-Only Access
**What:** Users can only edit/delete their own services and bookings

**Why:**
- Stops users from deleting others' services
- Prevents sabotage and data tampering
- Builds trust in the platform

**How:** Check if `request.user == service.provider` in views

---

### CSRF Protection
**What:** All forms have `{% csrf_token %}`

**Why:**
- Stops attackers from tricking users into unwanted actions
- Ensures forms are submitted from our website, not fake sites
- Django validates the token automatically

---

### Admin Approval
**What:** Services need admin approval before showing publicly

**Why:**
- Prevents spam and scam services
- Maintains quality and trust
- Protects clients from fake listings

**How:** `is_approved` field (default: False), only show approved services

---

### Input Validation
**What:** All forms validated using Django forms

**Why:**
- Stops bad data from breaking the site
- Prevents SQL injection and XSS attacks
- Ensures data is formatted correctly

**Checks:** Required fields, max lengths, valid dates, valid prices

---

### Password Security
**What:** Django's built-in password hashing

**Why:**
- Passwords never stored as plain text
- If database is stolen, passwords are still safe
- Uses industry-standard encryption

---

### Future Improvements
- Rate limiting (stop spam submissions)
- Email verification for new accounts
- Two-factor authentication
- Password reset functionality


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