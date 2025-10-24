"""
Crop Recommendation ML Model using Scikit-learn
"""

import joblib
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

logger = logging.getLogger(__name__)

class CropRecommendationModel:
    def __init__(self, model_path: str = None):
        self.model_path = model_path or "app/ml_models/crop_recommendation_model.pkl"
        self.model = None
        self.label_encoders = {}
        self.feature_columns = [
            'temperature', 'humidity', 'ph', 'rainfall', 'soil_type_encoded',
            'season_encoded', 'region_encoded', 'water_requirement_encoded'
        ]
        self.crop_data = self.load_crop_data()
        self.load_model()
    
    def load_crop_data(self) -> pd.DataFrame:
        """Load crop data for recommendations"""
        # Sample crop data - in production, this would come from database
        crop_data = pd.DataFrame({
            'crop_name': [
                'Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane', 'Potato',
                'Tomato', 'Onion', 'Chili', 'Cabbage', 'Cauliflower', 'Spinach',
                'Mango', 'Banana', 'Orange', 'Apple', 'Grapes', 'Pomegranate'
            ],
            'temperature_min': [20, 15, 18, 20, 20, 10, 15, 10, 20, 10, 10, 5, 20, 20, 10, 5, 15, 20],
            'temperature_max': [35, 25, 30, 35, 35, 25, 30, 25, 35, 25, 25, 20, 35, 35, 30, 25, 30, 35],
            'humidity_min': [60, 40, 50, 50, 60, 60, 60, 50, 50, 60, 60, 70, 60, 70, 60, 50, 50, 60],
            'humidity_max': [90, 80, 90, 90, 90, 90, 90, 80, 90, 90, 90, 95, 90, 95, 90, 80, 80, 90],
            'ph_min': [5.5, 6.0, 5.5, 6.0, 6.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0],
            'ph_max': [7.5, 7.5, 7.0, 8.0, 7.5, 6.5, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0],
            'rainfall_min': [1000, 300, 500, 500, 1000, 500, 500, 400, 500, 500, 500, 600, 1000, 1000, 800, 500, 500, 500],
            'rainfall_max': [3000, 1000, 2000, 1500, 3000, 1500, 1500, 1200, 1500, 1500, 1500, 2000, 3000, 3000, 2000, 1500, 1500, 1500],
            'soil_type': ['clay', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy', 'loamy'],
            'season': ['kharif', 'rabi', 'kharif', 'kharif', 'kharif', 'rabi', 'kharif', 'rabi', 'kharif', 'rabi', 'rabi', 'rabi', 'kharif', 'kharif', 'kharif', 'rabi', 'kharif', 'kharif'],
            'region': ['north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north', 'north'],
            'water_requirement': ['high', 'medium', 'medium', 'medium', 'high', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'high', 'medium', 'high', 'medium', 'medium', 'medium', 'medium'],
            'yield_per_hectare': [4.5, 3.8, 4.2, 2.2, 70, 25, 30, 20, 15, 35, 25, 20, 15, 25, 20, 15, 20, 15],
            'market_price': [3500, 2200, 1800, 7000, 3500, 2000, 3000, 2500, 8000, 1500, 2000, 3000, 5000, 3000, 4000, 6000, 8000, 6000]
        })
        return crop_data
    
    def load_model(self):
        """Load the pre-trained crop recommendation model"""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
                logger.info("Crop recommendation model loaded successfully")
            else:
                self.create_model()
                logger.info("New crop recommendation model created")
        except Exception as e:
            logger.error(f"Error loading crop recommendation model: {e}")
            self.create_model()
    
    def create_model(self):
        """Create and train a new crop recommendation model"""
        try:
            # Prepare features
            df = self.crop_data.copy()
            
            # Encode categorical variables
            categorical_columns = ['soil_type', 'season', 'region', 'water_requirement']
            for col in categorical_columns:
                le = LabelEncoder()
                df[f'{col}_encoded'] = le.fit_transform(df[col])
                self.label_encoders[col] = le
            
            # Prepare features and target
            X = df[self.feature_columns]
            y = df['crop_name']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.model = RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                max_depth=10
            )
            self.model.fit(X_train, y_train)
            
            # Save model
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            
            logger.info("Crop recommendation model trained and saved")
            
        except Exception as e:
            logger.error(f"Error creating crop recommendation model: {e}")
            raise
    
    def preprocess_input(self, input_data: Dict) -> np.ndarray:
        """Preprocess input data for prediction"""
        try:
            # Create feature vector
            features = np.array([
                input_data.get('temperature', 25),
                input_data.get('humidity', 70),
                input_data.get('ph', 6.5),
                input_data.get('rainfall', 1000),
                self.label_encoders['soil_type'].transform([input_data.get('soil_type', 'loamy')])[0],
                self.label_encoders['season'].transform([input_data.get('season', 'kharif')])[0],
                self.label_encoders['region'].transform([input_data.get('region', 'north')])[0],
                self.label_encoders['water_requirement'].transform([input_data.get('water_requirement', 'medium')])[0]
            ]).reshape(1, -1)
            
            return features
        except Exception as e:
            logger.error(f"Error preprocessing input: {e}")
            raise
    
    def recommend_crops(self, input_data: Dict) -> Dict:
        """Recommend crops based on input parameters"""
        try:
            if self.model is None:
                raise ValueError("Model not loaded")
            
            # Preprocess input
            features = self.preprocess_input(input_data)
            
            # Get predictions with probabilities
            probabilities = self.model.predict_proba(features)[0]
            crop_names = self.model.classes_
            
            # Get top 5 recommendations
            top_indices = np.argsort(probabilities)[-5:][::-1]
            
            recommendations = []
            for idx in top_indices:
                crop_name = crop_names[idx]
                probability = probabilities[idx]
                
                # Get crop details
                crop_info = self.crop_data[self.crop_data['crop_name'] == crop_name].iloc[0]
                
                recommendations.append({
                    'crop_name': crop_name,
                    'confidence': float(probability),
                    'yield_per_hectare': float(crop_info['yield_per_hectare']),
                    'market_price': float(crop_info['market_price']),
                    'water_requirement': crop_info['water_requirement'],
                    'season': crop_info['season'],
                    'suitability_score': float(probability * 100)
                })
            
            return {
                'recommendations': recommendations,
                'input_parameters': input_data,
                'total_crops_analyzed': len(crop_names)
            }
            
        except Exception as e:
            logger.error(f"Error in crop recommendation: {e}")
            return {
                'error': str(e),
                'recommendations': []
            }
    
    def get_crop_details(self, crop_name: str) -> Dict:
        """Get detailed information about a specific crop"""
        try:
            crop_info = self.crop_data[self.crop_data['crop_name'] == crop_name]
            if crop_info.empty:
                return {'error': 'Crop not found'}
            
            crop = crop_info.iloc[0]
            return {
                'crop_name': crop['crop_name'],
                'temperature_range': f"{crop['temperature_min']}-{crop['temperature_max']}°C",
                'humidity_range': f"{crop['humidity_min']}-{crop['humidity_max']}%",
                'ph_range': f"{crop['ph_min']}-{crop['ph_max']}",
                'rainfall_range': f"{crop['rainfall_min']}-{crop['rainfall_max']}mm",
                'soil_type': crop['soil_type'],
                'season': crop['season'],
                'water_requirement': crop['water_requirement'],
                'yield_per_hectare': float(crop['yield_per_hectare']),
                'market_price': float(crop['market_price'])
            }
        except Exception as e:
            logger.error(f"Error getting crop details: {e}")
            return {'error': str(e)}
