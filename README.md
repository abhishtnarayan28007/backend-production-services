# 📊 Project 1: Market Harvester & Resilient ETL Pipeline

An automated Extraction, Transformation, and Loading (ETL) pipeline built with **Python** to ingest raw market telemetry, sanitize noisy and corrupted datasets, handle missing values gracefully, and export structured operational reports.

---

## 🚀 Key Features

* **Automated Data Extraction**: Parses raw market data feeds and structured JSON payloads dynamically.
* **Resilient Data Transformation**: Cleans missing fields, handles data type mismatches, and filters corrupted records without halting pipeline execution.
* **Dual Output Architecture**: Generates clean structured JSON datasets (`actionable_market_data.json`) alongside human-readable audit summaries (`harvest_summary.txt`).
* **System Logging & Auditing**: Writes operational telemetry and pipeline activity directly to disk (`pipeline.log`) for tracking pipeline performance over time.
* **Fault-Tolerant File I/O**: Safe handling of missing inputs or unexpected raw data formats using standard Python error handling.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Data Processing**: Standard JSON, File I/O, Custom Data Cleaners
* **Logging & Telemetry**: Standard Python Logging (`FileHandler` + `StreamHandler`)

---------------------------------------------------------

# ⚔️ Project 2 - Deadpool Real-Time Webhook Alert Engine

A high-performance asynchronous webhook processor built with **FastAPI** and **Pydantic**. This engine receives real-time event telemetry from external clients, validates payload schemas, logs system audits, and dispatches dynamic alerts to a custom Telegram channel.

---

## 🚀 Key Features

* **Real-Time Webhook Ingestion**: Ingests HTTP POST JSON events dynamically.
* **Data Validation**: Strict schema enforcement using Pydantic models.
* **Telegram Integration**: Dynamic message formatting and automated dispatch.
* **Production Logging**: Dual-stream logging (Console + File Audit) with UTF-8 encoding support.
* **Error & Network Resiliency**: Explicit HTTP status modeling (`502 Bad Gateway`, `500 Internal Server Error`) with configurable request timeouts.
* **Traffic Simulator Included**: Standalone client testing script to simulate multi-priority enterprise payloads.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI / Uvicorn
* **Data Validation**: Pydantic
* **HTTP Client**: Requests
* **Logging**: Standard Python Logging (`FileHandler` + `StreamHandler`)

### 1. Download Project Files
```bash
git clone https://github.com/abhishtnarayan28007/Python-Automation-Gauntlet.git
cd Python-Automation-Gauntlet/capstone_projects
```

## 🌐 Live Service

The application is deployed on Railway and active 24/7.

* **Base URL**: `https://backend-production-services-production.up.railway.app`
* **Health Check**: `GET /`
* **Alert Webhook**: `POST /webhook/alert`

### 🧪 Webhook Example Payload

Send a `POST` request to `https://backend-production-services-production.up.railway.app/webhook/alert` with the following JSON body:

```json
{
  "event_id": "EVT-1234",
  "source": "Stripe",
  "priority": "HIGH",
  "message": "High volume of failed transactions."
}
```

