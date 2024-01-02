# Write your MySQL query statement below

WITH cte_rnk AS(
    SELECT d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        RANK() OVER(PARTITION BY d.name ORDER BY e.Salary DESC) AS rnk
    FROM Employee e
        INNER JOIN Department d
            ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM cte_rnk
WHERE rnk = 1
;
