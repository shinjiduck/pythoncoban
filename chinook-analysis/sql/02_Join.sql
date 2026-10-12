-- Inner Join
SELECT i.InvoiceId, c.FirstName, c.LastName, i.Total
FROM dbo.Invoice AS i
INNER JOIN dbo.Customer AS c
    ON i.CustomerId = c.CustomerId;
    --On là điều kiện để nối bảng Invoice với bảng Customer
-- Join kết hợp Group By
SELECT TOP 5
       c.FirstName + ' ' + c.LastName AS ho_ten, -- Nối họ và tên
       c.Country,
       SUM(i.Total) AS tong_chi
FROM dbo.Customer AS c
INNER JOIN dbo.Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.FirstName, c.LastName, c.Country
ORDER BY tong_chi DESC;
-- Nối nhiều bảng liên tiếp
SELECT g.Name AS the_loai,
       SUM(il.UnitPrice * il.Quantity) AS doanh_thu
FROM dbo.InvoiceLine AS il
INNER JOIN dbo.Track AS t ON il.TrackId = t.TrackId
INNER JOIN dbo.Genre AS g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY doanh_thu DESC;
-- LEFT JOIN giữ toàn bộ bảng bên trái, dòng nào không có cặp thì phần bên phải để trống (NULL).
SELECT t.TrackId, t.Name
FROM dbo.Track AS t
LEFT JOIN dbo.InvoiceLine AS il ON t.TrackId = il.TrackId
WHERE il.InvoiceLineId IS NULL;