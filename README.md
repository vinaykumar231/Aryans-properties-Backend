# Aryans Properties

## Overview
Aryans Properties is a comprehensive real estate platform backend built using **FastAPI** for the backend and **MySQL** as the database. The platform allows users to manage property listings, user accounts, and transactions efficiently. It supports three types of users: **Buyers**, **Sellers**, and **Admins**, each with their own dedicated features.

---

## Features

### **Buyer Portal**
- **Profile**: View and manage buyer details.
- **Property Search**:
  - Search for properties using filters (location, price, size, amenities).
  - View detailed property listings.
- **Transaction Management**: Initiate and track property transactions.
- **Notifications**: Receive updates on transactions via email and SMS.

---

### **Seller Portal**
- **Profile**: Manage seller details.
- **Property Management**:
  - List new properties for sale.
  - Edit or delete existing property listings.
- **Transaction Overview**: View transaction history and status.

---

### **Admin Portal**
- **Dashboard**:
  - View details of all users (buyers and sellers).
  - Monitor property listings and transactions.
- **User  Management**:
  - Manage user accounts and permissions.
- **Content Management**:
  - Handle property details and announcements.
- **Payment Management**:
  - View and manage payment details for transactions.

---

## Technology Stack
### **Backend**
Ensure the following are installed on your system:
- Python 3.12.2 
- FastAPI
- Mysql (or other relational database)
- git

---

## Installation Instructions

### **Backend**
1. Clone the repository:
   ```bash
   git clone https://github.com/vinaykumar231/Aryans-properties-Backend.git
   cd aryans-properties-backend

install dependencies:
bash

Verify

Open In Editor
Run
Copy code
pip install -r requirements.txt
Set up the database:
Create a MySQL database.
Update the database connection string in the settings.py or .env file.
Run the application:
bash

Verify

Open In Editor
Run
Copy code
uvicorn main:app --reload
Access the API docs at http://localhost:8000/docs.
Database Structure
Tables
Users: Stores details of buyers, sellers, and admins.
Properties: Stores property details.
Transactions: Tracks property transactions.
Notifications: Stores notifications for users.
API Endpoints
Buyer APIs
Get buyer profile
Search for properties
Initiate transactions
Seller APIs
Manage property listings
View transaction history
Admin APIs
Manage user accounts
Monitor property listings
Handle payments
Future Enhancements
Integration with third-party payment gateways.
Enhanced reporting and analytics for transactions.
Mobile app support for buyers and sellers.
License
This project is licensed.

Author
Vinay Kumar
vinaykumar.pydev@gmail.com
