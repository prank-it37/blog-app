# Blog App

A full-stack blogging web application built using Python, Flask, SQLite, and Jinja2.

The project allows users to register accounts, log in securely, create posts, edit their own content, and manage their blogs through a simple and intuitive interface.

Originally started as a blog platform, the project is actively being developed with the long-term goal of evolving into a fully functional social media application.

## Features

Authentication

* User registration
* Secure login and logout
* Password hashing
* Session management

Blog Management

* Create posts
* Edit posts
* Delete posts
* View all published posts
* Author-based access control

Backend

* Flask-based architecture
* Modular project structure
* Request routing and handling
* Dynamic page rendering with Jinja2

Database

* SQLite integration
* Relational schema for users and posts
* Database initialization scripts

Testing

* Automated tests using Pytest
* Isolated test databases
* Verification of authentication and blog functionality

## Tech Stack

* Python
* Flask
* SQLite
* Jinja2
* HTML
* CSS
* Pytest
* Git and GitHub

## Project Structure

The application follows Flask's recommended package structure.

The `flaskr` package contains the core application logic.

* `auth.py` manages registration and authentication.
* `blog.py` contains routes and functionality related to posts.
* `db.py` handles database connections and initialization.
* `schema.sql` defines the database schema.
* `templates/` contains Jinja2 templates.
* `static/` stores CSS and other static assets.

The `tests` directory contains automated tests.

The `instance` directory stores instance-specific files, including the SQLite database.

Files such as `requirements.txt`, `pyproject.toml`, and `README.md` provide dependency information, project configuration, and documentation.

## Current Functionality

* User authentication
* CRUD operations for blog posts
* Persistent database storage
* Template inheritance with Jinja2
* Unit testing support

## Future Development

The project is being expanded beyond a traditional blogging platform.

Planned features include:

### User Profiles

* Profile pictures
* User bios
* Public profile pages

### Social Features

* Likes and reactions
* Comments and replies
* Follow and unfollow functionality
* Notifications

### Media Support

* Image uploads
* Video uploads
* Audio attachments

### Real-Time Communication

* Private messaging
* Group chats
* WebSocket-based communication

### Scalability Improvements

* PostgreSQL migration
* SQLAlchemy ORM
* Redis caching
* Docker containerization
* REST APIs
* Cloud deployment

### Security Enhancements

* Email verification
* Password reset functionality
* CSRF protection
* Rate limiting

## Status

In Active Development

This project began as a learning exercise in full-stack web development and continues to grow. The long-term vision is to transform it into a complete social media platform while exploring modern web technologies and scalable system design.
