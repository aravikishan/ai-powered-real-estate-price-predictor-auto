# AI-Powered Real Estate Price Predictor

## Overview
The AI-Powered Real Estate Price Predictor is an advanced web application designed to assist real estate investors, agents, and analysts in making informed decisions by predicting property prices. Utilizing historical data and AI algorithms, this application provides accurate price predictions based on property attributes such as location, size, number of bedrooms, and bathrooms. The tool is particularly beneficial for individuals and businesses looking to gain insights into property investments and market trends, offering a user-friendly interface to explore and analyze real estate data.

## Features
- **Real Estate Price Prediction**: Calculate estimated property prices using AI algorithms based on input parameters like location, size, bedrooms, and bathrooms.
- **Market Trends Visualization**: Access and visualize market trends for different locations using interactive charts.
- **Property Database Management**: Manage and view a database of properties with essential details and historical prices.
- **User-Friendly Interface**: Navigate through a clean and responsive interface designed for ease of use.
- **Contact and About Pages**: Learn more about the application and get in touch with the development team.
- **Static and Dynamic Content**: Serve static files and dynamic content through templating for an enriched user experience.

## Tech Stack
| Technology    | Description                                    |
|---------------|------------------------------------------------|
| Python        | Programming language used for backend logic    |
| FastAPI       | Web framework for building APIs                |
| Uvicorn       | ASGI server for running FastAPI applications   |
| Jinja2        | Templating engine for rendering HTML pages     |
| SQLite3       | Lightweight database for storing property data |
| Pydantic      | Data validation and settings management        |
| HTML/CSS/JS   | Frontend technologies for UI/UX design         |
| Docker        | Containerization for deployment                |

## Architecture
The application architecture consists of a FastAPI backend that serves both API endpoints and HTML pages using Jinja2 templates. The SQLite3 database is used to store property data and prediction results. Static files such as CSS and JavaScript are served to enhance the frontend experience.

```plaintext
+-------------------+
|   Frontend (UI)   |
+-------------------+
| - HTML Templates  |
| - CSS/JS Files    |
+-------------------+
         |
         v
+-------------------+
|  FastAPI Backend  |
+-------------------+
| - API Endpoints   |
| - Templating      |
+-------------------+
         |
         v
+-------------------+
|   SQLite3 DB      |
+-------------------+
| - Property Data   |
| - Predictions     |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-real-estate-price-predictor-auto.git
   cd ai-powered-real-estate-price-predictor-auto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit:
   ```
   http://localhost:8000
   ```

## API Endpoints
| Method | Path               | Description                                      |
|--------|--------------------|--------------------------------------------------|
| GET    | `/`                | Home page displaying the application overview    |
| GET    | `/predict`         | Page for predicting property prices              |
| GET    | `/market-trends`   | Page displaying market trends                    |
| GET    | `/about`           | Page with information about the application      |
| GET    | `/contact`         | Contact page for user inquiries                  |
| POST   | `/api/predict`     | API endpoint for predicting property prices      |
| GET    | `/api/properties`  | Retrieve a list of properties from the database  |
| GET    | `/api/trends`      | Retrieve market trends data                      |

## Project Structure
```
.
├── Dockerfile                 # Docker configuration file
├── app.py                     # Main application file with API logic
├── requirements.txt           # Python dependencies
├── start.sh                   # Shell script for starting the application
├── static                     # Static files directory
│   ├── css
│   │   └── style.css          # Main stylesheet for the application
│   ├── js
│   │   └── main.js            # Main JavaScript file for client-side logic
│   └── style.css              # Additional styling
├── templates                  # HTML templates directory
│   ├── about.html             # About page template
│   ├── contact.html           # Contact page template
│   ├── home.html              # Home page template
│   ├── market_trends.html     # Market trends page template
│   └── predict.html           # Predict price page template
└── real_estate.db             # SQLite3 database file
```

## Screenshots
![Home Page](screenshots/home.png)
![Predict Page](screenshots/predict.png)
![Market Trends Page](screenshots/market_trends.png)

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t real-estate-predictor .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 real-estate-predictor
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing coding standards and includes relevant tests.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.