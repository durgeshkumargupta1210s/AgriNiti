"""
Pest Detection ML Model using TensorFlow/Keras
"""

import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import os
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)

class PestDetectionModel:
    def __init__(self, model_path: str = None):
        self.model_path = model_path or "app/ml_models/pest_detection_model.h5"
        self.model = None
        self.class_names = [
            "Healthy", "Aphids", "Whiteflies", "Spider Mites", "Thrips",
            "Leaf Miners", "Caterpillars", "Mealybugs", "Scale Insects",
            "Leaf Blight", "Powdery Mildew", "Rust", "Bacterial Spot",
            "Virus", "Nematodes", "Root Rot"
        ]
        self.load_model()
    
    def load_model(self):
        """Load the pre-trained pest detection model"""
        try:
            if os.path.exists(self.model_path):
                self.model = tf.keras.models.load_model(self.model_path)
                logger.info("Pest detection model loaded successfully")
            else:
                self.create_model()
                logger.info("New pest detection model created")
        except Exception as e:
            logger.error(f"Error loading pest detection model: {e}")
            self.create_model()
    
    def create_model(self):
        """Create a new pest detection model"""
        try:
            # Create a CNN model for pest detection
            model = tf.keras.Sequential([
                tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(512, activation='relu'),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(len(self.class_names), activation='softmax')
            ])
            
            model.compile(
                optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            self.model = model
            logger.info("New pest detection model created")
        except Exception as e:
            logger.error(f"Error creating pest detection model: {e}")
            raise
    
    def preprocess_image(self, image_path: str) -> np.ndarray:
        """Preprocess image for model prediction"""
        try:
            # Load and resize image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError("Could not load image")
            
            # Convert BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Resize to model input size
            image = cv2.resize(image, (224, 224))
            
            # Normalize pixel values
            image = image.astype(np.float32) / 255.0
            
            # Add batch dimension
            image = np.expand_dims(image, axis=0)
            
            return image
        except Exception as e:
            logger.error(f"Error preprocessing image: {e}")
            raise
    
    def predict(self, image_path: str) -> Dict:
        """Predict pest/disease from image"""
        try:
            if self.model is None:
                raise ValueError("Model not loaded")
            
            # Preprocess image
            processed_image = self.preprocess_image(image_path)
            
            # Make prediction
            predictions = self.model.predict(processed_image)
            confidence_scores = predictions[0]
            
            # Get top 3 predictions
            top_indices = np.argsort(confidence_scores)[-3:][::-1]
            
            results = []
            for idx in top_indices:
                results.append({
                    "class": self.class_names[idx],
                    "confidence": float(confidence_scores[idx])
                })
            
            # Get primary prediction
            primary_prediction = results[0]
            
            return {
                "primary_prediction": primary_prediction,
                "all_predictions": results,
                "confidence_threshold": 0.7,
                "is_healthy": primary_prediction["class"] == "Healthy"
            }
            
        except Exception as e:
            logger.error(f"Error in pest prediction: {e}")
            return {
                "error": str(e),
                "primary_prediction": {"class": "Unknown", "confidence": 0.0}
            }
    
    def get_treatment_recommendations(self, pest_class: str) -> Dict:
        """Get treatment recommendations for detected pest/disease"""
        treatments = {
            "Aphids": {
                "organic": ["Neem oil spray", "Soap water solution", "Ladybugs introduction"],
                "chemical": ["Imidacloprid", "Acephate"],
                "prevention": ["Regular monitoring", "Beneficial insects", "Proper plant spacing"]
            },
            "Whiteflies": {
                "organic": ["Yellow sticky traps", "Neem oil", "Insecticidal soap"],
                "chemical": ["Pyrethroids", "Systemic insecticides"],
                "prevention": ["Good ventilation", "Remove infected plants", "Regular cleaning"]
            },
            "Spider Mites": {
                "organic": ["Water spray", "Predatory mites", "Neem oil"],
                "chemical": ["Miticide sprays", "Acaricides"],
                "prevention": ["High humidity", "Regular misting", "Clean environment"]
            },
            "Leaf Blight": {
                "organic": ["Copper fungicide", "Baking soda spray", "Proper drainage"],
                "chemical": ["Chlorothalonil", "Mancozeb"],
                "prevention": ["Crop rotation", "Good air circulation", "Avoid overhead watering"]
            },
            "Powdery Mildew": {
                "organic": ["Milk spray", "Baking soda solution", "Sulfur dust"],
                "chemical": ["Fungicides", "Systemic treatments"],
                "prevention": ["Proper spacing", "Good air flow", "Resistant varieties"]
            }
        }
        
        return treatments.get(pest_class, {
            "organic": ["General organic treatment", "Neem oil", "Proper plant care"],
            "chemical": ["Consult agricultural expert", "Appropriate pesticides"],
            "prevention": ["Regular monitoring", "Good plant hygiene", "Proper nutrition"]
        })
