# Tổng tiền tố (Prefix Sum)

## Lý thuyết

Tính trước mảng tổng dồn để mỗi truy vấn _"tổng đoạn $i..j$"_ chỉ còn một phép trừ, đạt độ phức tạp $O(1)$.

- **Định nghĩa:** $P[k]$ là tổng $k$ phần tử đầu tiên.
- **Công thức:** $\text{tổng } a[i..j] = P[j+1] - P[i]$
- **Ứng dụng:** Dùng khi bài toán yêu cầu tính tổng nhiều đoạn con liên tiếp.
- **Tối ưu:** Giảm độ phức tạp từ $O(n)$ cho mỗi truy vấn xuống $O(1)$.

---

## Ví dụ minh họa

Cho mảng ban đầu: $a = [3, 1, 4, 1, 5]$ (đánh số chỉ số từ $0$ đến $4$ trong Python).

Mảng tổng dồn được khởi tạo với độ dài $\text{len}(a) + 1 = 6$:

- $P = [0, 3, 4, 8, 9, 14]$
- Giải thích từng chỉ số:
  - $P[0] = 0$
  - $P[1] = a[0] = 3$
  - $P[2] = a[0] + a[1] = 4$
  - $P[3] = a[0] + a[1] + a[2] = 8$
  - $P[4] = a[0] + a[1] + a[2] + a[3] = 9$
  - $P[5] = a[0] + \dots + a[4] = 14$

> **Tóm lại:** $P[k]$ là tổng của $k$ phần tử đầu tiên (tương đương tổng từ $a[0]$ đến $a[k-1]$).

### Code khởi tạo mảng Prefix Sum ($P$ có kích thước $n+1$)

```python
P = [0] * (len(a) + 1)
for i in range(len(a)):
    P[i + 1] = P[i] + a[i]
```

### Tính tổng đoạn từ chỉ số $i$ đến $j$ (0-indexed)

$$\text{Sum}(i, j) = P[j + 1] - P[i]$$

**Ví dụ:** Muốn tính tổng từ chỉ số $1$ đến $3$ trong mảng $a = [3, 1, 4, 1, 5]$:

- $i = 1, j = 3$
- $\text{Sum}(1, 3) = P[4] - P[1] = 9 - 3 = 6$

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Đánh đổi một ít bộ nhớ (để lưu mảng $P$) và tốn $O(n)$ thời gian tiền xử lý ban đầu, đổi lại khả năng trả lời mọi truy vấn trong $O(1)$.

### 1. Bài toán Truy vấn Tổng đoạn (Range Sum Queries)

Đây là dạng bài cơ bản nhất. Cho một mảng $a$ gồm $n$ phần tử, nhận vào $q$ truy vấn, mỗi truy vấn yêu cầu tính tổng các phần tử từ chỉ số $L$ đến $R$.

- **Cách ngây thơ (Brute Force):** Lặp từ $L$ đến $R$ để cộng dồn $\rightarrow$ Tốn $O(n)$ cho mỗi truy vấn, tổng độ phức tạp $O(q \times n)$ (Dễ bị **TLE - Time Limit Exceeded**).
- **Áp dụng Prefix Sum:** Tính trước mảng $P$ trong $O(n)$, mỗi truy vấn chỉ cần tính $P[R+1] - P[L]$ trong $O(1)$. Tổng độ phức tạp giảm xuống $O(n + q)$.

### 2. Tìm dãy con liên tiếp có tổng bằng $K$ (Subarray Sum Equals K)

Cho mảng $a$, tìm số lượng (hoặc độ dài lớn nhất/nhỏ nhất) của mảng con liên tiếp có tổng đúng bằng $K$.

- **Công thức biến đổi:**
  $$\text{Sum}(i, j) = P[j+1] - P[i] = K \iff P[i] = P[j+1] - K$$
- **Kỹ thuật kết hợp:** Combined **Prefix Sum + Hash Map (Dictionary)**. Khi duyệt qua từng phần tử $j$, kiểm tra giá trị $(P[j+1] - K)$ đã xuất hiện trong Hash Map trước đó chưa. Kỹ thuật này giúp tối ưu độ phức tạp từ $O(n^2)$ về $O(n)$.

### 3. Bài toán trên mảng 2 chiều (2D Prefix Sum / Matrix Range Sum)

Cho ma trận $A$ kích thước $m \times n$, cần trả lời nhiều truy vấn tính tổng các số trong một hình chữ nhật con có góc trên-trái là $(r_1, c_1)$ và góc dưới-phải là $(r_2, c_2)$.

- **Áp dụng:** Xây dựng mảng Prefix Sum 2D dựa trên nguyên lý **Bao hàm - Loại trừ (Inclusion-Exclusion Principle)**.
- Giúp tính tổng bất kỳ hình chữ nhật con nào trong ma trận chỉ với độ phức tạp $O(1)$.

### 4. Mảng hiệu (Difference Array) kết hợp Prefix Sum

Dạng bài yêu cầu **cập nhật cộng/trừ một giá trị $v$ vào tất cả các phần tử trong khoảng $[L, R]$** qua $q$ thao tác, sau đó xuất ra mảng cuối cùng.

- **Thực hiện:**
  1. **Tạo Mảng hiệu (Difference Array $D$):** Khi cần cộng $v$ vào đoạn $[L, R]$, chỉ cần 2 thao tác: $D[L] += v$ và $D[R+1] -= v$ (mỗi thao tác tốn $O(1)$).
  2. **Tái tạo mảng ban đầu:** Lấy **Prefix Sum** của mảng hiệu $D$ để thu được mảng kết quả cuối cùng.

### 5. Xử lý chuỗi (String / Character Counting)

- **Ví dụ:** Cho một chuỗi ký tự, cần trả lời $q$ câu hỏi dạng: _"Trong đoạn từ vị trí $L$ đến $R$ có bao nhiêu ký tự 'a'?"_
- **Cách làm:** Tạo mảng Prefix Sum đếm tần suất với $P[i]$ lưu số lượng ký tự 'a' xuất hiện từ đầu chuỗi đến vị trí $i$. Số ký tự 'a' trong khoảng $[L, R]$ sẽ là $P[R+1] - P[L]$.

---

## 🚩 Dấu hiệu nhận biết bài toán Prefix Sum

Khi đọc đề bài, nên cân nhắc sử dụng Prefix Sum nếu xuất hiện các dấu hiệu:

1. Có các cụm từ: **"dãy con liên tiếp" (contiguous subarray)**, **"đoạn [L, R]"**, **"ma trận con"**.
2. Bài toán có **nhiều truy vấn (multiple queries)** đọc dữ liệu liên tục trên một mảng **cố định** (không có thao tác thêm/xóa phần tử động giữa chừng).

---

[⬅️ Quay lại trang chính README](../README.md)
