# AI Chip Market Share Visualization

An interactive dashboard for visualizing the global market share distribution of AI chip manufacturers from 2015-2025, showing the evolution from general GPU market to AI-specific accelerators.

## Features

- **Interactive Year Range Selection**: Choose any range from 2015-2025
- **Multiple Chart Types**:
  - Bar Chart (grouped comparison)
  - Line Chart (trend analysis)
  - Pie Chart (latest year distribution)
  - Stacked Area Chart (cumulative view)
- **Dual Metrics**: View both market share percentage and revenue in billions USD
- **Market Evolution Visualization**: Clear visual distinction between general GPU era (2015-2017) and AI accelerator era (2019-2025)
- **Transition Marker**: Orange dashed line at 2018 marks the market shift on all time-series charts
- **Key Statistics**: Real-time metrics for major manufacturers
- **Data Table**: Detailed pivot table view
- **Reliable Data Sources**: Jon Peddie Research (2015-2017), TechInsights, IDC, Statista (2018+)

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

## Data Sources & Market Evolution

This application visualizes two distinct market periods:

### 2015-2017: General GPU Market
- **Source**: Jon Peddie Research discrete GPU market reports
- **Market**: Consumer/gaming GPUs, workstation GPUs, early machine learning
- **Key Event**: AMD peaked at 33.7% share in 2017 due to cryptocurrency mining boom

### 2018: Transition Year
- AI workloads began shifting from consumer GPUs to dedicated data center solutions
- NVIDIA's Tesla V100 and CUDA ecosystem established dominance in AI training

### 2019-2025: AI Accelerator Market
- **Sources**: TechInsights, IDC, Statista, Yole Group, Grand View Research
- **Market**: Data center AI chips, ML accelerators, training & inference hardware
- **Intel Entry**: Intel enters with Gaudi accelerators
- **AMD Pivot**: AMD shifts focus to MI-series data center accelerators

### Key Data Points:
- **2015-2017**: General GPU market ($5-8B), NVIDIA 66-81%, AMD 19-34%
- **2023**: $17.7B AI market (NVIDIA 65%, Intel 22%, AMD 11%) [TechInsights]
- **2024**: $50B+ market, NVIDIA 88-93% of server GPU revenue
- **2025**: $100B+ projected, NVIDIA 87%, AMD growing to 6.5%

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
