# CM4025 Coursework Project

This is a Django-based web application for managing and sharing stories. Users can submit, view, and rate stories.

## Features
- Submit new stories with a title, author, content, and genre.
- View a random story on the home page.
- Manage your own stories (edit or delete).
- Rate stories with a star rating system.
- User authentication (login, logout, and account management).

## Installation

1. Clone the repository:
   git clone <repository-url>
   cd CM4025_CW

2. Install the requirements:
    pip install -r requirements.txt

3. Apply Migrations
    python manage.py makemigrations
    python manage.py migrate

4. Run server
    python manage.py runserver