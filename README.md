# TFL-Tube-Line-Status-Monitoring-System

## Overview
The **TFL Tube Line Status Monitoring System** is a real-time data processing and visualization solution that fetches tube line status information from the Transport for London (TFL) API. This system aggregates and analyzes data, storing it in a ClickHouse database, and provides real-time insights into the status of various tube lines, including disruptions, delays, and service performance. The project leverages OLAP techniques for efficient querying and reporting.

## Key Features
- **Real-Time ETL Pipeline**: Automatically fetches tube line status data from the TFL API, transforms the data, and loads it into ClickHouse for efficient storage and querying.
- **OLAP Analysis**: Uses OLAP techniques to enable fast querying and aggregation of tube line disruptions and delays across multiple time periods.
- **Data Visualization**: Visualizes tube line status trends in real-time using Matplotlib, helping users track disruptions, delays, and service performance over time.
- **Logging & Error Handling**: Includes a robust logging system to capture and alert for any issues during data fetching, insertion, or visualization.

## Technologies Used
- **Python**: Main programming language for fetching, processing, and visualizing the data.
- **ClickHouse**: OLAP database for storing and querying large datasets efficiently.
- **Matplotlib**: For creating real-time visualizations of tube line status trends.
- **Requests**: For fetching real-time tube line status data from the TFL API.
- **Logging**: For tracking errors and ensuring smooth execution of the pipeline.
- **Pandas**: For data manipulation and cleaning before insertion into the ClickHouse database.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tfl-tube-line-status-monitoring.git
   cd tfl-tube-line-status-monitoring
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up a ClickHouse instance:

Install and run ClickHouse locally or use a remote instance.

Update the Clickhouse.py file with your database connection details.

Run the script to start fetching and visualizing the data:

bash
Copy
Edit
python main.py

Transport-for-London-Tube-Line-Status-Monitoring-System/
│
├── Clickhouse.py              # Defines the ClickHouse client, database connection setup, and schema.
├── Data_Insertion.py          # Handles the insertion of fetched tube line status data into the ClickHouse database.
├── Fetch_Data.py              # Contains the function to fetch data from the TFL API.
├── Main.py                    # Main script that ties together the ETL pipeline, querying, and data visualization.
├── Plot_data.py               # Contains the function to generate real-time visualizations using Matplotlib.
├── Query_Data.py              # Contains the function to query the ClickHouse database for analysis.
├── Query_TLF_Status.py        # Query script to manually fetch and analyze tube line status data from ClickHouse.
├── README.md                  # Project overview, setup instructions, and usage guide.
└── requirements.txt           # Lists the dependencies needed to run the project.


Example Output
Once the system is running, you will see real-time visualizations of tube line status. The graphs will show the status of each tube line over time, with numerical status values representing different levels of service disruptions (e.g., Good Service, Minor Delays, Severe Delays).

Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
TFL API for providing real-time tube line status data.

ClickHouse for efficient OLAP database management and fast querying.

Matplotlib for creating real-time visualizations.

