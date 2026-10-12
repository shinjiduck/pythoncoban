Select * from Customer
--Lấy tất cả từ bảng customer
Where Country = 'Brazil'
--Điều kiện where khi country = "Brazil"
WHERE Country IN ('USA', 'Canada', 'Brazil')    -- thuộc danh sách
WHERE Total BETWEEN 5 AND 10                    -- trong khoảng
WHERE FirstName LIKE 'M%'                       -- tên bắt đầu bằng M
WHERE BillingState IS NULL                      -- ô bị trống
Order by Total Desc
--Sắp xếp theo Total desc là giảm sdaanf
limit 5;
--limit là lấy giới hạn top 5
--Phẩy chấm ; là kết thúc câu
--Gom nhóm BillingCountry
SELECT BillingCountry, SUM(Total) AS doanh_thu
FROM Invoice
GROUP BY BillingCountry
ORDER BY doanh_thu DESC
LIMIT 5;
-- Nhóm dữ liệu có cùng giá trị khi dùng với các hàm: Count(), Max(), Min(), Sum(), AVG()
