# Cửa sổ trượt (Sliding Window)

## Lý thuyết

Giữ một "cửa sổ" trên đoạn con liên tiếp của mảng/chuỗi. Khi dịch chuyển cửa sổ sang phải, ta chỉ cần **thêm phần tử mới** (đi vào cửa sổ) và **bớt phần tử cũ** (đi ra khỏi cửa sổ) thay vì phải tính toán lại từ đầu toàn bộ đoạn con.

* **Ứng dụng:** Dùng cho bài toán tìm mảng con hoặc chuỗi con **LIÊN TIẾP** thỏa mãn điều kiện tối ưu (tổng lớn nhất, độ dài nhỏ nhất, tệp ký tự duy nhất...).
* **Cơ chế:** Cộng giá trị mới $a[i]$, trừ giá trị cũ $a[i - k]$.
* **Tối ưu:** Giảm độ phức tạp thời gian từ $O(n \times k)$ xuống $O(n)$.

---

## Ví dụ minh họa

Cho mảng $a = [2, 1, 5, 1, 3, 2]$ và kích thước cửa sổ cố định $k = 3$. Tìm tổng $k$ phần tử liên tiếp lớn nhất.

* **Khởi tạo:** Tính tổng $k$ phần tử đầu tiên:
  $$\text{cua\_so} = a[0] + a[1] + a[2] = 2 + 1 + 5 = 8$$
  Lưu $\text{tot} = 8$.

* **Trượt cửa sổ từ $i = 3$ đến $n-1$:**
  * **Khi $i = 3$ (nhận $a[3] = 1$, bỏ $a[0] = 2$):**
    $$\text{cua\_so} = 8 + 1 - 2 = 7 \rightarrow \text{tot} = \max(8, 7) = 8$$
  * **Khi $i = 4$ (nhận $a[4] = 3$, bỏ $a[1] = 1$):**
    $$\text{cua\_so} = 7 + 3 - 1 = 9 \rightarrow \text{tot} = \max(8, 9) = 9$$
  * **Khi $i = 5$ (nhận $a[5] = 2$, bỏ $a[2] = 5$):**
    $$\text{cua\_so} = 9 + 2 - 5 = 6 \rightarrow \text{tot} = \max(9, 6) = 9$$

Kết quả tổng lớn nhất đạt được là **$9$** (tương ứng đoạn $[5, 1, 3]$).

### Code Python mẫu

```python
def max_sub_array_of_size_k(a, k):
    n = len(a)
    if n < k:
        return 0
        
    # Tính tổng cửa sổ đầu tiên
    cua_so = sum(a[:k])
    tot = cua_so
    
    # Trượt cửa sổ qua phần còn lại của mảng
    for i in range(k, n):
        cua_so += a[i] - a[i - k]  # Thêm phần tử mới a[i], bớt phần tử cũ a[i - k]
        tot = max(tot, cua_so)
        
    return tot
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Tận dụng lại sự trùng lặp (overlap) giữa hai cửa sổ liên tiếp để tránh tính toán trùng lặp, đưa độ phức tạp từ $O(n \times k)$ hoặc $O(n^2)$ về $O(n)$.

### 1. Cửa sổ trượt kích thước cố định $K$ (Fixed Size Sliding Window)
Dạng bài cơ bản nhất giống ví dụ trên (tính tổng, trung bình cộng, hoặc tìm giá trị lớn nhất/nhỏ nhất của mọi mảng con có độ dài đúng bằng $K$).
* **Ví dụ đề thi:** Bài toán tính tổng doanh thu lớn nhất của cửa hàng pop-up trong $K$ ngày liên tiếp (đề thi COS Pro).

### 2. Cửa sổ trượt kích thước linh hoạt (Variable Size Sliding Window)
Cửa sổ mở rộng hoặc thu hẹp tùy thuộc vào điều kiện đề bài.
* **Bài toán:** Tìm mảng con ngắn nhất có tổng $\ge S$, hoặc tìm chuỗi con dài nhất không chứa ký tự trùng lặp.
* **Cách giải:** Dùng 2 con trỏ `phai` (mở rộng cửa sổ) và `trai` (thu hẹp cửa sổ khi thỏa mãn hoặc vi phạm điều kiện).

### 3. Cửa sổ trượt kết hợp Hash Table / Monotonic Queue
* **Cửa sổ trượt + Hash Map:** Dùng đếm tần suất ký tự trong cửa sổ trượt (ví dụ: Tìm tất cả chuỗi đồng anagram).
* **Cửa sổ trượt + Deque (Monotonic Queue):** Tìm phần tử lớn nhất/nhỏ nhất trong mỗi cửa sổ kích thước $K$ (Sliding Window Maximum) với độ phức tạp $O(n)$.

---

## 🚩 Dấu hiệu nhận biết bài toán Sliding Window

Khi đọc đề bài, nên cân nhắc sử dụng Cửa sổ trượt nếu xuất hiện các dấu hiệu:

1. Yêu cầu xử lý trên **mảng con (subarray)** hoặc **chuỗi con (substring)** phải **LIÊN TIẾP**.
2. Đề bài có tham số **kích thước cố định $K$** (ví dụ: "trong $K$ phần tử liên tiếp", "$K$ ngày liên tiếp").
3. Yêu cầu tìm giá trị **lớn nhất (Max), nhỏ nhất (Min), hoặc tính tổng/trung bình** trên các đoạn liên tiếp.
4. Đề bài yêu cầu tìm **độ dài dài nhất/ngắn nhất** của mảng con thỏa mãn một điều kiện $X$ nào đó.

---

[⬅️ Quay lại trang chính README](../README.md)