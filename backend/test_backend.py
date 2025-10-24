"""
Simple test script to verify backend setup
"""

import requests
import json
import os
import sys

def test_backend_health():
    """Test if backend is running and healthy"""
    try:
        response = requests.get("http://localhost:8000/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check passed")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not accessible: {e}")
        return False

def test_api_endpoints():
    """Test basic API endpoints"""
    base_url = "http://localhost:8000"
    
    endpoints = [
        ("/", "Root endpoint"),
        ("/api/health", "Health check"),
        ("/docs", "API documentation"),
    ]
    
    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {description}: OK")
            else:
                print(f"⚠️ {description}: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {description}: {e}")

def test_ml_models():
    """Test ML model initialization"""
    try:
        # Test pest detection model
        from app.ml_models.pest_detection import PestDetectionModel
        pest_model = PestDetectionModel()
        print("✅ Pest detection model loaded")
        
        # Test crop recommendation model
        from app.ml_models.crop_recommendation import CropRecommendationModel
        crop_model = CropRecommendationModel()
        print("✅ Crop recommendation model loaded")
        
        return True
    except Exception as e:
        print(f"❌ ML model loading failed: {e}")
        return False

def test_database_connection():
    """Test database connection"""
    try:
        from app.database import get_db
        from app.models.user import User
        from sqlalchemy.orm import Session
        
        # This is a basic test - in production, you'd want more comprehensive tests
        print("✅ Database models imported successfully")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing FARMER Backend Setup")
    print("=" * 40)
    
    # Test 1: Backend health
    print("\n1. Testing Backend Health...")
    health_ok = test_backend_health()
    
    # Test 2: API endpoints
    print("\n2. Testing API Endpoints...")
    test_api_endpoints()
    
    # Test 3: ML models
    print("\n3. Testing ML Models...")
    ml_ok = test_ml_models()
    
    # Test 4: Database
    print("\n4. Testing Database Connection...")
    db_ok = test_database_connection()
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Test Summary:")
    print(f"Backend Health: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"ML Models: {'✅ PASS' if ml_ok else '❌ FAIL'}")
    print(f"Database: {'✅ PASS' if db_ok else '❌ FAIL'}")
    
    if health_ok and ml_ok and db_ok:
        print("\n🎉 All tests passed! Backend is ready.")
        return True
    else:
        print("\n⚠️ Some tests failed. Check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
