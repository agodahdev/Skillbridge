# SkillBridge - User Stories

## Agile Methodology

This project was developed using Agile methodology with user stories tracked in GitHub Issues. All stories were implemented and closed upon completion.

**GitHub Project Board:** https://github.com/agodahdev/Skillbridge/issues

---

## MoSCoW Prioritization

Stories are prioritized using the MoSCoW method:
- **Must Have:** Critical features required for MVP
- **Should Have:** Important features that add significant value
- **Could Have:** Nice-to-have features if time permits
- **Won't Have:** Features for future releases

### Story Points Breakdown
- **Must Have:** 6 stories (60%)
- **Should Have:** 3 stories (30%)
- **Could Have:** 1 story (10%)
- **Won't Have:** 0 stories (future roadmap)

**Total Should-Have: 30% (Well under 60% requirement ✅)**


## User Stories by Role

### Client User Stories


#### User Story #1: Register & Login 🔴 MUST HAVE
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

#### User Story #2: View Available Services 🔴 MUST HAVE
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


#### User Story #3: Book a Service 🟡 SHOULD HAVE
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

#### User Story #4: Post New Service 🔴 MUST HAVE
**As a** Provider  
**I want to** create a new service listing  
**So that** clients can find and book me

**Acceptance Criteria:**
- I can input a service name, description, category, and rate
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

#### User Story #5: Edit/Delete My Service 🟡 SHOULD HAVE
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

#### User Story #6: View My Bookings 🟡 SHOULD HAVE
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

#### User Story #7: Approve or Reject Services 🔴 MUST HAVE
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

#### User Story #8: Frontend CRUD (No Admin Panel) 🟢 COULD HAVE
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

#### User Story #9: Production-Ready Setup 🔴 MUST HAVE
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

---

#### User Story #10: Setup Project Infrastructure 🔴 MUST HAVE
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

**Project Repository:** https://github.com/agodahdev/Skillbridge  
**Live Site:** https://skillbridge-ba237edbd42e.herokuapp.com/