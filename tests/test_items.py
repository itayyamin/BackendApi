"""
Test cases for Item API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backendapi.main import app
from backendapi.database import Base, get_db


# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def test_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Override the get_db function for testing
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    
    yield  # Run the test
    
    # Clean up after the test
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(test_db):
    # Return a TestClient for testing API endpoints
    with TestClient(app) as c:
        yield c


def test_create_item(client):
    """Test creating a new item."""
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "Test description", "is_active": True},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "Test description"
    assert data["is_active"] is True
    assert "id" in data


def test_read_item(client):
    """Test retrieving an item by ID."""
    # First create an item
    response = client.post(
        "/items/",
        json={"name": "Get Item", "description": "Item to retrieve", "is_active": True},
    )
    created_item = response.json()
    item_id = created_item["id"]
    
    # Now retrieve it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Get Item"
    assert data["description"] == "Item to retrieve"
    assert data["id"] == item_id


def test_read_items(client):
    """Test retrieving all items."""
    # Create a few items
    client.post("/items/", json={"name": "Item 1", "description": "First item"})
    client.post("/items/", json={"name": "Item 2", "description": "Second item"})
    
    # Get all items
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2  # At least the 2 we just created
    assert any(item["name"] == "Item 1" for item in data)
    assert any(item["name"] == "Item 2" for item in data)


def test_update_item(client):
    """Test updating an item."""
    # First create an item
    response = client.post(
        "/items/",
        json={"name": "Original Name", "description": "Original description"},
    )
    created_item = response.json()
    item_id = created_item["id"]
    
    # Now update it
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Name", "description": "Updated description", "is_active": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["description"] == "Updated description"
    assert data["is_active"] is False
    assert data["id"] == item_id


def test_delete_item(client):
    """Test deleting an item."""
    # First create an item
    response = client.post(
        "/items/",
        json={"name": "Item to Delete", "description": "Will be deleted"},
    )
    created_item = response.json()
    item_id = created_item["id"]
    
    # Now delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404