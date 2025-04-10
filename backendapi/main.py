"""
Main application file for the BackendApi.
"""
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="BackendApi",
    description="A Python Backend API Service",
    version="0.1.0",
)

@app.get("/")
async def root():
    """Root endpoint returning API information."""
    return {
        "message": "Welcome to the BackendApi",
        "status": "running",
        "version": "0.1.0",
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for the API."""
    return {
        "status": "healthy",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backendapi.main:app", host="0.0.0.0", port=8000, reload=True)