-- Case when if else trong SQL
SELECT InvoiceId, Total,
       CASE
           WHEN Total >= 15 THEN N'Lớn'
           WHEN Total >= 5  THEN N'Vừa'
           ELSE N'Nhỏ'
       END AS loai_hoa_don
FROM dbo.Invoice;
-- Hàm ngày tháng
SELECT YEAR(InvoiceDate) AS nam,
       SUM(Total) AS doanh_thu
FROM dbo.Invoice
GROUP BY YEAR(InvoiceDate)
ORDER BY nam;
-- Truy vấn con (subquery): câu hỏi lồng trong câu hỏi
SELECT InvoiceId, BillingCountry, Total
FROM dbo.Invoice
WHERE Total > (SELECT AVG(Total) FROM dbo.Invoice)
ORDER BY Total DESC;
--CTE (WITH): chia câu hỏi khó thành từng bước

Khi câu hỏi phức tạp, viết lồng nhiều lớp ngoặc rất khó đọc. CTE cho phép tính trước một bảng tạm, đặt tên, rồi dùng tiếp:

Câu hỏi: Có bao nhiêu khách ở mỗi hạng chi tiêu?
WITH chi_tieu AS (
    -- Bước 1: tính tổng chi của từng khách
    SELECT CustomerId, SUM(Total) AS tong_chi
    FROM dbo.Invoice
    GROUP BY CustomerId
)
-- Bước 2: phân hạng rồi đếm
SELECT CASE
           WHEN tong_chi >= 45 THEN N'VIP'
           WHEN tong_chi >= 38 THEN N'Thân thiết'
           ELSE N'Thường'
       END AS hang,
       COUNT(*) AS so_khach
FROM chi_tieu
GROUP BY CASE
           WHEN tong_chi >= 45 THEN N'VIP'
           WHEN tong_chi >= 38 THEN N'Thân thiết'
           ELSE N'Thường'
         END;
-- Tóm tắt khi nào dùng gì
--Câu hỏi có dạng	Dùng
--Thông tin nằm ở nhiều bảng	JOIN
--Cái gì chưa xảy ra	LEFT JOIN + IS NULL
--Phân loại, gắn nhãn	CASE WHEN
--So với trung bình / một con số tính trước	Subquery
--Câu hỏi nhiều bước	CTE (WITH)
--Xếp hạng, top N mỗi nhóm	RANK() + PARTITION BY
--So với kỳ trước, tăng trưởng	LAG()
--Chiếm bao nhiêu %	SUM() OVER ()