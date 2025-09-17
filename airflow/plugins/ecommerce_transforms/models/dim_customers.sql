WITH customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

payments AS (
    SELECT
        order_id,
        SUM(payment_value) as total_order_value
    FROM {{ ref('stg_payments') }}
    GROUP BY 1
),

customer_orders AS (
    SELECT
        c.customer_unique_id,
        o.order_purchase_timestamp,
        p.total_order_value
        
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN payments p ON o.order_id = p.order_id

    WHERE o.order_status = 'delivered'
)

SELECT
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    
    MIN(co.order_purchase_timestamp) AS first_order_date,
    MAX(co.order_purchase_timestamp) AS most_recent_order_date,
    COUNT(co.order_purchase_timestamp) AS number_of_orders,
    SUM(co.total_order_value) AS lifetime_value

FROM customer_orders co
LEFT JOIN customers c ON co.customer_unique_id = c.customer_unique_id
GROUP BY 1, 2, 3 