# Hotel Revenue & Booking Analysis

## 📁 Project Overview

This project provides a comprehensive revenue and reservation analysis for **Highfield Hotel** using historical data exported from booking systems and internal revenue reports. The goal is to derive actionable insights to improve room profitability, understand booking patterns, and support data-driven decision-making.

---

## 🎯 Objectives

- Analyze room-wise profitability and occupancy.
- Identify high-performing and underperforming rooms.
- Understand booking patterns, cancellation trends, and guest behavior.
- Detect opportunities to optimize pricing or improve occupancy.
- Automate the monthly reporting process across Excel, Power BI, and Tableau.

---

## 🧩 Data Sources

- `room_income.csv`: Internal revenue and room utilization data.
- `bcom_data.csv`: External Booking.com reservation data (arrival, payment, commission).

Both are located in the `data/` folder.

---

## 📦 Project Structure

hotel_data_analysis/<br>
│<br>
|- data/ # Raw data (CSV)<br>
|── notebooks/ # Jupyter notebooks for data cleaning and analysis<br>
|── outputs/<br>
| |── reports/ # README, summary reports<br>
| |── graphs/ # Visualizations<br>
| |── excel/ # Excel dashboards<br>
|── dashboards/<br>
| |── power_bi/ # Power BI reports (.pbix)<br>
| |── tableau/ # Tableau workbook (.twbx)<br>
|── scripts/ # Automation scripts<br>

---

## 🛠️ Tools Used

- **Python (Pandas, Matplotlib, Seaborn, Plotly)** — For data wrangling and analysis
- **Excel** — Quick tabular dashboard and trend views
- **Power BI** — Interactive reporting
- **Tableau Public** — Visual storytelling
- **Jupyter Notebooks** — All cleaning and processing steps

---

## 📈 Key Insights Delivered

- Net profit per room and room type
- Commission losses and cancellation rate from Booking.com
- Revenue leakage patterns
- Room occupancy vs profitability heatmaps
- Recommendations for tariff optimization

---

## 🔁 Monthly Automation

- New data can be placed into the `data/` folder.
- Run the notebook or automation script (`scripts/monthly_refresh.py`) to regenerate dashboards and reports.
- Power BI and Tableau refresh templates link directly to processed Excel outputs.

---

## 📬 Contact

For improvements, issues or collaboration, please contact the data analytics team.

