# Property Data Automation System

A Python automation solution built with Playwright that automatically collects, organizes, and exports real estate property data into structured Excel and CSV reports.

This project demonstrates how automation can reduce manual data entry, improve data organization, and save valuable staff time for real estate organizations.

---

## Business Problem

Many real estate companies spend hours manually copying property information into spreadsheets or updating listings across different platforms.

This repetitive process can lead to:

- Time-consuming manual work
- Data entry errors
- Inconsistent property records
- Difficulty maintaining organized property data
- Reduced staff productivity

---

## Solution

This automation system visits property listing pages, extracts essential property information, and automatically generates organized Excel and CSV reports.

Instead of manually collecting property information, staff receive structured data ready for analysis or further processing.

---

## Features

- Automatically collects property listings
- Extracts:
  - Property Title
  - Price
  - Location
  - Bedrooms
  - Bathrooms
  - Property Size
  - Property URL
- Exports data to Excel
- Exports data to CSV
- Handles multiple property pages automatically
- Includes error handling to continue scraping if one page fails

---

## Business Benefits

This solution helps real estate organizations by:

✅ Reducing repetitive manual work

✅ Saving staff time

✅ Organizing property data into structured reports

✅ Minimizing manual data entry errors

✅ Making property information easier to analyze

---

## Technologies Used

- Python
- Playwright
- OpenPyXL
- CSV
- Regular Expressions (re)

---

## Sample Output

### Excel Output
![Excel Output](ecommerce.png)

### CSV Output

![CSV Output](csv.png)

---

## Project Structure

```
real-estate-scraper/
│
├── scraper.py
├── README.md
├── requirements.txt
├── sample_output.xlsx
├── sample_output.csv
├── excel.png
├── csv.png
└── .gitignore
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run the scraper:

```bash
python scraper.py
```

---

## Future Improvements

- Export data directly into a SQL database
- Schedule automatic daily scraping
- Email generated reports automatically
- Build a web dashboard for viewing reports
- Detect duplicate property listings
- Generate summary reports

---

## Disclaimer

This project was developed for educational and portfolio purposes using publicly accessible demonstration content. Always ensure that automated data collection complies with the target website's Terms of Service and applicable laws before scraping production websites.

---

## Author

PeterCodx

Python Automation & Web Scraping Developer

Helping businesses automate repetitive tasks and transform web data into actionable insights.
