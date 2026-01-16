# Polymarket Trading Bot — Automated Market Maker for Prediction Markets

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Polymarket](https://img.shields.io/badge/Polymarket-Compatible-purple?style=for-the-badge)](https://polymarket.com)

**High-performance Python trading bot for Polymarket prediction markets with real-time WebSocket streaming, gasless transactions, and automated strategy execution.**

[Features](#features) • [Installation](#installation) • [Quick Start](#quick-start) • [Documentation](#documentation)

</div>

---

## 🎯 Overview

A production-ready trading solution designed for Polymarket's prediction markets. This bot provides institutional-grade tools for automated trading, market analysis, and portfolio management on the world's largest prediction market platform.

### Why This Bot?

- **Zero Gas Fees** — Native Builder Program integration eliminates transaction costs
- **Sub-second Execution** — WebSocket-based real-time market data streaming
- **Battle-tested Strategies** — Pre-built algorithms for various market conditions
- **Enterprise Security** — Bank-grade encryption for private key storage

## ✨ Features

### Core Trading Capabilities

| Feature | Description |
|---------|-------------|
| 🔄 **Real-time Data** | WebSocket streaming for live orderbook updates |
| ⚡ **Gasless Mode** | Zero transaction fees via Builder Program |
| 📊 **Multi-asset Support** | BTC, ETH, SOL, XRP 15-minute markets |
| 🛡️ **Encrypted Storage** | PBKDF2 + Fernet private key encryption |
| 📈 **Strategy Engine** | Modular architecture for custom strategies |
| 🎛️ **Risk Management** | Built-in take-profit and stop-loss controls |

### Pre-built Strategies

- **Volatility Trading** — Capitalizes on sudden probability movements
- **Orderbook Analysis** — Real-time market depth visualization
- **Custom Framework** — Easy-to-extend base classes for your strategies

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Polymarket account with configured wallet
- (Optional) Builder Program credentials for gasless trading

### Setup

Clone the repository using Git:
```bash
git clone https://github.com/winderi4/polymarket-bot-arbitrage
```

Install the required dependencies:
```bash
cd polymarket-bot-arbitrage
pip install -r requirements.txt
```

### Environment Configuration

Create environment variables for authentication:

```bash
export POLY_PRIVATE_KEY=your_wallet_private_key
export POLY_PROXY_WALLET=0xYourPolymarketProxyAddress
```

> 💡 **Finding Your Proxy Wallet**: Navigate to [polymarket.com/settings](https://polymarket.com/settings) to locate your proxy wallet address.

## 🚀 Quick Start

### Option 1: Market Viewer (Read-Only)

Monitor live orderbook data without any trading:

```bash
python apps/orderbook_viewer.py --coin ETH
```

<img width="690" height="476" alt="Orderbook Viewer Interface" src="https://github.com/user-attachments/assets/83621505-41e7-4b5a-90fd-3c84d1610291" />

*No credentials required — perfect for market analysis and research.*

### Option 2: Automated Trading

Execute the built-in volatility strategy:

```bash
python apps/flash_crash_runner.py --coin ETH
```

<img width="693" height="401" alt="Trading Strategy Interface" src="https://github.com/user-attachments/assets/d5ccffc8-20c5-4cd1-9c3d-679099b22899" />

*Requires `POLY_PRIVATE_KEY` and `POLY_PROXY_WALLET` environment variables.*

## 📖 Documentation

### Strategy Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--coin` | ETH | Target asset (BTC/ETH/SOL/XRP) |
| `--drop` | 0.30 | Trigger threshold for entry |
| `--size` | 5.0 | Position size in USDC |
| `--lookback` | 10 | Analysis window (seconds) |
| `--take-profit` | 0.10 | Profit target (USDC) |
| `--stop-loss` | 0.05 | Maximum loss limit (USDC) |

### Code Examples

#### Basic Integration

```python
from src import create_bot_from_env
import asyncio

async def main():
    bot = create_bot_from_env()
    orders = await bot.get_open_orders()
    print(f"Active orders: {len(orders)}")

asyncio.run(main())
```

#### Order Placement

```python
from src import TradingBot, Config

bot = TradingBot(
    config=Config(safe_address="0x..."),
    private_key="0x..."
)

result = await bot.place_order(
    token_id="...",
    price=0.65,
    size=10.0,
    side="BUY"
)
```

#### WebSocket Streaming

```python
from src.websocket_client import MarketWebSocket

ws = MarketWebSocket()
ws.on_book = lambda snapshot: print(f"Mid Price: {snapshot.mid_price:.4f}")
await ws.subscribe(["token_id"])
await ws.run()
```

## ⚙️ Configuration Reference

### Environment Variables

| Variable | Required | Description |
|----------|:--------:|-------------|
| `POLY_PRIVATE_KEY` | ✅ | Wallet private key for signing |
| `POLY_PROXY_WALLET` | ✅ | Polymarket proxy wallet address |
| `POLY_BUILDER_API_KEY` | ❌ | Builder Program API key |
| `POLY_BUILDER_API_SECRET` | ❌ | Builder Program API secret |
| `POLY_BUILDER_API_PASSPHRASE` | ❌ | Builder Program passphrase |

### YAML Configuration (Alternative)

```yaml
safe_address: "0xYourWalletAddress"
builder:
  api_key: "your_api_key"
  api_secret: "your_api_secret"
  api_passphrase: "your_passphrase"
```

Load with: `TradingBot(config_path="config.yaml", private_key="0x...")`

## 🔒 Security

This bot implements industry-standard security practices:

- **Key Encryption**: PBKDF2 with 480,000 iterations + Fernet symmetric encryption
- **Secure Storage**: Encrypted files with 0600 permissions
- **Best Practices**: Never commit `.env` files, use dedicated wallets

## 📁 Project Structure

```
├── src/                    # Core trading library
├── apps/                   # Entry points and strategies
├── lib/                    # Reusable utility components
└── config.yaml            # Configuration template
```

## 🔧 API Reference

### TradingBot Methods

- `place_order()` — Submit new orders
- `cancel_order()` — Cancel existing orders
- `get_open_orders()` — Retrieve active orders
- `get_trades()` — Fetch trade history
- `get_order_book()` — Get current orderbook
- `get_market_price()` — Current market price

### WebSocket Methods

- `subscribe()` — Subscribe to market feeds
- `run()` — Start WebSocket connection
- `disconnect()` — Clean disconnect
- `get_orderbook()` — Cached orderbook data
- `get_mid_price()` — Current mid price

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| Authentication errors | Verify `POLY_PRIVATE_KEY` and `POLY_PROXY_WALLET` |
| Invalid key format | Ensure 64 hex characters (0x prefix optional) |
| Order failures | Check wallet balance and market liquidity |
| Connection issues | Verify network and firewall settings |

## 🌐 Additional Resources

### Recommended Infrastructure

For optimal performance, consider using a VPS close to Polymarket's servers:

**Trading VPS**: [@TradingVps](https://app.tradingvps.io/aff.php?aff=57)

<img width="890" height="595" alt="VPS Dashboard" src="https://github.com/user-attachments/assets/72966dac-3faa-4e93-941e-a34026d59822" />

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is provided for educational and research purposes. Trading on prediction markets involves financial risk. Always conduct your own research and never trade with funds you cannot afford to lose.

---

<div align="center">

**Questions or Feedback?**

Telegram: [@Vladmeer](https://t.me/vladmeer67) • Twitter: [@Vladmeer](https://x.com/vladmeer67)

</div>