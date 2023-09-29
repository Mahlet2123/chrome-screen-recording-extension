# chrome-screen-recording-extension-react-django

This repository contains the codebase for a Chrome Extension designed to capture and share screen recordings seamlessly. The frontend is built with React, providing an intuitive user interface for initiating and managing screen recordings. On the backend, Django handles video storage and presentation.


## Project Structure

The project is organized into two main directories:

- `backend`: This directory contains the Django backend of the application.
- `frontend`: This directory is reserved for the React frontend of the application.

## Getting Started

### Backend Setup

1. Make sure you have Python and pipenv installed on your system.

2. Navigate to the `backend` directory:

- Activate the virtual environment:

		pipenv shell

- Install the required Python packages listed in `requirements.txt` into your virtual environment:

  		pipenv install -r requirements.txt

- Start the Django development server:

		python manage.py runserver

- Your Django backend should now be running locally at http://localhost:8000/.

### Frontend Setup

Make sure you have Node.js and npm (Node Package Manager) installed on your system.

Navigate to the frontend directory:

	cd frontend
