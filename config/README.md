# Photo Gallery Web Application

A full-stack photo gallery web application built with Django and PostgreSQL. The application allows users to register, manage their profiles, upload photos, browse the gallery, filter photos by tags, and interact with photos through likes and dislikes.

## Features

### Authentication

- User registration
- User login and logout
- Unique username validation
- Unique email validation
- Password validation
- Secure password hashing
- Authentication-protected pages

### User Profiles

- Automatic profile creation
- Profile picture upload
- User bio
- Edit username and email
- Change password

### Photo Gallery

- Upload photos
- Add photo titles and descriptions
- Add photo tags
- Browse uploaded photos
- View individual photo details
- Filter photos by tags
- Display photo uploader and upload date

### Photo Interactions

- Like photos
- Dislike photos
- Display like and dislike counts
- Prevent users from liking and disliking the same photo at the same time

## Technologies Used

- Python 3.11
- Django 3.2.25
- PostgreSQL
- HTML5
- Tailwind CSS
- Font Awesome
- Pillow
- Git
- GitHub
- Render

## Project Structure

```text
photo-gallery/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── photo_gallery/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── change_password.html
│   │   ├── upload_photo.html
│   │   └── photo_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md


## Author

Abigael Mwangi

- Email: abigaelmwangi534@gmail.com
- GitHub: Abbie Jonnes

#License
This project is under the MIT License