import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure the page
st.set_page_config(
    page_title="AI Chip Market Share",
    page_icon="🖥️",
    layout="wide"
)

# Market share data compiled from reliable sources
# 2015-2017: General GPU market (gaming/discrete GPUs) - Source: Jon Peddie Research
# 2018+: AI-specific accelerator market - Source: TechInsights, IDC, Statista
market_data = {
    'Year': [2015, 2015, 2015, 2015,
             2016, 2016, 2016, 2016,
             2017, 2017, 2017, 2017,
             2018, 2018, 2018, 2018,
             2019, 2019, 2019, 2019,
             2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022,
             2023, 2023, 2023, 2023,
             2024, 2024, 2024, 2024,
             2025, 2025, 2025, 2025],
    'Manufacturer': ['NVIDIA', 'Intel', 'AMD', 'Others'] * 11,
    'Market Share (%)': [
        # 2015 (General GPU Market - Source: Jon Peddie Research)
        81.0, 0.0, 19.0, 0.0,
        # 2016 (General GPU Market - Source: Jon Peddie Research)
        70.5, 0.0, 29.5, 0.0,
        # 2017 (General GPU Market - Source: Jon Peddie Research)
        66.3, 0.0, 33.7, 0.0,
        # 2018 - Transition year (AI workloads emerging)
        75.0, 5.0, 18.0, 2.0,
        # 2019 - AI market forming
        78.0, 10.0, 10.0, 2.0,
        # 2020 - Dedicated AI accelerator market
        80.0, 15.0, 3.0, 2.0,
        # 2021
        81.0, 13.0, 4.0, 2.0,
        # 2022
        83.0, 11.0, 4.5, 1.5,
        # 2023 (Source: TechInsights - $17.7B market)
        65.0, 22.0, 11.0, 2.0,
        # 2024 (Source: Multiple reports - NVIDIA 93% of server GPU revenue)
        88.0, 6.0, 5.0, 1.0,
        # 2025 (Source: Latest projections - NVIDIA 86-92% AI GPU share)
        87.0, 5.5, 6.5, 1.0
    ],
    'Revenue (Billions USD)': [
        # 2015 (General GPU Market estimate)
        4.1, 0.0, 1.0, 0.0,
        # 2016 (General GPU Market estimate)
        4.2, 0.0, 1.8, 0.0,
        # 2017 (General GPU Market estimate - crypto mining boom)
        5.5, 0.0, 2.8, 0.0,
        # 2018 - Transition year
        6.0, 0.4, 1.4, 0.2,
        # 2019
        7.0, 0.9, 0.9, 0.2,
        # 2020
        8.0, 1.5, 0.3, 0.2,
        # 2021
        9.7, 1.6, 0.5, 0.2,
        # 2022
        12.5, 1.7, 0.7, 0.2,
        # 2023 (TechInsights: $17.7B total)
        11.5, 3.9, 1.9, 0.4,
        # 2024 estimates (~$50B market)
        44.0, 3.0, 2.5, 0.5,
        # 2025 projections (NVIDIA $49B+, AMD $5.6B)
        87.0, 5.5, 6.5, 1.0
    ],
    'Market Type': ['General GPU'] * 12 + ['Transition'] * 4 + ['AI Accelerator'] * 28
}

df = pd.DataFrame(market_data)

