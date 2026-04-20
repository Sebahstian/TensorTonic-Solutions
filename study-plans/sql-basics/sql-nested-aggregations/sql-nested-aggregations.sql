-- Write your SQL query here
WITH per_day AS (
    SELECT
        order_date,
        COUNT(*) as daily_count,
        SUM(amount) as daily_revenue
    FROM orders
    GROUP BY order_date
)

SELECT 
    ROUND(AVG(daily_count), 2) as avg_daily_orders,
    ROUND(AVG(daily_revenue), 2) as avg_daily_revenue,
    MAX(daily_count) as busiest_day_orders
FROM per_day;