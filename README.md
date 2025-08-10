# URL Shortener

A sleek and user-friendly URL shortening web application with a modern dark-themed interface.  
Built with Django (backend) and jQuery (frontend) for fast, responsive user experience and secure URL management.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [How It Works](#how-it-works)  
- [Customization](#customization)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Overview

URL shorteners are useful tools that convert long URLs into shorter, more manageable links that are easy to share and remember. This project is a full-stack URL shortener with the following goals:

- Provide a simple, intuitive user interface with dark mode and smooth animations.  
- Use Django to securely generate and store short codes mapped to original URLs.  
- Use jQuery on the frontend to send requests and update the UI dynamically without full page reloads.  
- Provide instant feedback through toast notifications to enhance user experience.

The project serves as a great starting point for anyone interested in learning web development, Django backend, frontend interactions, or deploying practical web applications.

---

## Features

- **URL Shortening:** Quickly generate a short link that redirects to the original URL.  
- **Responsive UI:** Works well on desktops and mobile devices with flexible layout.  
- **Dark Themed Interface:** Soft color palette and dark backgrounds for comfortable viewing.  
- **3D Header Animation:** Subtle floating effect adds a modern, dynamic touch.  
- **Form Validation:** Checks for empty input and alerts users before sending requests.  
- **Clear/Cancel Button:** Instantly clear input field and remove any displayed short URLs.  
- **Toast Notifications:** Temporary popup messages inform users of success, errors, or actions.  
- **CSRF Protection:** Django’s built-in security for safe POST requests.  
- **Smooth User Experience:** AJAX requests avoid full page reloads for fast responses.

---

## Demo

To try the app locally after setup, visit:  
urlshortener/
│
├── urlshortner/                # Main Django app folder
│   ├── migrations/             # Database migration files
│   ├── static/                 # Static assets (CSS, JS, images)
│   │   └── images/             # Image assets folder
│   ├── templates/              # HTML templates including main page
│   ├── views.py                # Backend logic to handle requests
│   ├── models.py               # Database models (URL storage)
│   ├── urls.py                 # URL routing for the app
│   └── admin.py                # Django admin configuration (optional)
│
├── manage.py                   # Django management utility
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file

How It Works
Backend (Django)
When a user submits a URL via an AJAX POST request to the /create endpoint, the backend begins by validating the submitted URL to ensure it is properly formatted
and safe to store. After confirming the URL's validity, the backend generates a unique short code—typically a 6 to 8 character alphanumeric string—that serves as 
the identifier for the shortened link. This short code is then saved in the database alongside the original URL, establishing a persistent mapping between the two.
Once the short code is generated and stored, the backend sends it back to the frontend, which uses it to construct the shortened URL displayed to the user.

Later, when a user visits a URL containing the short code (for example, /short_code), the backend looks up the original URL associated with that short code by 
querying the database. Upon finding the corresponding URL, the backend seamlessly redirects the user to the original, full-length address.