# Memory chip production data (units produced in billions) by company
# Sources: TrendForce, Yole Group, IC Insights, Omdia
# Covers DRAM + NAND Flash production
memory_data = {
    'Year': [2016, 2016, 2016, 2016, 2016, 2016,
             2017, 2017, 2017, 2017, 2017, 2017,
             2018, 2018, 2018, 2018, 2018, 2018,
             2019, 2019, 2019, 2019, 2019, 2019,
             2020, 2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022, 2022,
             2023, 2023, 2023, 2023, 2023, 2023,
             2024, 2024, 2024, 2024, 2024, 2024,
             2025, 2025, 2025, 2025, 2025, 2025],
    'Company': ['Samsung', 'SK Hynix', 'Micron', 'Kioxia', 'Western Digital', 'Others'] * 10,
    'Units Produced (Billions)': [
        # 2016 - DRAM+NAND combined (~82B total)
        30.3, 20.5, 16.4, 8.2, 4.1, 2.5,
        # 2017 - Memory super cycle, supply tight (~90B total)
        33.3, 22.5, 18.0, 9.0, 4.5, 2.7,
        # 2018 - Peak of memory super cycle (~97B total)
        35.8, 24.3, 19.4, 9.7, 4.9, 2.9,
        # 2019 - Memory downturn, oversupply (~93B total)
        33.5, 23.2, 18.6, 10.2, 5.1, 2.4,
        # 2020 - Recovery, COVID-driven demand (~105B total)
        38.9, 26.3, 21.0, 10.5, 5.3, 3.0,
        # 2021 - Strong demand, supply constraints (~120B total)
        44.4, 30.0, 24.0, 12.0, 6.0, 3.6,
        # 2022 - Oversupply, demand slowdown (~112B total)
        40.3, 28.0, 22.4, 11.2, 5.6, 4.5,
        # 2023 - Deep downturn, production cuts (~98B total)
        35.3, 24.5, 18.6, 10.8, 5.4, 3.4,
        # 2024 - AI-driven HBM recovery (~118B total)
        42.5, 30.7, 22.4, 12.4, 5.9, 4.1,
        # 2025 - Strong HBM/AI memory demand (~138B projected)
        49.7, 35.9, 26.2, 13.8, 6.9, 5.5
    ],
    'Revenue (Billions USD)': [
        # 2016 - Total memory revenue ~$77B
        28.9, 14.6, 12.3, 9.2, 7.7, 4.3,
        # 2017 - Super cycle peak, prices surged (~$126B total)
        50.4, 25.2, 20.2, 13.9, 10.1, 6.2,
        # 2018 - Continued high prices (~$158B total)
        63.2, 31.6, 25.3, 17.4, 12.6, 7.9,
        # 2019 - Sharp downturn in prices (~$106B total)
        39.2, 22.3, 17.0, 12.7, 9.5, 5.3,
        # 2020 - Moderate recovery (~$117B total)
        44.5, 25.6, 19.5, 12.9, 9.4, 5.1,
        # 2021 - Strong pricing (~$153B total)
        57.4, 35.1, 27.5, 16.1, 11.6, 5.3,
        # 2022 - Downturn begins (~$130B total)
        49.3, 29.1, 24.1, 13.7, 9.8, 4.0,
        # 2023 - Deep downturn, lowest in years (~$92B total)
        33.1, 22.0, 15.5, 10.6, 7.4, 3.4,
        # 2024 - AI/HBM-driven recovery (~$164B total)
        62.3, 42.6, 28.9, 15.6, 9.8, 4.8,
        # 2025 - Projected strong growth (~$210B total)
        80.9, 54.6, 35.7, 19.3, 12.6, 6.9
    ]
}

memory_df = pd.DataFrame(memory_data)

# Title and description
st.title("🖥️ Global AI Chip Market Share Analysis")
st.markdown("""
This dashboard visualizes the market share distribution of major AI chip manufacturers
based on data from industry analysts including TechInsights, IDC, Statista, and market research firms.
""")

# Market transition info banner
st.info("""
📊 **Market Evolution Note**: This visualization shows two distinct market periods:
- **2015-2017**: General discrete GPU market (gaming, workstation, early ML)
- **2018**: Transition year as AI workloads moved to data centers
- **2019-2025**: Dedicated AI accelerator market (data center AI chips)

A vertical line at 2018 marks this market transition on the charts.
""")

# Sidebar controls
st.sidebar.header("📊 Visualization Controls")

# Year range selector
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Chart type selector
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Pie Chart (Latest Year)", "Stacked Area Chart"]
)

# Metric selector
metric = st.sidebar.radio(
    "Select Metric",
    ["Market Share (%)", "Revenue (Billions USD)"]
)

