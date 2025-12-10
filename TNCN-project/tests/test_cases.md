\# TEST THUẾ TNCN - CÁC TRƯỜNG HỢP KIỂM TRA



\## TEST 1: Không có thu nhập

\- \*\*Nhập:\*\* Tất cả tháng = 0, Phụ thuộc = 0

\- \*\*Kết quả đúng:\*\* Thuế = 0



\## TEST 2: Dưới ngưỡng giảm trừ  

\- \*\*Nhập:\*\* Mỗi tháng = 10,000,000, Phụ thuộc = 1

\- \*\*Kết quả đúng:\*\* Thuế = 0

\- \*\*Lý do:\*\* 10tr < (11tr + 4.4tr) = 15.4tr



\## TEST 3: Thu nhập 20 triệu/tháng

\- \*\*Nhập:\*\* Mỗi tháng = 20,000,000, Phụ thuộc = 0

\- \*\*Kết quả đúng:\*\* Thuế/tháng = 650,000

\- \*\*Tính:\*\* (5tr × 5%) + (4tr × 10%) = 250,000 + 400,000 = 650,000



\## TEST 4: Thu nhập cao 100 triệu

\- \*\*Nhập:\*\* Mỗi tháng = 100,000,000, Phụ thuộc = 0

\- \*\*Kết quả đúng:\*\* Tính theo bậc cao nhất 35%



\## TEST 5: Được hoàn thuế

\- \*\*Nhập:\*\* 

&nbsp; - Tháng 1-3: 50,000,000

&nbsp; - Tháng 4-12: 0

&nbsp; - Phụ thuộc: 1

\- \*\*Kết quả đúng:\*\* Được hoàn tiền



\## TEST 6: Phải nộp thêm

\- \*\*Nhập:\*\*

&nbsp; - Tháng 1-11: 10,000,000  

&nbsp; - Tháng 12: 100,000,000

&nbsp; - Phụ thuộc: 0

\- \*\*Kết quả đúng:\*\* Phải nộp thêm tiền

