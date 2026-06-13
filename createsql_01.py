import mysql.connector

# 1. Configuration
config = {
    "host": "localhost",
    "user": "root",
    "password": "nizam07",
    "database": "office"
}

try:
    # Establishing the connection
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    
    
    cursor.execute("CREATE TABLE Customers (customer_id INT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount DECIMAL(10, 2), FOREIGN KEY (customer_id) REFERENCES Customers(customer_id))")

    
    cursor.execute("INSERT INTO Customers VALUES (1, 'Alice'), (2, 'Bob')")
    cursor.execute("INSERT INTO Orders VALUES (101, 1, 250.00), (102, 1, 50.00), (103, 2, 100.00)")
    
    conn.commit()  


    print("--- Joined Customer and Order Data ---")
    query = """
    SELECT Customers.name, Orders.order_id, Orders.amount
    FROM Customers
    INNER JOIN Orders ON Customers.customer_id = Orders.customer_id
    """
    cursor.execute(query)
    
    for (name, order_id, amount) in cursor.fetchall():
        print(f"Customer: {name} | Order: {order_id} | Amount: ${amount}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nConnection closed successfully.")