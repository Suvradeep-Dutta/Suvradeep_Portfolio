CREATE TABLE SalesData (
  Date TEXT,
  Product TEXT,
  Category TEXT,
  Units_Sold INTEGER,
  Unit_Price FLOAT,
  Region TEXT
);

INSERT INTO SalesData (Date, Product, Category, Units_Sold, Unit_Price, Region) VALUES
('2024-01-05', 'Laptop', 'Electronics', 3, 70000.00, 'South'),
('2024-01-10', 'Mouse', 'Electronics', 10, 800.00, 'West'),
('2024-01-15', 'Pen', 'Stationery', 50, 10.00, 'East'),
('2024-01-22', 'Notebook', 'Stationery', 20, 50.00, 'North'),
('2024-02-01', 'Laptop', 'Electronics', 2, 72000.00, 'South'),
('2024-02-14', 'Mouse', 'Electronics', 15, 850.00, 'East'),
('2024-02-25', 'Pen', 'Stationery', 40, 12.00, 'West'),
('2024-03-01', 'Laptop', 'Electronics', 5, 69000.00, 'North'),
('2024-03-10', 'Notebook', 'Stationery', 10, 55.00, 'South'),
('2024-03-20', 'Pen', 'Stationery', 30, 11.00, 'East');