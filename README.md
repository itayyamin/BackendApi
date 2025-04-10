# BackendApi

A Python-based Backend API built with FastAPI and SQLAlchemy.

## Features

- FastAPI web framework with automatic OpenAPI documentation
- SQLAlchemy ORM with database migrations using Alembic
- Environment-based configuration using python-dotenv
- Pydantic data validation
- RESTful API design
- Comprehensive test suite using pytest

## Project Structure

```
backendapi/
├── __init__.py          # Package initialization
├── main.py              # Application entry point
├── database.py          # Database configuration
├── models/              # Database models
│   ├── __init__.py
│   └── item.py          # Sample Item model
├── routes/              # API route handlers
│   ├── __init__.py
│   └── items.py         # Item CRUD endpoints
```

## Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/itayyamin/BackendApi.git
   cd BackendApi
   ```

2. Set up a virtual environment:

   **Windows:**
   ```
   setup_venv.bat
   ```

   **macOS/Linux:**
   ```
   chmod +x setup_venv.sh
   ./setup_venv.sh
   ```

3. Create a `.env` file by copying the `.env.example` file:
   ```
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```

4. Customize the environment variables in the `.env` file as needed.

## Running the Application

1. Activate the virtual environment if it's not already activated:

   **Windows:**
   ```
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```
   source venv/bin/activate
   ```

2. Run the application:
   ```
   uvicorn backendapi.main:app --reload
   ```

3. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

- `GET /`: Root endpoint with API information
- `GET /health`: Health check endpoint
- `GET /items/`: List all items
- `POST /items/`: Create a new item
- `GET /items/{item_id}`: Get a specific item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

## Development

### Adding New Models

1. Create a new model file in the `backendapi/models` directory
2. Define your model class extending from `Base`
3. Import and include your model in `database.py`

### Adding New Routes

1. Create a new route file in the `backendapi/routes` directory
2. Define your router and endpoints
3. Import and include your router in `main.py`

## Testing

Run the tests with pytest:

```
pytest
```

## License

MIT
