--https://leetcode.com/problems/nth-highest-salary/

--https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver17
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
      SELECT DISTINCT top 1 salary FROM Employee ORDER BY salary DESC  OFFSET @N-1

    );
END