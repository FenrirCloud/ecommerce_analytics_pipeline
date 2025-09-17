SELECT
    order_id,
    customer_id,
    order_status,
    TIMESTAMP(order_purchase_timestamp) as order_purchase_timestamp
FROM {{ source('raw_ecommerce', 'olist_orders_dataset') }}