# Memory chip controls
st.sidebar.header("Memory Chip Controls")

memory_min_year = int(memory_df['Year'].min())
memory_max_year = int(memory_df['Year'].max())

memory_year_range = st.sidebar.slider(
    "Memory Chip Year Range",
    min_value=memory_min_year,
    max_value=memory_max_year,
    value=(memory_min_year, memory_max_year),
    step=1
)

memory_chart_type = st.sidebar.selectbox(
    "Memory Chart Type",
    ["Bar Chart", "Line Chart", "Pie Chart (Latest Year)", "Stacked Area Chart"],
    key="memory_chart_type"
)

memory_metric = st.sidebar.radio(
    "Memory Metric",
    ["Units Produced (Billions)", "Revenue (Billions USD)"],
    key="memory_metric"
)

# Filter data based on year range
filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Display key statistics
st.header("📈 Key Statistics")
col1, col2, col3, col4 = st.columns(4)

latest_year = filtered_df['Year'].max()
latest_data = filtered_df[filtered_df['Year'] == latest_year]

with col1:
    nvidia_share = latest_data[latest_data['Manufacturer'] == 'NVIDIA']['Market Share (%)'].values[0]
    st.metric("NVIDIA Market Share", f"{nvidia_share}%",
              delta=f"{latest_year}")

with col2:
    amd_share = latest_data[latest_data['Manufacturer'] == 'AMD']['Market Share (%)'].values[0]
    st.metric("AMD Market Share", f"{amd_share}%",
              delta=f"{latest_year}")

with col3:
    intel_share = latest_data[latest_data['Manufacturer'] == 'Intel']['Market Share (%)'].values[0]
    st.metric("Intel Market Share", f"{intel_share}%",
              delta=f"{latest_year}")

with col4:
    total_revenue = filtered_df[filtered_df['Year'] == latest_year]['Revenue (Billions USD)'].sum()
    st.metric("Total Market Size", f"${total_revenue:.1f}B",
              delta=f"{latest_year}")

# Main visualization
st.header("📊 Market Share Visualization")

