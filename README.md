# Django Food Delivery Web Application

## Description
This project is a web-based application developed using the Django framework. It is designed to manage food delivery orders with integrated user authentication, including social login features. The app allows customers to place and track food orders, while admins can manage these orders via an admin dashboard.

## Features
- User authentication (with social account integration)
- Food delivery order management system
- Admin dashboard for managing and tracking food orders
- Customizable templates for user interactions (e.g., order status, menus)
- Order tracking with fields for payment status and delivery progress
- SQLite database for backend data storage

## Project Structure
- `customer/`: Contains the core logic for handling food orders and customer information.
  - `models.py`: Defines the `OrderModel` used for managing food orders.
  - `views.py`: Manages user requests and the food ordering process.
  - `templates/`: HTML templates for the customer interface, such as order details, menus, and about page.
- `migrations/`: Database migrations to track changes in the models.
- `manage.py`: Django's command-line utility for administrative tasks.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project-folder
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000/`.

## Usage
- Register or log in using a social account or email.
- Browse menus, place food orders, and track delivery status.
- Admins can log in to manage customer orders and view statistics.
