# 📊 AI Sales Data Analyzer

A beginner-friendly sales data analysis project built using **Python, NumPy, Pandas, and Excel**.

This project takes raw sales data, cleans and analyzes it using Python, and exports the results into a structured multi-sheet Excel workbook.

## 🎯 Project Objective

The goal of this project is to analyze sales data and identify useful business insights such as:

* Which regions generate the most revenue?
* Which sales representatives perform best?
* Which product categories generate the highest sales?
* Which customer types contribute the most revenue?
* Which sales channels perform best?
* Which payment methods are most commonly used?
* How do discounts affect sales performance?
* What is the overall sales performance?

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Excel**
* **Git & GitHub**

## 📁 Project Structure

```text
sales_project/
│
├── 1_main.py
├── 2_Data_Cleaning.py
├── data/
│   └── sales_data.csv
├── Sales_Data_Pipeline_Dashboard.xlsx
├── .gitignore
└── README.md
```

## 🔄 Project Workflow

```text
Raw Sales Dataset
       ↓
Data Cleaning
       ↓
Data Transformation
       ↓
Exploratory Data Analysis
       ↓
Business Insights
       ↓
Excel Export
       ↓
GitHub
```

## 🧹 Data Cleaning

The project performs several data-cleaning steps using Pandas and NumPy, including:

* Standardizing column names
* Handling missing values
* Converting data types
* Parsing sales dates
* Removing invalid sales records
* Checking quantities and sales values
* Creating useful analysis columns

## 📊 Analysis Performed

### 1. Regional Performance

Analyzes total sales and contribution by region.

### 2. Sales Representative Performance

Identifies the highest-performing sales representatives based on total sales and other sales metrics.

### 3. Product Category Performance

Analyzes:

* Total revenue
* Total quantity sold
* Average sale
* Best-performing category
* Lowest-performing category

### 4. Customer Type Analysis

Compares sales performance between different customer types and calculates their contribution to total revenue.

### 5. Sales Channel Analysis

Compares sales channels using:

* Total sales
* Total quantity sold
* Average sale
* Revenue contribution

### 6. Payment Method Analysis

Analyzes sales performance across different payment methods.

### 7. Discount Strategy Analysis

Separates discounted and full-price orders to compare:

* Total revenue
* Average order value
* Total units sold

### 8. Overall Sales Summary

Calculates:

* Total accumulated revenue
* Total physical units sold
* Average transaction value

## 📗 Excel Output

The analysis results are exported into:

**`Sales_Data_Pipeline_Dashboard.xlsx`**

The workbook contains separate sheets for the major analyses, making the results easier to review and use for further Excel visualization.

## 📌 Dataset

The dataset was obtained from Kaggle and is licensed under **CC0: Public Domain**.

The dataset is used for educational and portfolio purposes.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/ayushigabani-bot/AI-Sales-Data-Analyzer.git
```

### 2. Open the project

```bash
cd AI-Sales-Data-Analyzer
```

### 3. Install required libraries

```bash
pip install pandas numpy openpyxl
```

### 4. Run the Python project

```bash
python 2_Data_Cleaning.py
```

The analysis will process the sales dataset and generate the Excel output.

## 📈 Key Skills Demonstrated

This project demonstrates practical experience with:

* Python programming
* NumPy
* Pandas
* Data cleaning
* Data transformation
* `groupby()`
* `agg()`
* Sorting
* Filtering
* `iloc`
* `loc`
* `idxmax()` and `idxmin()`
* Data aggregation
* Business-oriented data analysis
* Excel data export
* Git and GitHub

## 👩‍💻 Author

**Ayushi Gabani**

Aspiring Data Analyst / Data Science learner.

This project was created as part of my practical learning journey in Python, Pandas, NumPy, Excel, and data analysis.
