-- Write your SQL query here
SELECT
    name,
    price,
    price - (SELECT ROUND(AVG(price), 2) FROM products) AS vs_avg
FROM products
WHERE EXISTS (SELECT id FROM sales WHERE sales.product_id = products.id)
ORDER BY vs_avg DESC, name ASC;