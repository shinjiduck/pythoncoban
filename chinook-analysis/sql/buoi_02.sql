SELECT TOP 5
       c.FirstName + ' ' + c.LastName AS ho_ten, -- Nối họ và tên
       c.Country,
       SUM(i.Total) AS tong_chi
FROM dbo.Customer AS c
INNER JOIN dbo.Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.FirstName, c.LastName, c.Country
ORDER BY tong_chi DESC;
SELECT t.TrackId, t.Name
FROM dbo.Track AS t
LEFT JOIN dbo.InvoiceLine AS il ON t.TrackId = il.TrackId
WHERE il.InvoiceLineId IS NULL;
-- Bài 1: Top 5 khách chi tiêu nhiều nhất: họ tên, quốc gia, tổng chi.
SELECT TOP 5
       c.FirstName + ' ' + c.LastName AS ho_ten,
	   c.Country,
	   SUM (i.Total) AS tong_chi
FROM dbo.Customer as c
INNER JOIN DBO.INVOICE AS i
ON c.CustomerId = i.CustomerId
Group by c.FirstName, c.LastName, c.Country
Order by tong_chi DESC
-- Bài 2: Mỗi nhân viên hỗ trợ phụ trách tổng doanh thu bao nhiêu? Gợi ý: Customer.SupportRepId nối với Employee.EmployeeId.
SELECT (e.FirstName + ' ' + e.LastName) AS ho_ten,
       SUM(i.Total) as Tong_Doanh_Thu
From dbo.Employee as e
Inner Join dbo.Customer AS c
ON c.SupportRepID = e.EmployeeId
Inner Join dbo.Invoice as i
On c.CustomerId = i.CustomerId
Group by e.FirstName, e.LastName
-- Bài 3: Top 5 nghệ sĩ có doanh thu cao nhất. Gợi ý đường đi: InvoiceLine → Track → Album → Artist.
SELECT TOP 5
       a.Name AS Nghe_si,
       SUM(inv.UnitPrice * inv.Quantity) AS Doanh_thu
FROM dbo.InvoiceLine AS inv
INNER JOIN dbo.Track  AS t  ON inv.TrackId = t.TrackId
INNER JOIN dbo.Album  AS al ON t.AlbumId   = al.AlbumId
INNER JOIN dbo.Artist AS a  ON al.ArtistId = a.ArtistId
GROUP BY a.Name
ORDER BY Doanh_thu DESC;
-- Câu 4: Có bao nhiêu bài hát chưa bán được lần nào? Chiếm bao nhiêu % tổng số bài?
SELECT COUNT(DISTINCT t.TrackId) AS Tong_bai,
       COUNT(DISTINCT il.TrackId) AS So_bai_da_ban,
       COUNT(DISTINCT t.TrackId) - COUNT(DISTINCT il.TrackId) AS So_bai_chua_ban,
       ROUND((COUNT(DISTINCT t.TrackId) - COUNT(DISTINCT il.TrackId)) * 100.0
             / COUNT(DISTINCT t.TrackId), 2) AS Ty_le_chua_ban_pct
FROM dbo.Track AS t
LEFT JOIN dbo.InvoiceLine AS il ON t.TrackId = il.TrackId;