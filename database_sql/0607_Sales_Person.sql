# Write your MySQL query statement below

WITH cte_ord AS(
    SELECT o.order_id, o.sales_id
    FROM Orders o
        INNER JOIN Company c
            ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
SELECT sp.name
FROM SalesPerson sp
    LEFT OUTER JOIN cte_ord AS o
        ON sp.sales_id = o.sales_id
WHERE o.sales_id IS NULL
;