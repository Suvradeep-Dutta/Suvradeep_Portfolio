-- Createing a sales data table
CREATE TABLE SalesData (
  item TEXT, 
  category TEXT, 
  quantity TEXT, 
  price_per_unit FLOAT, 
  sale_date TEXT
  );
  
  -- Inserting elements in the table
  INSERT into SalesData (item, category, quantity, price_per_unit, sale_date)
  VALUES('Pen', 'Stationery', 10, 5.00, '2024-06-01'),
('Notebook', 'Stationery', 5, 20.00, '2024-06-03'),
('Pencil', 'Stationery', 15, 3.00, '2024-06-04'),
('Mouse', 'Electronics', 2, 500.00, '2024-06-05'),
('Keyboard', 'Electronics', 1, 1500.00, '2024-06-06'),
('Eraser', 'Stationery', 8, 2.50, '2024-06-07'),
('Charger', 'Electronics', 3, 700.00, '2024-06-07'),
('Pen', 'Stationery', 20, 5.00, '2024-06-08'),
('Mouse', 'Electronics', 1, 500.00, '2024-06-09'),
('Notebook', 'Stationery', 10, 20.00, '2024-06-10');