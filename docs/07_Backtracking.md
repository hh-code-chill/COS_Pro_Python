# Quay lùi (Backtracking)

## Lý thuyết

Thuật toán Quay lùi là phương pháp **thử mọi khả năng có thể** dựa trên chiến lược **Đệ quy (Recursion)**. Thuật toán di chuyển dọc theo cây lựa chọn (Decision Tree) bằng cách chọn một hướng đi; nếu gặp bế tắc hoặc không thỏa mãn điều kiện bài toán, nó sẽ **QUAY LUI (Backtrack)** về bước trước đó để thử hướng đi khác.

* **Cơ chế hoạt động:**
  * Xây dựng dần các phần tử của lời giải.
  * Nếu đạt trạng thái hoàn chỉnh thỏa mãn đề bài $\rightarrow$ Lưu hoặc in ra cấu hình.
  * Nếu nhận thấy hướng đi hiện tại không thể dẫn đến lời giải hợp lệ $\rightarrow$ **Cắt tỉa nhánh (Pruning)** để dừng sớm và quay lại bước trước.
* **Tối ưu trong Python:** Với các bài toán sinh cấu hình cơ bản (hoán vị, tổ hợp), ta có thể tận dụng thư viện `itertools` sẵn có của Python để viết code ngắn gọn và tối ưu tốc độ hơn.

---

## Ví dụ minh họa

Sinh tất cả các **Hoán vị (Permutations)** của một danh sách phần tử, ví dụ $a = [1, 2, 3]$.

* **Cây lựa chọn (Decision Tree):**
  * Bắt đầu: `cur = []`, tập phần tử còn lại `con = [1, 2, 3]`.
  * **Bước 1:** Thử chọn `1` $\rightarrow$ `cur = [1]`, `con = [2, 3]`.
  * **Bước 2:** Thử chọn `2` $\rightarrow$ `cur = [1, 2]`, `con = [3]`.
  * **Bước 3:** Thử chọn `3` $\rightarrow$ `cur = [1, 2, 3]`, `con = []` $\rightarrow$ In `[1, 2, 3]`, quay lui!
  * Tiếp tục quay lùi lên Bước 2 để thử phương án chọn `3` trước `2`...

### Code Python mẫu

#### 1. Viết thuần bằng Đệ quy Quay lùi (Handmade)
```python
def sinh_hoan_vi(cur, con):
    # Trạng thái cơ sở: không còn phần tử nào để chọn
    if not con:
        print(cur)
        return
        
    # Duyệt qua từng lựa chọn khả thi ở bước hiện tại
    for i in range(len(con)):
        # Chọn con[i], đệ quy tiếp với tập con còn lại (loại bỏ con[i])
        sinh_hoan_vi(cur + [con[i]], con[:i] + con[i+1:])

# Chạy thử ví dụ
a = [1, 2, 3]
sinh_hoan_vi([], a)
```

#### 2. Sử dụng thư viện `itertools` (Khuyên dùng khi thi)
```python
import itertools

a = [1, 2, 3]

# Sinh tất cả hoán vị độ dài len(a)
for p in itertools.permutations(a):
    print(list(p))
```

---

## Các Dạng Bài Toán Mở Rộng

> 💡 **Tư tưởng cốt lõi:** Duyệt vét cạn (Exhaustive Search) kết hợp Cắt tỉa (Pruning) trên không gian trạng thái nhằm tránh việc duyệt qua các trường hợp chắc chắn sai.

### 1. Sinh các Cấu hình Đếm / Tổ hợp (Generation Problems)
* Sinh chuỗi nhị phân độ dài $N$.
* Sinh tập con / Tổ hợp chập $K$ của $N$ phần tử (`itertools.combinations`).
* Sinh Hoán vị của $N$ phần tử (`itertools.permutations`).

### 2. Bài toán Xếp Hậu (N-Queens Problem)
Đặt $N$ quân hậu lên bàn cờ $N \times N$ sao cho không có 2 quân hậu nào khống chế lẫn nhau (không cùng hàng, cột, đường chéo).
* **Cắt tỉa nhánh:** Trước khi đặt quân hậu ở cột $j$, kiểm tra xem vị trí đó có bị tấn công bởi các quân hậu đã đặt trước đó hay không. Nếu có thì bỏ qua ngay.

### 3. Giải ô số Sudoku (Sudoku Solver)
Thử điền các số từ 1 đến 9 vào ô trống. Nếu điền đến một ô mà không có số nào hợp lệ $\rightarrow$ Quay lui lại ô trống trước đó để đổi sang số khác.

### 4. Giải Mê cung / Tìm đường đi (Maze Solving / Path Finding)
Tìm tất cả các đường đi từ điểm bắt đầu đến điểm kết thúc trên một lưới ma trận 2D. 
* Đánh dấu ô đã đi qua để tránh lặp vô tận, sau khi quay lui thì bỏ đánh dấu để các nhánh khác có thể đi qua ô đó.

### 5. Bài toán Tập con có tổng bằng K (Subset Sum)
Tìm tất cả các tập con của mảng sao cho tổng các phần tử đúng bằng $K$.

---

## 🚩 Dấu hiệu nhận biết bài toán Backtracking

Khi đọc đề bài, nên cân nhắc sử dụng Quay lùi nếu xuất hiện các dấu hiệu:

1. Đề bài yêu cầu **"liệt kê tất cả"**, **"sinh mọi cấu hình"**, **"đếm số cách sắp xếp"**, hoặc **"tìm tất cả các đường đi/phương án"** thỏa mãn ràng buộc.
2. Kích thước đầu vào $N$ **rất nhỏ** (thường $N \le 15 \dots 20$) do độ phức tạp thời gian tăng theo cấp số nhân ($O(2^n)$ hoặc $O(N!)$).
3. Không thể áp dụng các thuật toán tối ưu hơn như Tham lam (Greedy) hay Quy hoạch động (DP) do bài toán thiếu tính chất tối ưu con hoặc yêu cầu xuất ra chi tiết từng cấu hình.

---

[⬅️ Quay lại trang chính README](../README.md)