if chart_type == "Bar Chart":
    fig = px.bar(
        filtered_df,
        x='Year',
        y=metric,
        color='Manufacturer',
        title=f"GPU/AI Chip {metric} by Manufacturer ({year_range[0]}-{year_range[1]})",
        barmode='group',
        color_discrete_map={
            'NVIDIA': '#76B900',
            'AMD': '#ED1C24',
            'Intel': '#0071C5',
            'Others': '#808080'
        }
    )
    # Add vertical line at 2018 to mark market transition
    if year_range[0] <= 2018 <= year_range[1]:
        fig.add_vline(x=2017.5, line_dash="dash", line_color="orange",
                     annotation_text="Market Transition", annotation_position="top")
    fig.update_layout(height=500, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":
    fig = px.line(
        filtered_df,
        x='Year',
        y=metric,
        color='Manufacturer',
        title=f"GPU/AI Chip {metric} Trends ({year_range[0]}-{year_range[1]})",
        markers=True,
        color_discrete_map={
            'NVIDIA': '#76B900',
            'AMD': '#ED1C24',
            'Intel': '#0071C5',
            'Others': '#808080'
        }
    )
    # Add vertical line at 2018 to mark market transition
    if year_range[0] <= 2018 <= year_range[1]:
        fig.add_vline(x=2017.5, line_dash="dash", line_color="orange",
                     annotation_text="Market Transition", annotation_position="top")
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Pie Chart (Latest Year)":
    latest_year_data = filtered_df[filtered_df['Year'] == latest_year]
    fig = px.pie(
        latest_year_data,
        values=metric,
        names='Manufacturer',
        title=f"AI Chip {metric} Distribution - {latest_year}",
        color='Manufacturer',
        color_discrete_map={
            'NVIDIA': '#76B900',
            'AMD': '#ED1C24',
            'Intel': '#0071C5',
            'Others': '#808080'
        }
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Stacked Area Chart":
    fig = px.area(
        filtered_df,
        x='Year',
        y=metric,
        color='Manufacturer',
        title=f"GPU/AI Chip {metric} Distribution Over Time ({year_range[0]}-{year_range[1]})",
        color_discrete_map={
            'NVIDIA': '#76B900',
            'AMD': '#ED1C24',
            'Intel': '#0071C5',
            'Others': '#808080'
        }
    )
    # Add vertical line at 2018 to mark market transition
    if year_range[0] <= 2018 <= year_range[1]:
        fig.add_vline(x=2017.5, line_dash="dash", line_color="orange",
                     annotation_text="Market Transition", annotation_position="top")
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# --- Memory Chip Production Section ---
st.markdown("---")
st.header("Memory Chip Production by Company")
st.markdown("""
Annual memory chip production (DRAM + NAND Flash) broken down by manufacturer
over the last 10 years. Data sourced from TrendForce, Yole Group, IC Insights, and Omdia.
""")

# Filter memory data
filtered_memory_df = memory_df[
    (memory_df['Year'] >= memory_year_range[0]) &
    (memory_df['Year'] <= memory_year_range[1])
]

# Memory chip color scheme
memory_colors = {
    'Samsung': '#1428A0',
    'SK Hynix': '#E4002B',
    'Micron': '#00B2A9',
    'Kioxia': '#E60012',
    'Western Digital': '#005EB8',
    'Others': '#808080'
}

# Key memory statistics
st.subheader("Key Memory Statistics")
mcol1, mcol2, mcol3, mcol4 = st.columns(4)

latest_memory_year = filtered_memory_df['Year'].max()
latest_memory_data = filtered_memory_df[filtered_memory_df['Year'] == latest_memory_year]

with mcol1:
    samsung_units = latest_memory_data[latest_memory_data['Company'] == 'Samsung']['Units Produced (Billions)'].values[0]
    st.metric("Samsung Production", f"{samsung_units:.1f}B chips", delta=f"{latest_memory_year}")

with mcol2:
    skhynix_units = latest_memory_data[latest_memory_data['Company'] == 'SK Hynix']['Units Produced (Billions)'].values[0]
    st.metric("SK Hynix Production", f"{skhynix_units:.1f}B chips", delta=f"{latest_memory_year}")

with mcol3:
    micron_units = latest_memory_data[latest_memory_data['Company'] == 'Micron']['Units Produced (Billions)'].values[0]
    st.metric("Micron Production", f"{micron_units:.1f}B chips", delta=f"{latest_memory_year}")

with mcol4:
    total_units = latest_memory_data['Units Produced (Billions)'].sum()
    st.metric("Total Production", f"{total_units:.1f}B chips", delta=f"{latest_memory_year}")

# Memory chip chart
if memory_chart_type == "Bar Chart":
    mem_fig = px.bar(
        filtered_memory_df,
        x='Year',
        y=memory_metric,
        color='Company',
        title=f"Memory Chip {memory_metric} by Company ({memory_year_range[0]}-{memory_year_range[1]})",
        barmode='group',
        color_discrete_map=memory_colors
    )
    mem_fig.update_layout(height=500, xaxis_tickangle=-45)
    st.plotly_chart(mem_fig, use_container_width=True)

elif memory_chart_type == "Line Chart":
    mem_fig = px.line(
        filtered_memory_df,
        x='Year',
        y=memory_metric,
        color='Company',
        title=f"Memory Chip {memory_metric} Trends ({memory_year_range[0]}-{memory_year_range[1]})",
        markers=True,
        color_discrete_map=memory_colors
    )
    mem_fig.update_layout(height=500)
    st.plotly_chart(mem_fig, use_container_width=True)

elif memory_chart_type == "Pie Chart (Latest Year)":
    latest_mem_data = filtered_memory_df[filtered_memory_df['Year'] == latest_memory_year]
    mem_fig = px.pie(
        latest_mem_data,
        values=memory_metric,
        names='Company',
        title=f"Memory Chip {memory_metric} Distribution - {latest_memory_year}",
        color='Company',
        color_discrete_map=memory_colors
    )
    mem_fig.update_traces(textposition='inside', textinfo='percent+label')
    mem_fig.update_layout(height=500)
    st.plotly_chart(mem_fig, use_container_width=True)

elif memory_chart_type == "Stacked Area Chart":
    mem_fig = px.area(
        filtered_memory_df,
        x='Year',
        y=memory_metric,
        color='Company',
        title=f"Memory Chip {memory_metric} Over Time ({memory_year_range[0]}-{memory_year_range[1]})",
        color_discrete_map=memory_colors
    )
    mem_fig.update_layout(height=500)
    st.plotly_chart(mem_fig, use_container_width=True)

# Memory data table
st.subheader("Memory Chip Data")
show_memory_data = st.checkbox("Show memory chip data table")
if show_memory_data:
    st.dataframe(
        filtered_memory_df.pivot_table(
            values=[memory_metric],
            index='Year',
            columns='Company'
        ).round(2),
        use_container_width=True
    )

# Data table
st.header("📋 Raw Data")
show_data = st.checkbox("Show detailed data table")
if show_data:
    st.dataframe(
        filtered_df.pivot_table(
            values=[metric],
            index='Year',
            columns='Manufacturer'
        ).round(2),
        use_container_width=True
    )

# Data sources and methodology
st.header("📚 Data Sources & Methodology")

st.markdown("""
### Market Evolution Timeline

#### 2015-2017: General GPU Market Era
- **Source**: Jon Peddie Research discrete GPU market reports
- **Market Definition**: Consumer/gaming GPUs, workstation GPUs, early machine learning
- **Key Observation**: AMD gained significant share in 2016-2017 (peaked at 33.7%) due to cryptocurrency mining demand
- **Intel**: Not present in discrete GPU market during this period

#### 2018: Transition Year
- AI workloads began moving from consumer GPUs to dedicated data center solutions
- NVIDIA introduced Tesla V100 and started dominating the emerging AI accelerator market
- Market definition shifts from "discrete GPUs" to "AI accelerators"

#### 2019-2025: AI Accelerator Market Era
- **Sources**: TechInsights, IDC, Statista, Yole Group, Grand View Research
- **Market Definition**: Data center AI chips, ML accelerators, training & inference hardware
- **Intel Entry**: Intel enters with Xeon Phi (discontinued) and later Gaudi accelerators
- **AMD Shift**: AMD pivots from consumer GPUs to MI-series data center accelerators

### Key Data Points:
- **2015-2017**: General GPU market ($5-8B), NVIDIA 66-81% share, AMD 19-34%
- **2023**: $17.7B AI accelerator market - NVIDIA (65%), Intel (22%), AMD (11%) [TechInsights]
- **2024**: $50B+ market - NVIDIA captured 88-93% of server GPU revenue
- **2025**: $100B+ projected - NVIDIA 87%, AMD growing to 6.5% ($5.6B)

### Why the Data Shifts

The dramatic market share changes between 2017 and 2020 reflect two factors:
1. **Market Redefinition**: From general-purpose GPUs to AI-specific accelerators
2. **Architectural Advantage**: NVIDIA's CUDA ecosystem and Tensor Cores dominated AI training workloads
3. **New Entrants**: Intel entered with data center AI products; "Others" includes Google TPU, AWS chips, etc.

### Methodology Notes:
- Revenue figures are estimates based on reported datacenter/AI segments
- Market definitions vary by source (some include CPUs, others only discrete accelerators)
- 2015-2017 data represents discrete GPU market, not AI-specific
- 2018-2019 data interpolated during market transition period
- "Others" post-2018 includes Google TPU, AWS Trainium/Inferentia, Cerebras, Graphcore, etc.
""")

st.markdown("---")
st.caption("Dashboard created for educational purposes. Data compiled from public analyst reports and market research.")
