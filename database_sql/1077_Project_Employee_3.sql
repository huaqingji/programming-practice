# Write your MySQL query statement below
WITH cte AS(
    SELECT p.project_id, e.employee_id
        , RANK() OVER(PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS rnk
    FROM Project p
        INNER JOIN Employee e
            ON p.employee_id = e.employee_id
)
SELECT project_id, employee_id
FROM cte
WHERE rnk = 1
;