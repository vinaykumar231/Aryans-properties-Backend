# Aryans Properties

## Overview

Aryans Properties is a comprehensive real estate platform backend developed using **FastAPI** and **MySQL**. The platform provides a robust solution for managing property listings, user accounts, and transactions with dedicated portals for Buyers, Sellers, and Admins.

## Features

### Buyer Portal
- **Profile Management**: View and update buyer details
- **Property Search**: 
  - Advanced filtering (location, price, size, amenities)
  - Detailed property listing views
- **Transaction Tracking**: Initiate and monitor property transactions
- **Notifications**: Email and SMS updates on transaction status

### Seller Portal
- **Profile Management**: Update and maintain seller information
- **Property Listing**:
  - Add new properties for sale
  - Edit or remove existing property listings
- **Transaction Insights**: Comprehensive transaction history and status monitoring

### Admin Portal
- **Dashboard**:
  - Comprehensive overview of users and properties
  - Transaction and listing monitoring
- **User Management**:
  - Account creation and permission control
- **Content Administration**:
  - Property detail management
  - Announcement handling
- **Payment Oversight**:
  - Full transaction payment tracking

## Technology Stack

### Backend
- Python 3.12.2
- FastAPI
- MySQL
- Git

## Prerequisites

- Python 3.12.2 installed
- MySQL database
- Git

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vinaykumar231/Aryans-properties-Backend.git
   cd aryans-properties-backend
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Database Configuration:
   - Create a MySQL database
   - Update connection details in `settings.py` or `.env`

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access API Documentation:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Database Structure

### Primary Tables
- **Users**: Stores user (buyer, seller, admin) details
- **Properties**: Comprehensive property information
- **Transactions**: Transaction tracking and details
- **Notifications**: User communication log

## API Endpoints

### Authentication
- User registration
- Login and logout
- Password reset

### Buyer Endpoints
- Profile retrieval and update
- Property search
- Transaction initiation

### Seller Endpoints
- Property listing management
- Transaction history

### Admin Endpoints
- User account management
- Property and transaction oversight

## Future Roadmap

- Third-party video conferencing integration
- Advanced reporting and analytics
- Cross-platform mobile application support
- Enhanced search and recommendation algorithms

## Security Features

- Role-based access control
- Secure authentication
- Data encryption
- Regular security audits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

Proprietary software. All rights reserved by Maitri AI.

## Contact

**Vinay Kumar**
- Email: vinaykumar.pydev@gmail.com
- GitHub: [@vinaykumar231](https://github.com/vinaykumar231)
