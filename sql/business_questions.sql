-- Business questions for the Brazilian E-commerce Analytics project.
-- Database: data/database/olist_analytics.sqlite
-- Main table: orders_analytics

-- 1. How many orders exist by status?
SELECT
    order_status,
    COUNT(*) AS orders
FROM orders_analytics
GROUP BY order_status
ORDER BY orders DESC;

-- 2. What is the monthly evolution of delivered orders?
SELECT
    order_year_month,
    COUNT(*) AS delivered_orders,
    ROUND(SUM(product_revenue), 2) AS product_revenue
FROM orders_analytics
WHERE order_status = 'delivered'
GROUP BY order_year_month
ORDER BY order_year_month;

-- 3. Which product categories generate the most revenue?
SELECT
    main_category,
    COUNT(*) AS orders,
    ROUND(SUM(product_revenue), 2) AS product_revenue,
    ROUND(AVG(product_revenue), 2) AS average_order_revenue
FROM orders_analytics
WHERE order_status = 'delivered'
GROUP BY main_category
ORDER BY product_revenue DESC
LIMIT 10;

-- 4. Which states generate the most revenue?
SELECT
    customer_state,
    COUNT(*) AS orders,
    ROUND(SUM(product_revenue), 2) AS product_revenue,
    ROUND(AVG(product_revenue), 2) AS average_order_revenue
FROM orders_analytics
WHERE order_status = 'delivered'
GROUP BY customer_state
ORDER BY product_revenue DESC
LIMIT 10;

-- 5. Do late deliveries have lower review scores?
SELECT
    is_late,
    COUNT(*) AS orders,
    ROUND(AVG(review_score), 2) AS average_review_score,
    ROUND(AVG(delay_days), 2) AS average_delay_days
FROM orders_analytics
WHERE order_status = 'delivered'
  AND is_late IS NOT NULL
  AND review_score IS NOT NULL
GROUP BY is_late
ORDER BY is_late;

-- 6. Which categories have the highest late delivery rate?
SELECT
    main_category,
    COUNT(*) AS delivered_orders,
    ROUND(100.0 * SUM(CASE WHEN is_late = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS late_rate_pct,
    ROUND(AVG(review_score), 2) AS average_review_score
FROM orders_analytics
WHERE order_status = 'delivered'
  AND main_category IS NOT NULL
  AND main_category <> 'unknown'
GROUP BY main_category
HAVING delivered_orders >= 500
ORDER BY late_rate_pct DESC
LIMIT 10;

-- 7. What are the main payment types?
SELECT
    main_payment_type,
    COUNT(*) AS orders,
    ROUND(SUM(payment_value), 2) AS payment_value,
    ROUND(AVG(max_installments), 2) AS average_installments
FROM orders_analytics
WHERE order_status = 'delivered'
GROUP BY main_payment_type
ORDER BY orders DESC;

-- 8. What is the average delivery time by customer state?
SELECT
    customer_state,
    COUNT(*) AS delivered_orders,
    ROUND(AVG(delivery_days), 2) AS average_delivery_days,
    ROUND(AVG(delay_days), 2) AS average_delay_days,
    ROUND(AVG(review_score), 2) AS average_review_score
FROM orders_analytics
WHERE order_status = 'delivered'
  AND delivery_days IS NOT NULL
GROUP BY customer_state
ORDER BY average_delivery_days DESC;

