# Discussion Board Project

A dynamic discussion board platform built with Django that allows users to engage in meaningful conversations across various topics.

## Features

- User Authentication System
  - Sign up with custom user profiles
  - Login/Logout functionality
  - Password change capability
  - Profile management with avatar support

- Discussion Boards
  - Multiple topic boards
  - Post and topic tracking
  - Last post tracking
  - Topic count and post count tracking

- User Interface
  - Responsive design using Bootstrap 5
  - Clean and intuitive navigation
  - Real-time feedback with success/error messages
  - FontAwesome icons integration

## Technology Stack

- Backend
  - Python 3.x
  - Django Web Framework
  - postgresql

- Frontend
  - HTML5
  - Bootstrap 5.3
  - CSS3
  - JavaScript/jQuery 3.7.1

## Screenshots


![Home Page](discussion_board/screenshots/main.jpeg)

### Discussion Board
![Alt text](discussion_board/screenshots/2.jpeg)


## Project Structure

```
discussion_board/
├── accounts/                 # User authentication and profiles
│   ├── templates/
│   │   └── accounts/
│   │       ├── my_profile.html
│   │       ├── signup.html
│   │       └── change_password.html
│   ├── forms.py
│   └── views.py
├── boards/                   # Main discussion board functionality
│   ├── templates/
│   │   ├── home.html
│   │   ├── about.html
│   │   └── base.html
├── static/                   # Static files
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── jquery-3.7.1.min.js
```

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd djangopr1
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

## Key Features

### User Management
- Profile customization with avatar uploads
- Secure password change system
- Profile information updates
- User authentication and authorization

### Board System
- Multiple discussion boards
- Topic and post tracking
- Last post tracking
- Board statistics (post count, topic count)

### UI/UX Features
- Responsive design for all devices
- Bootstrap-based clean interface
- Interactive feedback messages
- User-friendly navigation

## Security Features

- CSRF protection
- Secure password handling
- Login required decorators
- File upload validation

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

