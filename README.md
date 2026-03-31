# Cyber-Threat-Intelligence-Attack-Surface-Analysis-Using-Shodan-and-Splunk
📌 Overview

This project analyzes cyber exposure in war-affected countries using Shodan and Splunk.

🎯 Features
Country-based cyber exposure analysis
Open port and service detection
Vulnerability (CVE) analysis
Splunk dashboards for visualization
🛠 Technologies Used
Python
Shodan API
Splunk
Pandas
⚙️ Setup Instructions
1. Install Dependencies

pip install shodan pandas

2. Add API Key

Replace YOUR_API_KEY in the script.

3. Run Data Collection

python data_collection.py

4. Convert Data

python convert_to_csv.py

5. Upload to Splunk
Add data input
Select CSV file
Set sourcetype as CSV
📊 Splunk Queries

Example:
index=cyber_threat | stats count by country

📈 Results
Identified high-risk ports (22, 23, 3389)
Found vulnerable systems across multiple countries
Observed patterns linked to geopolitical conflicts
⚠️ Disclaimer

This project uses publicly available data from Shodan and is intended for educational purposes only.

👨‍💻 Author

Manav Vaidya
