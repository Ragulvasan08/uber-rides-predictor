# 🚀 Uber Rides Prediction - Flask Web App

A stunning, ultra-modern machine learning web application that predicts weekly Uber rides based on various city parameters. Built with Flask, featuring a dark glassmorphism UI with neon accents and animated modals.

![Uber Rides Predictor](https://img.shields.io/badge/Flask-2.3.3-red?style=for-the-badge&logo=flask)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange?style=for-the-badge&logo=scikit-learn)

## ✨ Features

### 🎨 **Ultra-Modern UI/UX**
- **Dark Glassmorphism Design** - Frosted glass effects with neon accents
- **Animated Background** - Floating particles and gradient animations
- **Modal Popup Results** - Stunning prediction results with success animations
- **Responsive Design** - Works perfectly on all devices
- **Custom Scrollbars** - Neon-styled scrollbars matching the theme

### 🔧 **Technical Features**
- **Machine Learning Integration** - Scikit-learn model for predictions
- **Real-time Validation** - Input validation with visual feedback
- **Loading States** - Smooth loading animations during prediction
- **Error Handling** - Comprehensive error handling and user feedback
- **RESTful API** - JSON API endpoint for external integrations

### 🛡️ **Security & Performance**
- **Input Validation** - Robust validation for all user inputs
- **Error Boundaries** - Graceful error handling and recovery
- **Logging** - Comprehensive logging for debugging
- **Production Ready** - Gunicorn configuration for deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/uber-rides-predictor.git
   cd uber-rides-predictor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🌐 Deployment

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI** and login
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### Option 2: Railway

1. **Connect your GitHub repository** to Railway
2. **Railway will automatically detect** the Flask app and deploy it
3. **No additional configuration needed**

### Option 3: Render

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service**
3. **Set build command**: `pip install -r requirements.txt`
4. **Set start command**: `gunicorn app:app`

## 📊 API Usage

### Prediction Endpoint
```bash
POST /api/predict
Content-Type: application/json

{
  "Priceperweek": 25,
  "Population": 1800000,
  "Monthlyincome": 5000,
  "Averageparkingpermonth": 96
}
```

### Response
```json
{
  "prediction": 1250,
  "status": "success",
  "message": "Prediction completed successfully"
}
```

### Health Check
```bash
GET /health
```

## 🎯 Input Parameters

| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| `Priceperweek` | Weekly price for rides ($) | 25 |
| `Population` | City population | 1800000 |
| `Monthlyincome` | Average monthly income ($) | 5000 |
| `Averageparkingpermonth` | Monthly parking cost ($) | 96 |

## 🎨 Design System

### Color Palette
- **Primary**: `#7877c6` (Neon Purple)
- **Secondary**: `#ff7bc4` (Neon Pink)
- **Success**: `#10b981` (Neon Green)
- **Background**: `#0f0f23` to `#16213e` (Dark Gradient)

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 400, 500, 600, 700, 800

### Components
- **Glassmorphism Cards** - Frosted glass effect with blur
- **Neon Buttons** - Gradient backgrounds with shimmer effects
- **Animated Modals** - Scale-in animations with backdrop blur
- **Floating Icons** - Subtle hover animations

## 🛠️ Development

### Project Structure
```
uber-rides-predictor/
├── app.py                 # Main Flask application
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version
├── static/
│   ├── style.css        # Ultra-modern CSS styles
│   └── script.js        # Interactive JavaScript
├── templates/
│   ├── index.html       # Main prediction interface
│   └── error.html       # Error page template
└── README.md            # This file
```

### Running Tests
```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Web framework
- **Scikit-learn** - Machine learning library
- **FontAwesome** - Icons
- **Google Fonts** - Typography
- **CSS Grid & Flexbox** - Layout system

## 📞 Support

If you have any questions or need help:
- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/uber-rides-predictor/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/uber-rides-predictor/discussions)

---

⭐ **Star this repository if you found it helpful!** 