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