-- https://leetcode.com/problems/combine-two-tables/
/* Write your T-SQL query statement below */
SELECT P.lastName, p.firstName, ad.city, ad.state FROM Person P
left JOIN Address AD
on P.personId = AD.personID