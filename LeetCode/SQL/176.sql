--https://leetcode.com/problems/second-highest-salary/description/

/* Write your T-SQL query statement below */
SELECT *, DENSE_RANK() OVER (
    PARTITION BY salary
    ORDER BY salary ASC 
) FROM Employee 