# 🥤 FMCG AI Business Intelligence Assistant

## Overview

This project is an AI-powered Business Intelligence Assistant developed for the FMCG (Fast Moving Consumer Goods) Beverages domain.

The system helps business users obtain insights related to:

* Product Performance
* Regional Sales Comparison
* Promotion Effectiveness
* Inventory Stockouts

through a conversational interface, reducing dependency on manual reporting and dashboard creation.

---

## Business Problem

Business teams frequently require insights such as:

* Which products generate the highest revenue?
* Which promotions perform best?
* How do regions compare in sales?
* Are there any inventory stockouts?

Traditionally, these requests require analyst intervention and manual dashboard creation.

This solution provides a self-service analytics assistant for faster decision-making.

---

## Features

### Product Analysis

* Top Revenue Products
* Lowest Revenue Products

### Sales Analysis

* Regional Revenue Comparison

### Promotion Analysis

* Promotion Performance Evaluation

### Inventory Analysis

* Stockout Detection

### Dashboard Features

* KPI Cards
* Interactive Charts
* Download Results as CSV
* Conversational Query Interface

---

## Dataset

The project uses four synthetic FMCG datasets:

### Product Master

Contains beverage product information.

### Store Master

Contains store, city, and region information.

### Sales & Promotions

Contains weekly sales, promotions, revenue, and discounts.

### Inventory

Contains stock movement and stockout information.

---

## Technology Stack

* Python
* Pandas
* NumPy
* Streamlit

---

## Project Structure

```text
FMCG_AI_Assistant/
│
├── data/
│   ├── products.csv
│   ├── stores.csv
│   ├── sales.csv
│   └── inventory.csv
│
├── screenshots/
│
├── app.py
├── generate_data.py
├── requirements.txt
└── README.md
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Questions

* Which products generated highest revenue?
* Show lowest revenue products
* Compare regional sales
* Which promotion performed best?
* Show stockout analysis

---

## Future Enhancements

* LLM-based Natural Language Querying
* Demand Forecasting
* Automated Business Reports
* Real-Time Data Integration
* Cloud Deployment

---
## Streamlit App

https://fmcg-ai-business-assistant-ifz4ziudt6g3zgxgikp368.streamlit.app/

## Author

Sanjana Chinta

AI & ML Department

Chaitanya Bharathi Institute of Technology (CBIT)
