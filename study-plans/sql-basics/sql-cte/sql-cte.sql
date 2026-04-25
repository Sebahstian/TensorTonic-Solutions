-- Write your SQL query here
WITH customer_orders AS (
    SELECT
        customer,
        COUNT(order_date) AS order_count,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer    
)

SELECT *
FROM customer_orders
WHERE order_count > 1
ORDER BY total_spent DESC, customer ASC;