from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Set up SQLite database
conn = sqlite3.connect("orders.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, symbol TEXT, price REAL, quantity INTEGER, order_type TEXT)")

@app.post("/orders")
async def create_order(symbol: str, price: float, quantity: int, order_type: str):
    cursor.execute("INSERT INTO orders (symbol, price, quantity, order_type) VALUES (?, ?, ?, ?)", (symbol, price, quantity, order_type))
    conn.commit()
    return {"message": "Order created"}

@app.get("/orders")
async def get_orders():
    cursor.execute("SELECT * FROM orders")
    orders = [{"id": row[0], "symbol": row[1], "price": row[2], "quantity": row[3], "order_type": row[4]} for row in cursor.fetchall()]
    return orders