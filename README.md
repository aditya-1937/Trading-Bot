# Binance Futures Testnet Trading Bot

## Setup
pip install -r requirements.txt

Create .env file:
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Features
- Market & Limit Orders
- CLI validation
- Logging
- Clean structure
