# Quy hoạch động (Dynamic Programming - DP)

## Lý thuyết

Quy hoạch động là phương pháp giải các bài toán phức tạp bằng cách **chia nhỏ chúng thành các bài toán con**, giải từng bài toán con đúng một lần và **lưu trữ kết quả** (dùng mảng/bảng `dp`) để tái sử dụng.

* **Triết lý:** *"Đánh đổi bộ nhớ (RAM) lấy tốc độ xử lý"* — Tránh việc tính toán lại cùng một bài toán con nhiều lần (khắc phục điểm yếu mù quáng của thuật toán Đệ quy thuần túy).
* **Các bước cốt lõi khi giải bài toán DP:**
  1. **Xác định trạng thái (State):** Mảng `dp[i]` (hoặc `dp[i][j]`) biểu diễn thông tin gì tại bước $i$?
  2. **Xác định công thức truy hồi (State Transition Equation):** Tìm mối liên hệ tính `dp[i]` dựa trên các trạng thái `dp` nhỏ hơn trước đó.
  3. **Khởi tạo bài toán cơ sở (Base Cases):** Gán giá trị ban đầu cho các trạng thái nhỏ nhất không thể chia nhỏ hơn được nữa (ví dụ: `dp[0]`, `dp[1]`).
  4. **Thứ tự tính toán:** Duyệt qua các trạng thái từ nhỏ đến lớn (Bottom-up) để lấp đầy bảng `dp`.

---

## Ví dụ minh họa

**Bài toán Leo cầu thang (Climbing Stairs):** Có $n$ bậc thang. Mỗi lần bạn có thể bước lên $1$ bậc hoặc $2$ bậc. Hỏi có bao nhiêu cách khác nhau để leo lên đến đỉnh bậc thứ $n$?

* **Định nghĩa trạng thái:** Gọi `dp[i]` là số cách để leo lên đến bậc thứ $i$.
* **Công thức truy hồi:** Để đứng ở bậc thứ $i$, bạn chỉ có thể đi từ bậc $(i-1)$ bước lên 1 bậc, hoặc từ bậc $(i-2)$ bước lên 2 bậc.
  $$dp[i] = dp[i - 1] + dp[i - 2]$$
* **Khởi tạo cơ sở:**
  * $dp[0] = 1$ (ở mặt đất, có 1 cách là không bước).
  * $dp[1] = 1$ (chỉ có 1 cách bước 1 bước từ mặt đất).

* **Diễn biến bảng DP với $n = 5$:**
  * $dp[0] = 1$
  * $dp[1] = 1$
  * $dp[2] = dp[1] + dp[0] = 1 + 1 = 2$
  * $dp[3] = dp[2] + dp[1] = 2 + 1 = 3$
  * $dp[4] = dp[3] + dp[2] = 3 + 2 = 5$
  * $dp[5] = dp[4] + dp[3] = 5 + 3 = 8$

👉 Kết quả để leo lên bậc $5$ là **$8$** cách.

### Code Python mẫu

```python
def climb_stairs(n):
    if n <= 1:
        return 1
        
    # 1. Khởi tạo mảng DP với kích thước (n + 1)
    dp = [0] * (n + 1)
    
    # 2. Gán giá trị cơ sở
    dp[0] = 1
    dp[1] = 1
    
    # 3. Tính toán Bottom-up theo công thức truy hồi
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# Chạy thử ví dụ
print("Số cách leo lên 5 bậc:", climb_stairs(5))  # Output: 8
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Lời giải tối ưu của bài toán lớn được xây dựng dựa trên lời giải tối ưu của các bài toán con đã được giải trước đó.

### 1. Bài toán Đếm số cách (Counting Problems)
* **Ví dụ:** Leo cầu thang, Tìm số đường đi duy nhất trên lưới $M \times N$ (Unique Paths) từ góc trên-trái đến góc dưới-phải.
* **Đặc điểm:** Công thức truy hồi dạng tổng các bài toán con ($dp = dp_1 + dp_2 + \dots$).

### 2. Dãy con tăng dài nhất (Longest Increasing Subsequence - LIS)
Cho mảng $a$, tìm độ dài dãy con dài nhất mà các phần tử sau luôn lớn hơn phần tử trước (không nhất thiết phải liên tiếp).
* **Công thức:** $dp[i] = \max(dp[j] + 1)$ với mọi $j < i$ và $a[j] < a[i]$.
* **Tối ưu:** $O(n^2)$ với DP cơ bản hoặc $O(n \log n)$ khi kết hợp DP + Binary Search.

### 3. Bài toán Balo 0/1 (0/1 Knapsack)
Cho $N$ đồ vật với trọng lượng $w[i]$ và giá trị $v[i]$. Chọn các đồ vật sao cho tổng trọng lượng không vượt quá $W$ và tổng giá trị thu được là lớn nhất (mỗi đồ vật chỉ được chọn 1 lần hoặc không chọn).
* **Trạng thái:** $dp[i][w]$ là giá trị lớn nhất khi xét $i$ đồ vật đầu tiên với giới hạn trọng lượng $w$.

### 4. Bài toán Đổi tiền tối ưu (Coin Change - DP Version)
Tìm số lượng đồng xu ít nhất để tạo nên tổng tiền $S$ với hệ thống mệnh giá bất kỳ (khắc phục điểm yếu của thuật toán Tham lam - Greedy khi mệnh giá tiền không tối ưu).
* **Công thức:** $dp[i] = \min(dp[i - coin] + 1)$ với mọi $coin \le i$.

### 5. Biến đổi chuỗi (Edit Distance / Levenshtein Distance)
Tìm số phép biến đổi ít nhất (Thêm, Xóa, Thay thế ký tự) để chuyển chuỗi $A$ thành chuỗi $B$.

---

## 🚩 Dấu hiệu nhận biết bài toán Dynamic Programming

Khi đọc đề bài, nên cân nhắc sử dụng Quy hoạch động nếu xuất hiện các dấu hiệu:

1. Yêu cầu tìm **giá trị tối ưu** (*"lớn nhất"*, *"nhỏ nhất"*) hoặc **đếm số phương án/số cách** thỏa mãn điều kiện.
2. Bài toán có **Các bài toán con chồng lấp (Overlapping Subproblems):** Khi giải bằng Đệ quy thông thường, cùng một bài toán con bị gọi lại nhiều lần gây bùng nổ thời gian $O(2^n)$.
3. Bài toán có **Cấu trúc tối ưu con (Optimal Substructure):** Lời giải tối ưu của bài toán tổng thể chứa lời giải tối ưu của các bài toán con bên trong.
4. Đề bài có **các quyết định/lựa chọn lặp lại** qua từng bước (ví dụ: ở mỗi vật phẩm chọn hay không chọn; ở mỗi bước đi chọn bước 1 hay 2 bậc).

---

[⬅️ Quay lại trang chính README](../README.md)