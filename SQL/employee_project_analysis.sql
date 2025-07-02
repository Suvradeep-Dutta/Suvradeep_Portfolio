/* -------------------------------------------------------------
   EMPLOYEE & PROJECT ANALYSIS – 10 INTERVIEW‑STYLE QUERIES
   Table: EmployeeProjects
   ------------------------------------------------------------- */


/* 1. Total number of employees in the dataset */
SELECT COUNT(DISTINCT employee_id)  FROM EmployeeData;

/* 2. Total salary paid per department */
SELECT department, SUM(salary) as total_salary
from EmployeeData
group by department;

/* 3. Average salary of employees per project */
SELECT project, ROUND(AVG(salary),2) as avg_salary
from EmployeeData
GROUP by project;

/* 4. Number of employees in each department */
SELECT department, COUNT(DISTINCT employee_id) as total_employees
FROM EmployeeData
GROUP by department
ORDER by total_employees DESC;

/* 5. Top 3 highest‑paid employees */
SELECT *
from EmployeeData
ORDER by salary DESC
limit 3;

/* 6. Total number of projects handled by each department */
SELECT department, COUNT(DISTINCT project) as projects_handled
from EmployeeData
GROUP by department;

/* 7. Employees working on more than 2 projects */
SELECT employee_id, employee_name, COUNT(DISTINCT project) as project_count
from EmployeeData
GROUP by employee_name
HAVING project_count > 2
order by project_count DESC;

/* 8. Total salary paid per project */
SELECT project, SUM(salary) as total_salary
FROM EmployeeData
GROUP by project
order by total_salary DESC;

/* 9. Employees with salary above their department average */
WITH dep_avg as(
  select DISTINCT department as dep, AVG(salary) AS avg_salary
  from EmployeeData
  GROUP BY department
  )
  SELECT employee_id, employee_name, dep, salary
  from EmployeeData
  inner JOIN dep_avg
  on department= dep
  WHERE salary > avg_salary
  order by salary desc;
  
  /* 10. Department with the highest total salary payout */
  SELECT department, SUM(salary) as total_salary
  from EmployeeData
  group by department
  ORDER by total_salary desc
  limit 1;