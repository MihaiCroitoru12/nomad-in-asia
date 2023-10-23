# Weather ETL Script

This script performs an Extract, Transform, and Load (ETL) process for weather data.

## Workflow Overview

1. **Extraction**: The Python script uses [OpenWeatherMap API](https://openweathermap.org/api) to pull real-time weather data

2. **Transformation**: While the majority of the data remains unaltered, minor adjustments and formatting are performed within the script to make the data compatible for storage and further analysis. Additionally, I've integrated weather alerts to enhance the information value.

3. **Loading**: The data is stored in a PostgreSQL database on AWS EC2, ensuring secure cloud-based storage.

4. **Automation**: The script's operation is automated to run hourly using a Task Scheduler. This approach ensures that the Power BI dashboard is fueled by the most up-to-date information.

5. **Visualization**: Using the data I've stored, I've designed a Power BI dashboard for report insights and weather alerts.

## Technical Specifications

- **Python**: Serves as the backbone, driving the ETL process.
  
- **OpenWeatherMap API**: The chosen source for real-time weather data. 

- **PostgreSQL on AWS EC2**: I established a virtual machine on AWS EC2, where I implemented a PostgreSQL database, essential for handling the live data I use.

## Access Note
Note that the database is currently set to limited access for security reasons.

