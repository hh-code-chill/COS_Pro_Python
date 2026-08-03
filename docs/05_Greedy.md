# Tham lam (Greedy)

## Lý thuyết

Thuật toán Tham lam chọn lựa phương án **TỐI ƯU CỤC BỘ** ở mỗi bước với hy vọng sẽ dẫn đến kết quả **TỐI ƯU TOÀN CỤC**. 

* **Cơ chế:** Tại mỗi thời điểm, đưa ra quyết định tốt nhất ngay lúc đó mà không cần quan tâm đến các bước trong tương lai.
* **Đặc điểm:** Thuật toán đơn giản, dễ cài đặt và tốc độ thực thi rất nhanh.
* **Hạn chế:** **Không phải lúc nào cũng cho kết quả đúng!** Thuật toán chỉ đúng khi bài toán thỏa mãn tính chất lựa chọn tham lam (*Greedy Choice Property*).

> ⚠️ **Lưu ý quan trọng:** Nếu thử nghiệm chiến thuật Tham lam trên các test case nhỏ mà cho ra kết quả sai, cần chuyển hướng ngay sang **Quy hoạch động (Dynamic Programming)** hoặc **Quay lui (Backtracking)**.

---

## Ví dụ minh họa

Cho số tiền cần đổi $780$ và hệ thống các mệnh giá tiền: $[500, 100, 50, 10]$. Tìm số lượng tờ tiền ít nhất để đổi đủ $780$.

* **Chiến thuật Tham lam:** Luôn ưu tiên chọn tờ tiền có **mệnh giá lớn nhất** có thể tại thời điểm đó.
* **Diễn biến từng bước:**
  * **Bước 1 (Mệnh giá 500):** $780 // 500 = 1$ tờ. Số tiền còn lại: $780 \pmod{500} = 280$.
  * **Bước 2 (Mệnh giá 100):** $280 // 100 = 2$ tờ. Số tiền còn lại: $280 \pmod{100} = 80$.
  * **Bước 3 (Mệnh giá 50):** $80 // 50 = 1$ tờ. Số tiền còn lại: $80 \pmod{50} = 30$.
  * **Bước 4 (Mệnh giá 10):** $30 // 10 = 3$ tờ. Số tiền còn lại: $30 \pmod{10} = 0$.

👉 **Kết quả:** Tổng số tờ tiền ít nhất là $1 + 2 + 1 + 3 = 7$ tờ.

### Code Python mẫu

```python
def min_coins_greedy(can, denominations):
    # Sắp xếp các mệnh giá theo thứ tự giảm dần
    denominations.sort(reverse=True)
    
    so_to = 0
    for m in denominations:
        if can == 0:
            break
        so_to += can // m   # Cộng số tờ lấy được từ mệnh giá m
        can %= m            # Cập nhật số tiền còn dư
        
    return so_to

# Chạy thử ví dụ
menh_gia = [500, 100, 50, 10]
tien_can_doi = 780
print("Số tờ tiền ít nhất:", min_coins_greedy(tien_can_doi, menh_gia))  # Output: 7
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Luôn tìm ra một **tiêu chí sắp xếp (Sorting key)** thích hợp để duyệt các phần tử và đưa ra lựa chọn tốt nhất ở từng bước.

### 1. Bài toán Đổi tiền / Rút tiền (Coin Change - Greedy Version)
Dạng bài cơ bản như ví dụ trên. Áp dụng chuẩn xác với hệ thống tiền tệ thực tế (nơi mệnh giá lớn luôn là bội số hoặc kết hợp tối ưu của mệnh giá nhỏ).

### 2. Bài toán Lập lịch công việc / Chọn khoảng không giao nhau (Interval Scheduling)
Cho danh sách $N$ cuộc họp với thời gian bắt đầu và kết thúc. Tìm số lượng cuộc họp nhiều nhất có thể tổ chức sao cho không cuộc họp nào bị trùng giờ.
* **Chiến thuật Tham lam:** Luôn ưu tiên chọn cuộc họp có **thời gian kết thúc sớm nhất**.

### 3. Bài toán Balo dạng phân số (Fractional Knapsack)
Cho các vật phẩm có trọng lượng và giá trị, có thể cắt nhỏ vật phẩm. Tìm cách chất hàng vào balo sao cho tổng giá trị lớn nhất mà không vượt quá trọng lượng $W$.
* **Chiến thuật Tham lam:** Sắp xếp các vật phẩm theo **đơn giá (giá trị / trọng lượng)** giảm dần và ưu tiên lấy vật phẩm có đơn giá cao nhất trước.

### 4. Bài toán Nối dây / Gom cụm tối ưu (Minimum Cost to Connect Ropes)
Cho $N$ sợi dây với độ dài khác nhau. Chi phí nối 2 sợi dây thành 1 là tổng độ dài của chúng. Tìm chi phí nhỏ nhất để nối tất cả thành 1 sợi.
* **Chiến thuật Tham lam:** Luôn chọn **2 sợi dây ngắn nhất** hiện tại để nối lại (kết hợp cấu trúc dữ liệu `Min Heap` / `Priority Queue`).

---

## 🚩 Dấu hiệu nhận biết bài toán Tham lam (Greedy)

Khi đọc đề bài, nên cân nhắc sử dụng Tham lam nếu xuất hiện các dấu hiệu:

1. Đề bài thuộc dạng **tối ưu hóa**: Yêu cầu tìm *"lớn nhất"*, *"nhỏ nhất"*, *"ít nhất"*, *"nhiều nhất"*.
2. Có thể dễ dàng xác định một **tiêu chí ưu tiên** (mệnh giá lớn nhất, thời gian kết thúc sớm nhất, đơn giá cao nhất...).
3. Dữ liệu bài toán thường **cần phải SẮP XẾP (Sorting)** trước khi tiến hành xử lý.
4. Lựa chọn ở bước hiện tại **không làm thay đổi hoặc ảnh hưởng tiêu cực** đến khả năng đưa ra lựa chọn ở các bước tiếp theo.

---

[⬅️ Quay lại trang chính README](../README.md)