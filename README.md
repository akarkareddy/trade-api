# Trade API
A simple API for trade orders.

## Setup
1. Clone: `git clone <repo-url>`
2. Run: `docker build -t trade-api . && docker run -p 8000:8000 trade-api`

## Endpoints
- POST `/orders`: {"symbol": "AAPL", "price": 150.5, "quantity": 10, "order_type": "buy"}
- GET `/orders`: List all orders
