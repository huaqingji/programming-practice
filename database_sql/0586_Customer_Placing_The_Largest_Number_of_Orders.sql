# Write your MySQL query statement below

WITH cte_cnt AS(
    SELECT customer_number, COUNT(order_number) AS cnt
    FROM Orders
    GROUP BY customer_number
    ORDER BY cnt DESC
    LIMIT 1
)
SELECT customer_number
FROM cte_cnt
;