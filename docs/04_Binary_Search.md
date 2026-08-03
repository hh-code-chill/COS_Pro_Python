# Tìm kiếm nhị phân (Binary Search)

## Lý thuyết

Thao tác tìm kiếm trên mảng **ĐÃ SẮP XẾP**. Với mỗi bước, so sánh giá trị cần tìm với phần tử ở giữa (`mid`) để loại bỏ một nửa không gian tìm kiếm còn lại, giúp đưa độ phức tạp thời gian xuống $O(\log n)$.

* **Cơ chế hoạt động:**
  * So sánh giá trị cần tìm $x$ với $a[mid]$.
  * Nếu $x < a[mid]$: Giá trị $x$ chỉ có thể nằm ở nửa bên trái $\rightarrow$ thu hẹp khoảng tìm kiếm về nửa trái (`hi = mid - 1`).
  * Nếu $x > a[mid]$: Giá trị $x$ chỉ có thể nằm ở nửa bên phải $\rightarrow$ thu hẹp khoảng tìm kiếm về nửa phải (`lo = mid + 1`).
  * Nếu $x == a[mid]$: Tìm thấy phần tử $\rightarrow$ trả về vị trí.
* **Thư viện hỗ trợ trong Python:** Có sẵn module `bisect` (`bisect_left`, `bisect_right`) giúp tìm vị trí chèn/tìm kiếm cực nhanh.

---

## Ví dụ minh họa

Cho mảng đã sắp xếp: $a = [1, 3, 5, 7, 9, 11, 13]$ và giá trị cần tìm $x = 7$.

* **Khởi tạo:** `lo = 0`, `hi = 6` ($n = 7$).
* **Diễn biến từng bước:**
  * **Bước 1:** 
    * $\text{mid} = (0 + 6) // 2 = 3$
    * $a[3] = 7$
    * Vì $a[3] == 7 \rightarrow$ Tìm thấy $x = 7$ ngay tại chỉ số `mid = 3`. Dừng!

*(Trường hợp tìm $x = 11$: Bước 1 sẽ thấy $a[3] = 7 < 11 \rightarrow$ cập nhật `lo = 3 + 1 = 4`, sang Bước 2 xét nửa $[9, 11, 13]$).*

### Code Python mẫu

#### 1. Code thuần (Handmade)
```python
def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid       # Trả về vị trí tìm thấy
        elif a[mid] < x:
            lo = mid + 1     # Tìm nửa bên phải
        else:
            hi = mid - 1     # Tìm nửa bên trái
            
    return -1                # Không tìm thấy
```

#### 2. Dùng module `bisect` trong Python
```python
import bisect

# Tìm vị trí đầu tiên >= x (tương đương bisect_left)
index = bisect.bisect_left(a, x)

# Kiểm tra xem x có thực sự tồn tại tại vị trí đó không
if index < len(a) and a[index] == x:
    print(f"Tìm thấy {x} tại chỉ số {index}")
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Chia để trị (Divide and Conquer), chia đôi không gian tìm kiếm sau mỗi bước xử lý.

### 1. Tìm kiếm giá trị chính xác / Vị trí xuất hiện đầu tiên, cuối cùng
Bài toán cơ bản kiểm tra sự tồn tại của $x$ hoặc tìm vị trí xuất hiện đầu tiên/cuối cùng của $x$ trong mảng có các phần tử trùng lặp (dùng `bisect_left` / `bisect_right`).

### 2. Tìm kiếm nhị phân trên kết quả (Binary Search on Answer)
Đây là dạng bài **rất hay gặp trong các kỳ thi thuật toán**. Đề bài không yêu cầu tìm phần tử trong mảng, mà yêu cầu tìm một **giá trị kết quả tối ưu** (nhỏ nhất hoặc lớn nhất) thỏa mãn điều kiện $X$.
* **Cách làm:** Xác định khoảng kết quả khả thi $[lo, hi]$. Dùng Binary Search để thử giá trị $mid$, kiểm tra xem $mid$ có thỏa mãn điều kiện không (hàm `check(mid)`), từ đó thu hẹp khoảng nghiệm.
* **Ví dụ:** Tìm vận tốc nhỏ nhất để hoàn thành công việc đúng hạn, tìm kích thước thùng chứa nhỏ nhất...

### 3. Tìm phần tử trong mảng xoay (Rotated Sorted Array)
Mảng ban đầu đã sắp xếp nhưng bị xoay tại một vị trí (ví dụ: $[4, 5, 6, 7, 0, 1, 2]$). Vẫn áp dụng Binary Search bằng cách xác định nửa nào của mảng đang được sắp xếp đúng thứ tự tại mỗi bước.

---

## 🚩 Dấu hiệu nhận biết bài toán Binary Search

Khi đọc đề bài, nên cân nhắc sử dụng Tìm kiếm nhị phân nếu xuất hiện các dấu hiệu:

1. Đề bài cung cấp mảng dữ liệu **ĐÃ SẮP XẾP** và kích thước mảng rất lớn ($N \ge 10^5$).
2. Cần tìm kiếm phần tử/vị trí với yêu cầu độ phức tạp thời gian tối ưu là $O(\log n)$.
3. Bài toán yêu cầu **"tìm giá trị nhỏ nhất thỏa mãn..."** hoặc **"tìm giá trị lớn nhất sao cho..."** (Dạng Binary Search on Answer).
4. Hàm kiểm tra tính đúng đắn có tính chất **đơn điệu** (Monotonic function): Nếu $x$ thỏa mãn thì mọi giá trị $> x$ (hoặc $< x$) cũng thỏa mãn.

---

[⬅️ Quay lại trang chính README](../README.md)