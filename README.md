# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI input validation
- Structured project architecture
- Logging of API requests and responses

## Requirements
Python 3.x

Install dependencies:

pip install -r requirements.txt

## Usage

Example MARKET order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Example LIMIT order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000

## Project Structure

bot/
- client.py (Binance API wrapper)
- orders.py (order logic)
- validators.py (input validation)
- logging_config.py (logging)

cli.py – command line interface

## Logging

All API requests and responses are logged to:

trading_bot.log
