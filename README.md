# Climate Data Dashboard

## 🌐 Live Demo

**View the live dashboard:** [Climate Data Dashboard](https://python-climate-dashboard.kokud.dev)

## Features
A data visualization dashboard built with Python and Dash to explore CO2 emissions and greenhouse gas data worldwide.

## Features

- Interactive CO2 emission trends visualization
- Greenhouse gases analysis
- Sector-wise emission breakdown
- Country-specific data comparison
- Temperature change visualization
- Responsive design with Tailwind CSS

## Tech Stack

- Python 3.12
- Dash
- Plotly
- Pandas
- Gunicorn
- Tailwind CSS
- Docker
- GitHub Actions

## Getting Started

### Prerequisites

- Python 3.12
- Docker (optional)

### Local Development

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run the application for development:
```sh
python main.py
```
4. Open http://localhost:8050 in your browser

### Docker Deployment
Build and run with Docker:
```sh
docker-compose up --build
```

## Project Structure
```
/Project
├── main.py         # Main application entry point
├── pages/          # Dashboard page components
├── components/     # Reusable UI components
├── data/           # Data loading and processing
└── assets/         # static assets and styles
```

### CI/CD
The project uses GitHub Actions for:
- Automated builds
- Container publishing to GitHub Container Registry
- Deployment to Docker Swarm

## Data Source
Data is sourced from Our World in Data CO2 dataset: https://github.com/owid/co2-data/blob/master/owid-co2-data.csv

## Screenshots

| View | Description |
|------|-------------|
| ![Home Page](https://github.com/user-attachments/assets/220e5e44-35ca-438f-84ce-70d59707d46d) | Home page |
| ![CO2 Emissions Trends](https://github.com/user-attachments/assets/22cee862-89bf-45ba-900f-0a235b7eb65c) | Global CO2 emissions trends visualization with interactive timeline |
| ![Greenhouse Gas Analysis](https://github.com/user-attachments/assets/92f1cc2e-6003-4437-9415-386143e31ba8) | Breakdown of different greenhouse gases and their contributions |

## Author
Konrad Kudlak

## License
This project is open source and available under the MIT License.

