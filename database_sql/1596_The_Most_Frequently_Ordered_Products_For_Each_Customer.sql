# Write your MySQL query statement below

WITH cte AS (
    SELECT o.customer_id
        , o.product_id
        , p.product_name
        , DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rnk
    FROM Orders o
        INNER JOIN Products p
            ON o.product_id = p.product_id
    GROUP BY o.customer_id, o.product_id, p.product_name
)
SELECT customer_id, product_id, product_name
FROM cte
WHERE rnk = 1
;