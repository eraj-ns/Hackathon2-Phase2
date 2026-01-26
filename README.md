# Todo Full-Stack Web Application

This is a secure, multi-user todo application with JWT-based authentication and user data isolation.

## Tech Stack

- **Frontend**: Next.js 16+ (App Router)
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL (or Neon Serverless PostgreSQL)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy the environment file and update the values:
   ```bash
   cp ../.env .env
   # Edit .env to add your database connection and JWT secret
   ```

5. Run the backend:
   ```bash
   python -m src.main
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## Features

- Secure user registration with email validation and strong password requirements
- Better Auth JWT with 30min expiry
- User data isolation - users can only access their own todos
- Protected API endpoints that require valid JWT tokens
- Responsive frontend interface

## API Endpoints

### Authentication

- Frontend handles auth via Better Auth: /sign-up, /sign-in (POST /api/auth/*)
- `POST /api/auth/login` - Login and get JWT token
- `GET /api/auth/verify` - Verify JWT token

### Todo Management

- `GET /api/todos` - Get all todos for the authenticated user
- `POST /api/tasks` - Create task (title required)
- `GET /api/todos/{todo_id}` - Get a specific todo
- `PUT /api/todos/{todo_id}` - Update a specific todo
- `DELETE /api/todos/{todo_id}` - Delete a specific todo

All todo endpoints require a valid JWT token in the `Authorization: Bearer {token}` header.

## Security Features

- Passwords are securely hashed using bcrypt
- JWT tokens are signed with a secret key stored in environment variables
- All protected endpoints validate JWT tokens
- Users can only access their own data
- Input validation on all endpoints

## Authentication Layout Structure

This application implements a modern authentication flow using Next.js 13+ App Router with route groups:

### Route Groups:
- `(auth)` - Contains authentication-related pages (login, signup, reset password) with a centered layout
- `(protected)` - Contains authenticated user pages (dashboard, todos) with a protected layout that checks auth status
- Root (`/`) - Public pages accessible to all users

### Key Features:
- Authentication context with login, logout, and registration
- Protected routes that redirect unauthenticated users to login
- Persistent user session using localStorage
- Responsive navigation that adapts based on authentication status
- Dark mode support throughout the application

### Pages:
- `/` - Public landing page
- `/login` - User login form
- `/signup` - User registration form
- `/reset-password` - Password reset form
- `/dashboard` - User dashboard with stats
- `/todos` - Todo management interface