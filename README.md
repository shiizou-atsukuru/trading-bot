# Binance Futures: Order Management System (OMS)
**Developed by Yash Verma**

A professional-grade trading bot and dashboard for Binance Futures. This system provides a robust **Order Management System (OMS)** that allows traders to stage, review, and bulk-execute orders via a web interface or a command-line tool.

## Features

* **Dual-Interface Control**:
* **Web Dashboard**: A modern Streamlit UI for visual order management.
* **CLI Tool**: A high-speed Typer-based interface for terminal power users.


* **Order Staging**: Add orders manually or via CSV to a "Staging Area" to review before hitting the market.
* **Bulk Execution**: Import complex trade lists via CSV and execute them sequentially with real-time status tracking.
* **Automated Audit Trail**: Every request, response, and error is timestamped and logged to a persistent file.
* **Dockerized Infrastructure**: Fully containerized for "one-command" setup and environment consistency.
* **Persistent Logging**: Uses volume mapping to ensure trading history survives container restarts.

---

## Project Architecture

The project follows a modular design to ensure the trading logic is separated from the user interface:

* **`ui.py`**: The Streamlit web dashboard.
* **`cli.py`**: The Typer command-line interface.
* **`bot/`**: Core logic folder.
* `orders.py`: Contains the actual Binance API execution logic.
* `logger.py`: Self-initializing logging system with configurable levels.
* `client.py`: Binance API client initialization.
* `validators.py`: Pre-trade input validation.



---

## Installation & Setup

### 1. Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
* Binance Testnet API Key and Secret.

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here

```

### 3. Launch the System

Build and start the OMS Dashboard:

```bash
docker compose up --build

```

Once the build finishes, access the UI at: **`http://localhost:8501`**

---

## Usage Guide

### Using the Web Dashboard (OMS)

1. **Manual Entry**: Use the "+ Add Manual Order" expander to stage individual trades.
2. **CSV Import**: Upload a CSV with headers `symbol,side,type,quantity,price`.
3. **Execution**: Review the "Staged Orders" table. Click **EXECUTE** to process all orders sequentially.
4. **Logs**: Monitor the sidebar "Live Feed" for real-time API feedback. Use the "Clear Log File" button to reset the history.

### Using the CLI

To execute a single trade without launching the UI:

```bash
docker compose run --rm trading-bot python cli.py BTCUSDT BUY MARKET 0.002

```

---

## CSV Format Example

To bulk import orders, use a `.csv` file with the following structure:

symbol,side,type,quantity,price


> **Note**: For `MARKET` orders, the `price` column should be left empty.

---

## Persistent Data

This project uses **Persistent Volume Mapping**. Your logs are stored in:

* **Internal**: `/app/logs/trading_bot.log`
* **Host (Your PC)**: `./logs/trading_bot.log`

Even if you delete the Docker container, your trade history remains safe in the `./logs` folder.

---