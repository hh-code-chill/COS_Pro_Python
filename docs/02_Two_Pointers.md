# Hai con trỏ (Two Pointers)

## Lý thuyết

Sử dụng hai chỉ số (con trỏ) cùng di chuyển quét trên mảng **ĐÃ SẮP XẾP** để tìm cặp phần tử hoặc đoạn thỏa mãn điều kiện (thường là tổng), giúp tránh việc sử dụng hai vòng lặp lồng nhau.

* **Cách đặt vị trí:** Con trỏ `trai` ở đầu mảng, con trỏ `phai` ở cuối mảng.
* **Cơ chế dịch chuyển:**
  * Nếu `tổng < target`: Tổng hiện tại đang nhỏ, cần tăng tổng $\rightarrow$ dời con trỏ `trai` sang phải (`trai += 1`).
  * Nếu `tổng > target`: Tổng hiện tại đang lớn, cần giảm tổng $\rightarrow$ dời con trỏ `phai` sang trái (`phai -= 1`).
  * Nếu `tổng == target`: Tìm thấy cặp thỏa mãn $\rightarrow$ dừng vòng lặp hoặc lưu kết quả.
* **Tối ưu:** Giảm độ phức tạp thời gian từ $O(n^2)$ xuống $O(n)$.

---

## Ví dụ minh họa

Cho mảng đã sắp xếp: $a = [1, 2, 4, 7, 11]$ và $target = 9$.

* **Khởi tạo:** `trai = 0` ($a[0] = 1$), `phai = 4` ($a[4] = 11$).
* **Diễn biến từng bước:**
  * **Bước 1:** $s = 1 + 11 = 12 > 9 \rightarrow$ Tổng quá lớn, dời `phai` sang trái (`phai = 3`, $a[3] = 7$).
  * **Bước 2:** $s = 1 + 7 = 8 < 9 \rightarrow$ Tổng quá nhỏ, dời `trai` sang phải (`trai = 1`, $a[1] = 2$).
  * **Bước 3:** $s = 2 + 7 = 9 == 9 \rightarrow$ Tìm thấy cặp thỏa mãn tại vị trí $(1, 3)$. Dừng!

### Code Python mẫu

```python
def two_sum_sorted(a, target):
    trai = 0
    phai = len(a) - 1
    
    while trai < phai:
        s = a[trai] + a[phai]
        if s == target:
            return [trai, phai]  # Trả về chỉ số của cặp số
        elif s < target:
            trai += 1
        else:
            phai -= 1
            
    return []  # Không tìm thấy
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Tận dụng tính chất đã sắp xếp của dữ liệu để loại bỏ bớt các trường hợp không cần thiết, giúp duyệt mảng chỉ trong một lần ($O(n)$).

### 1. Tìm cặp số có tổng bằng $K$ (Two Sum II)
Dạng bài cơ bản nhất như ví dụ trên. Cho mảng đã sắp xếp, tìm vị trí 2 số có tổng đúng bằng $K$.
* **Độ phức tạp:** $O(n)$ thời gian, $O(1)$ bộ nhớ phụ.

### 2. Bài toán 3 số / 4 số có tổng bằng $K$ (3Sum / 4Sum)
Cho mảng chưa sắp xếp, tìm tất cả các bộ 3 số $(a, b, c)$ có tổng bằng $0$ (hoặc $K$).
* **Cách giải:** Sắp xếp mảng trước $O(n \log n)$. Dùng 1 vòng lặp cố định phần tử thứ nhất, sau đó dùng kỹ thuật Two Pointers cho 2 phần tử còn lại.
* **Tối ưu:** Giảm độ phức tạp từ $O(n^3)$ xuống $O(n^2)$.

### 3. Kiểm tra chuỗi đối xứng (Valid Palindrome) / Đảo ngược mảng
Kiểm tra xem một chuỗi có đọc giống nhau từ trái sang phải và từ phải sang trái không.
* **Cách làm:** `trai` xuất phát từ chỉ số $0$, `phai` xuất phát từ cuối chuỗi. So sánh $a[trai]$ và $a[phai]$, nếu giống nhau thì tăng `trai` và giảm `phai` cho đến khi gặp nhau.

### 4. Gộp hai mảng đã sắp xếp (Merge Two Sorted Arrays)
Cho 2 mảng đã sắp xếp $A$ và $B$, gộp lại thành mảng $C$ duy nhất giữ nguyên thứ tự sắp xếp.
* **Cách làm:** Đặt con trỏ $i$ ở đầu mảng $A$, con trỏ $j$ ở đầu mảng $B$. So sánh $A[i]$ và $B[j]$, phần tử nào nhỏ hơn thì cho vào $C$ rồi tăng con trỏ tương ứng.

### 5. Cửa sổ trượt (Sliding Window - Two Pointers cùng chiều)
Tìm mảng con liên tiếp dài nhất/ngắn nhất thỏa mãn điều kiện nào đó.
* **Cách làm:** Hai con trỏ `trai` và `phai` cùng bắt đầu từ đầu mảng. `phai` mở rộng cửa sổ để nạp thêm phần tử, `trai` thu hẹp cửa sổ khi điều kiện bị vi phạm.

---

## 🚩 Dấu hiệu nhận biết bài toán Two Pointers

Khi đọc đề bài, nên cân nhắc sử dụng Two Pointers nếu xuất hiện các dấu hiệu:

1. Đề bài cho mảng hoặc dãy số **ĐÃ SẮP XẾP** (hoặc bài toán cho phép sắp xếp mảng trước mà không làm ảnh hưởng đến yêu cầu).
2. Yêu cầu tìm **cặp phần tử** hoặc **bộ $K$ phần tử** thỏa mãn điều kiện về tổng, hiệu hoặc khoảng cách.
3. Bài toán xử lý mảng/chuỗi có tính chất đối xứng, đảo ngược, hoặc so sánh hai đầu.
4. Cần tối ưu thuật toán từ $O(n^2)$ về $O(n)$ hoặc từ $O(n^3)$ về $O(n^2)$.

---

[⬅️ Quay lại trang chính README](../README.md)