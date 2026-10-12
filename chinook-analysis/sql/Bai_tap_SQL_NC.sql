--Câu 1: Phân hạng khách theo tổng chi tiêu (em tự đặt mốc sau khi xem dữ liệu), đếm số khách mỗi hạng.
SELECT c.CustomerId,
       c.FirstName + ' ' + c.LastName AS Ho_ten,
       SUM(i.Total) AS Tong_chi,
	   Case 
	   when SUM(i.Total) >= 45 then N'VIP'
	   when SUM(i.Total) > 40 then N'Tầm trung'
	   Else 'Nhỏ'
	   end as Loai_khach_hang
FROM dbo.Customer AS c
INNER JOIN dbo.Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName
ORDER BY Tong_chi DESC;
-- Câu 2: Doanh thu theo năm và % tăng trưởng so với năm trước
WITH tong_doanhthu AS (
    SELECT YEAR(InvoiceDate) AS Nam,
           SUM(Total) AS DoanhThu
    FROM dbo.Invoice
    GROUP BY YEAR(InvoiceDate)
)
SELECT Nam,
       DoanhThu,
       LAG(DoanhThu) OVER (ORDER BY Nam) AS Nam_truoc,
       ROUND((DoanhThu - LAG(DoanhThu) OVER (ORDER BY Nam)) * 100.0
             / LAG(DoanhThu) OVER (ORDER BY Nam), 2) AS Tang_truong_pct
FROM tong_doanhthu
ORDER BY Nam;
--Câu 3:Thể loại bán chạy nhất ở mỗi quốc gia là gì? Gợi ý: giống ví dụ “khách chi nhiều nhất mỗi nước”, nhưng thay khách bằng thể loại.
Select g.Name,
       i.BillingCountry,
	   Sum(ivl.UnitPrice * ivl.Quantity) as Doanh_thu,
	   RANK () OVER (PARTITION BY i.BillingCountry
	                 Order by SUM(ivl.UnitPrice * ivl.Quantity) desc) as hang
From Invoice as i
Inner join InvoiceLine as ivl
ON i.InvoiceId = ivl.InvoiceId
Inner Join Track as t
ON ivl.TrackId = t.TrackId
Inner join Genre as g
ON g.GenreId = t.GenreId
Group by g.Name,i.BillingCountry;