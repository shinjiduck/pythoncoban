-- Câu 1: Mỗi quốc gia có bao nhiêu khách hàng?
SELECT Country, COUNT(CustomerId) AS so_khach
FROM Customer
GROUP BY Country
ORDER BY so_khach DESC;
-- Câu 2: 10 hóa đơn có giá trị lớn nhất là những hóa đơn nào?
SELECT TOP 10 InvoiceId, BillingCountry, Total
FROM Invoice
ORDER BY Total DESC;
-- Câu 3: Mỗi quốc gia có giá trị hóa đơn trung bình bao nhiêu? Làm tròn 2 chữ số, chỉ giữ những nước có từ 10 hóa đơn trở lên. Gợi ý: cần cả AVG, COUNT và HAVING.
SELECT BillingCountry, 
       ROUND(AVG (Total),2) AS Gia_tri_tb,
	   COUNT(InvoiceID) AS So_hoa_don
FROM dbo.Invoice
GROUP BY BillingCountry
HAVING COUNT(InvoiceID) >=10;
-- Câu 4: Bảng Track có cột Milliseconds là độ dài bài hát. Bài hát dài nhất là bài nào, dài bao nhiêu phút? Gợi ý: phút = mili giây / 60000.
SELECT TOP 1 Name, ROUND(Milliseconds / 60000.0, 2) AS Phut
FROM dbo.Track
ORDER BY Phut DESC
-- Câu hỏi hiểu bài: trả lời bằng lời của em, WHERE và HAVING khác nhau thế nào?.. WHERE lọc từng dòng, chạy trước khi gom nhóm, nên không dùng được SUM, COUNT, AVG. HAVING lọc từng nhóm, chạy sau GROUP BY, nên dùng được các hàm đó.
--Ví dụ: “chỉ tính hóa đơn trên 5 đô” dùng WHERE; “chỉ giữ những nước có tổng trên 100 đô” dùng HAVING.