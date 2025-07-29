# Property Management POC Backend

A comprehensive REST API backend for property management built with FastAPI, SQLAlchemy, and PostgreSQL. This system manages properties, rental contracts, and payment tracking.

## Features

- **Property Management**: Store and manage property details including address, type, rooms, size, and estimated value
- **Contract Management**: Create and track rental contracts with tenant information, rent amounts, and lease terms
- **Payment Tracking**: Record and monitor rental payments with various payment methods and status tracking
- **RESTful API**: Clean, documented API endpoints with automatic OpenAPI/Swagger documentation
- **Database Integration**: PostgreSQL database with SQLAlchemy ORM for robust data management

## Project Structure

```
merent_be/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database configuration and session management
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── crud.py             # Database CRUD operations
│   └── routers/
│       ├── __init__.py
│       ├── properties.py    # Property-related API endpoints
│       ├── contracts.py     # Contract-related API endpoints
│       └── payments.py      # Payment-related API endpoints
├── requirements.txt         # Python dependencies
└── README.md              # This file
```

## Data Models

### Property
- `id`: Primary key
- `address`: Property address
- `type`: Property type (apartment, house, etc.)
- `rooms`: Number of rooms
- `size`: Property size in square meters
- `neighborhood`: Neighborhood/location
- `floor`: Floor number
- `unit`: Unit number
- `estimated_value`: Estimated property value

### Contract
- `id`: Primary key
- `property_id`: Foreign key to Property
- `tenant_name`: Tenant's name
- `monthly_rent`: Monthly rental amount
- `start_date`: Contract start date
- `end_date`: Contract end date
- `include_taxes`: Whether taxes are included
- `include_fees`: Whether fees are included
- `status`: Contract status

### Payment
- `id`: Primary key
- `contract_id`: Foreign key to Contract
- `amount`: Payment amount
- `date`: Payment date
- `method`: Payment method
- `reference`: Payment reference
- `receipt_filename`: Receipt file name
- `status`: Payment status

## API Endpoints

### Properties
- `GET /properties/` - List all properties
- `POST /properties/` - Create a new property

### Contracts
- `GET /contracts/property/{property_id}` - List contracts for a specific property
- `POST /contracts/` - Create a new contract

### Payments
- `GET /payments/contract/{contract_id}` - List payments for a specific contract
- `POST /payments/` - Create a new payment

## Setup

### Prerequisites
- Python 3.7+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd merent_be
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
   
   Set your database URL in the `.env` file:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   ```

5. **Database Setup**
   - Create a PostgreSQL database
   - Update the `DATABASE_URL` in your `.env` file
   - The application will automatically create tables on startup

6. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative API docs**: `http://localhost:8000/redoc` (ReDoc)

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **Pydantic**: Data validation using Python type annotations
- **python-dotenv**: Environment variable management
- **psycopg2-binary**: PostgreSQL adapter for Python

## Development

### Code Structure
- **Models** (`app/models.py`): SQLAlchemy ORM models defining database schema
- **Schemas** (`app/schemas.py`): Pydantic models for request/response validation
- **CRUD** (`app/crud.py`): Database operations and business logic
- **Routers** (`app/routers/`): API endpoint definitions organized by resource
- **Database** (`app/database.py`): Database connection and session management

### Adding New Features
1. Define new models in `app/models.py`
2. Create corresponding schemas in `app/schemas.py`
3. Add CRUD operations in `app/crud.py`
4. Create router endpoints in appropriate router file
5. Include new router in `app/main.py`

## License

[Add your license information here]
