/* ------------------------------------------------------------
   SALES ANALYSIS QUERIES  –  Suvradeep Portfolio
   Table: SalesData (Date TEXT, Product TEXT, Category TEXT,
                     Units_Sold INTEGER, Unit_Price REAL, Region TEXT)
   ------------------------------------------------------------ */



/* 1. Total GMV (Gross Merchandise Value) */
SELECT SUM(unit_sold * unit_price) AS total_gmv FROM SalesData;

/* 2. Top 3 products by GMV */
SELECT product, SUM(unit_sold * unit_price) as gmv from SalesData
GROUP BY product 
ORDER by gmv DESC 
LIMIT 3;

/* 3. Monthly GMV (Jan, Feb, Mar) */
SELECT strftime('%Y-%m', date) as month,
SUM(unit_sold * unit_price) as gmv
FROM SalesData
GROUP by month
order by month;

/* 4. Region with highest units sold */
SELECT region, SUM(unit_sold) as total_units_sold
FROM SalesData
GROUP by region
order by total_units_sold DESC
limit 1;

/* 5. Average unit price per category */
SELECT category, AVG(unit_price) as avg_price FROM SalesData
GROUP by category
ORDER by avg_price desc;

/* 6. Daily sales trend for “Laptop” product */
SELECT date, SUM(unit_sold * unit_price) as daily_sales from SalesData
WHERE product like 'Laptop'
group by date
ORDER by date;

/* 7. Percentage share of each region in overall GMV */
WITH region_gvm as(
  SELECT region, SUM(unit_sold * unit_price) AS gvm
  FROM SalesData
  GROUP by region
  )
  SELECT region, gvm, 100* gvm/ (SELECT SUM(gvm) from region_gvm) as percentage_share
  from region_gvm
  order by percentage_share DESC;

/* 8. Month‑over‑month GMV growth (%) Jan→Feb, Feb→Mar */
WITH MOM AS(
  SELECT strftime('%Y-%m', date) as month,
  SUM(unit_sold * unit_price) as gvm
  from SalesData
  GROUP BY month
  )
  SELECT month, gvm,
  100* (gvm-LAG(gvm) OVER( ORDER by month))/LAG(gvm) OVER(ORDER by month) as mom_growth_percent
        from MOM
        ORDER BY month;
        

/* 9. Products that sold fewer than 50 total units */
SELECT product, SUM(unit_sold) as total_units_sold
from SalesData
GROUP by product
HAVING total_units_sold < 50
order by total_units_sold;

/* 10. Day with highest single‑day GMV */
SELECT date, SUM(unit_sold * unit_price) as daily_gvm
from SalesData
group by date
order by daily_gvm desc
limit 1;

  