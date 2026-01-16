# AI Chip Market Share Visualization

An interactive dashboard for visualizing the global market share distribution of AI chip manufacturers over multiple years.

## Features

- **Interactive Year Range Selection**: Choose any range from 2020-2025
- **Multiple Chart Types**:
  - Bar Chart (grouped comparison)
  - Line Chart (trend analysis)
  - Pie Chart (latest year distribution)
  - Stacked Area Chart (cumulative view)
- **Dual Metrics**: View both market share percentage and revenue in billions USD
- **Key Statistics**: Real-time metrics for major manufacturers
- **Data Table**: Detailed pivot table view
- **Reliable Data Sources**: Compiled from TechInsights, IDC, Statista, and other industry analysts

## Installation

1. Clone this repository:
```bash
git clone https://github.com/WinstonOswald/AI-chip-market-share.git
cd AI-chip-market-share
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Controls

- **Year Range Slider**: Select the time period you want to analyze
- **Chart Type Dropdown**: Choose your preferred visualization style
- **Metric Radio Buttons**: Toggle between market share % and revenue
- **Show Data Table**: Checkbox to display raw data

## Data Sources

This application uses curated data from:
- **TechInsights**: Data-Center AI Chip Market Reports
- **Statista**: AI chip revenue analysis
- **IDC**: AI Infrastructure market research
- **Yole Group**: Semiconductor trends
- **Market Research Firms**: Grand View Research, Precedence Research

### Key Data Points:
- 2023: $17.7B market (NVIDIA 65%, Intel 22%, AMD 11%)
- 2024: NVIDIA captured 93% of server GPU revenue
- 2025: NVIDIA projected at 86-92% AI GPU market share

## Technologies Used

- **Streamlit**: Interactive web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive charting library

## Project Structure

```
AI-chip-market-share/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Screenshots

The dashboard includes:
- Key statistics cards showing current market positions
- Interactive charts with manufacturer-specific color coding
- Responsive layout that works on different screen sizes

## Contributing

Feel free to open issues or submit pull requests with improvements or updated data.

## License

This project is for educational purposes. Market data compiled from publicly available analyst reports.

## Disclaimer

Market share data is compiled from various public sources and represents estimates. Actual figures may vary depending on market definition (discrete GPUs vs. total AI infrastructure) and reporting methodology.
