# FARMER Backend API

Agricultural Intelligence Platform with ML Models for Pest Detection and Crop Recommendations.

## 🚀 Features

- **Pest Detection**: AI-powered pest and disease detection from images
- **Crop Recommendations**: ML-based crop suggestions based on farm conditions
- **Weather Integration**: Real-time weather data and forecasts
- **Market Data**: Crop prices and market analysis
- **Community Forum**: Farmer community discussions
- **AI Advisory**: Intelligent farming advice and recommendations

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework
- **PostgreSQL**: Primary database
- **Redis**: Caching and session management
- **TensorFlow**: ML models for pest detection
- **Scikit-learn**: Crop recommendation algorithms
- **Docker**: Containerization
- **Nginx**: Reverse proxy

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose (optional)

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

1. **Clone and setup**:
   ```bash
   cd backend
   cp env.example .env
   # Edit .env with your API keys
   ```

2. **Start services**:
   ```bash
   docker-compose up -d
   ```

3. **Access the API**:
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/api/health

### Option 2: Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup database**:
   ```bash
   # Start PostgreSQL and Redis
   # Create database: farmer_db
   ```

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Pest Detection
- `POST /api/pests/detect` - Detect pest from image
- `GET /api/pests/detections` - Get detection history
- `GET /api/pests/pests` - Get pests list

### Crop Recommendations
- `POST /api/crops/recommend` - Get crop recommendations
- `GET /api/crops/crops` - Get crops list
- `GET /api/crops/user-crops/{user_id}` - Get user's crops

### Weather Data
- `GET /api/weather/current/{location}` - Current weather
- `GET /api/weather/forecast/{location}` - Weather forecast
- `GET /api/weather/alerts/{user_id}` - Weather alerts

### Market Data
- `GET /api/market/prices` - Market prices
- `GET /api/market/analysis/{location}` - Market analysis
- `GET /api/market/news` - Market news

### Forum
- `POST /api/forum/posts` - Create forum post
- `GET /api/forum/posts` - Get forum posts
- `POST /api/forum/posts/{post_id}/comments` - Add comment

### AI Advisory
- `POST /api/advisory/chat` - Get AI advice
- `GET /api/advisory/conversations/{user_id}` - Get conversations
- `GET /api/advisory/quick-actions` - Get quick actions

## 🤖 ML Models

### Pest Detection Model
- **Framework**: TensorFlow/Keras
- **Input**: 224x224 RGB images
- **Output**: Pest classification with confidence scores
- **Classes**: 16 pest/disease categories

### Crop Recommendation Model
- **Framework**: Scikit-learn
- **Algorithm**: Random Forest
- **Input**: Weather, soil, and farm conditions
- **Output**: Ranked crop recommendations

## 🗄️ Database Schema

### Core Tables
- `users` - User profiles and authentication
- `crops` - Crop information and requirements
- `pests` - Pest and disease database
- `weather_data` - Weather records
- `market_prices` - Market price data
- `forum_posts` - Community discussions

### ML Tables
- `pest_detections` - Pest detection results
- `crop_recommendations` - Recommendation history
- `advisory_conversations` - AI chat history

## 🔧 Configuration

### Environment Variables
```bash
DATABASE_URL=postgresql://user:pass@localhost:5432/farmer_db
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
OPENWEATHER_API_KEY=your-api-key
MARKET_DATA_API_KEY=your-api-key
```

### API Keys Required
- **OpenWeatherMap**: Weather data
- **Market Data API**: Price information

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_pest_detection.py
```

## 📊 Monitoring

### Health Checks
- API Health: `/api/health`
- Database: Connection status
- Redis: Cache status
- ML Models: Model loading status

### Logging
- Application logs: `logs/app.log`
- Error logs: `logs/error.log`
- ML model logs: `logs/ml.log`

## 🚀 Deployment

### Production Deployment
1. **Setup production environment**:
   ```bash
   export DATABASE_URL=postgresql://prod_user:prod_pass@prod_host:5432/farmer_prod
   export SECRET_KEY=production-secret-key
   ```

2. **Deploy with Docker**:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. **Setup SSL certificates**:
   ```bash
   # Add SSL certificates to nginx/ssl/
   ```

### Scaling
- **Horizontal**: Multiple backend instances
- **Database**: Read replicas for queries
- **Cache**: Redis cluster for high availability
- **ML Models**: GPU instances for inference

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: [API Docs](http://localhost:8000/docs)
- **Issues**: GitHub Issues
- **Email**: support@farmer-app.com

---

**FARMER Backend** - Empowering farmers with AI-driven agricultural intelligence 🌾
