# 🏆 Bộ Đề Luyện Tập COS Pro Python (Level 1)

## Phần 1: Thuật toán cốt lõi (Prefix Sum, Two Pointers, Sliding Window, Binary Search)

### Bài 1: Mảng con có tổng bằng K

Cho một mảng các số nguyên dương `arr` và một số nguyên `K`. Hãy đếm số lượng mảng con liên tiếp (contiguous subarray) có tổng các phần tử đúng bằng `K`.

- **Gợi ý luyện tập (Code cả 2 cách):**
  - **Cách 1 - Two Pointers / Sliding Window:** Do mảng chỉ chứa số dương, bạn có thể dùng 2 con trỏ `trai` và `phai`. Lợi thế: Bộ nhớ $O(1)$, code rất trực quan.
    - [Đọc giải 1](../src/basic_algorithm_problem/ex1_1.py): Đây là bài giải áp dụng máy móc kĩ thuật sliding windown. Ý tưởng của nó là duyệt qua toàn bộ mảng con có 1 đến n phần tử và kiểm tra từng mảng có thỏa mãn không với 2 vòng lặp for => hiệu quả $O(n^2)$.
    - [Đọc giải 2](../src//basic_algorithm_problem/ex1_2.py): Vận dụng linh hoạt 2 pointer chỉ áp dụng khi mảng không âm. Hiệu quả $O(n)$.
  - **Cách 2 - Prefix Sum + Hash Map (Dictionary):** Lưu trữ số lần xuất hiện của các tổng tiền tố. Lợi thế: Xử lý mượt mà kể cả khi mảng có chứa số âm (nếu đề thi mở rộng điều kiện). Độ phức tạp thời gian vẫn là $O(n)$.

- Ứng dụng:
  - 📊 1. Phân tích Dữ liệu Tài chính / Chứng khoán  
    Bài toán: Bạn có dữ liệu biến động giá cổ phiếu hoặc lợi nhuận theo từng ngày trong năm: [-2, 5, -1, 3, -4, 6].  
    Ứng dụng: Tìm giai đoạn liên tiếp $K$ ngày mà công ty hòa vốn (tổng lợi nhuận bằng $0$), hoặc giai đoạn doanh thu đạt đúng mục tiêu $K$ tỷ để làm báo cáo tài chính/chia cổ tức.
  - 🎥 2. Xử lý Tín hiệu & Streaming (Video / Audio)  
    Bài toán: Kiểm tra dung lượng băng thông (Bandwidth) hoặc dữ liệu truyền tải theo từng giây.  
    Ứng dụng: Phát hiện các khoảng thời gian liên tiếp mà tổng dung lượng gói tin vượt quá ngưỡng $K$ để kích hoạt cơ chế tự động hạ độ phân giải (Auto Quality Bitrate) chống giật lag.
  - 🌐 3. Phân tích Hành vi Người dùng (Web Analytics)  
    Bài toán: Nhật ký (Log) lưu lượng truy cập của người dùng trên website theo từng phút.  
    Ứng dụng: Phát hiện các khoảng thời gian liên tiếp xuất hiện lượng truy vấn bất thường đạt ngưỡng $K$ để cảnh báo tấn công DDoS hoặc nghẽn mạng server.

### Bài 2: Chuỗi con không lặp dài nhất

Cho một chuỗi ký tự `S`. Tìm độ dài của chuỗi con liên tiếp dài nhất không chứa bất kỳ ký tự nào lặp lại.

- **Gợi ý luyện tập:**
  - Thuật toán tối ưu: **Sliding Window** kết hợp với Hash Set (hoặc Hash Map để lưu vị trí gần nhất của ký tự).
  - **Lưu ý:** Khi con trỏ `phai` gặp ký tự trùng lặp, không cần nhích con trỏ `trai` từng bước một, mà nhảy thẳng `trai` đến vị trí liền sau ký tự trùng lặp đó để tối ưu thời gian.

### Bài 3: Giao hàng tối ưu (Binary Search on Answer)

Có $N$ kiện hàng với trọng lượng `weights[i]`. Bạn cần chia các kiện hàng này cho $K$ xe tải (các kiện hàng trên cùng 1 xe phải liên tiếp nhau trong mảng). Hãy tìm mức tải trọng sức chứa (Capacity) tối thiểu mà các xe tải cần có để chở hết hàng.

- **Gợi ý luyện tập (Code cả 2 cách):**
  - **Cách 1 - Binary Search:** Không gian tìm kiếm kết quả nằm từ `max(weights)` (xe nhỏ nhất có thể chở kiện to nhất) đến `sum(weights)` (1 xe chở tất cả). Mỗi lần lấy `mid` làm tải trọng thử và đếm số xe cần dùng. Đây là cách chuẩn để pass bài này trong COS Pro ($O(n \log(\text{sum}))$.
  - **Cách 2 - Linear Search (Tìm kiếm tuyến tính):** Cho vòng lặp chạy từ `max(weights)` tăng dần lên. Dùng để đối chiếu kết quả khi debug, nhưng chắc chắn sẽ bị TLE (Time Limit Exceeded) khi nộp bài.

---

## Phần 2: Tham lam (Greedy) & Quy hoạch động (Dynamic Programming)

### Bài 4: Trả tiền lẻ (Coin Change)

Cho một mảng `coins` chứa các mệnh giá đồng xu và một số tiền `amount`. Tìm số lượng đồng xu ít nhất để tạo thành đúng `amount`. (Giả sử số lượng mỗi mệnh giá là vô hạn).

- **Gợi ý luyện tập (Code cả 2 cách):**
  - **Cách 1 - Greedy (Tham lam):** Luôn lấy đồng xu to nhất. Lợi thế: Cực kỳ nhanh $O(n)$. Điểm yếu: Sẽ ra kết quả **SAI** nếu hệ thống tiền tệ không chuẩn. (Ví dụ: `coins = [1, 3, 4]`, `amount = 6`. Greedy ra $4+1+1 = 3$ đồng, nhưng đáp án tối ưu là $3+3 = 2$ đồng).
  - **Cách 2 - Dynamic Programming (DP 1D):** Xây dựng mảng `dp[i]` là số đồng xu ít nhất để đổi số tiền `i`. Luôn cho ra kết quả đúng mọi trường hợp. Đổi lại tốn bộ nhớ $O(\text{amount})$ và thời gian $O(\text{amount} \times \text{len(coins)})$.

### Bài 5: Đường đi chi phí nhỏ nhất (Min Path Sum)

Cho một ma trận $M \times N$ chứa các số nguyên không âm. Tìm một đường đi từ góc trên-trái `(0, 0)` xuống góc dưới-phải `(M-1, N-1)` sao cho tổng các số trên đường đi là nhỏ nhất. Bạn chỉ được phép đi xuống hoặc sang phải.

- **Gợi ý luyện tập (Code cả 2 cách):**
  - **Cách 1 - Dynamic Programming (DP 2D):** `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`. Rất mượt và pass toàn bộ test case.
  - **Cách 2 - Recursion + Backtracking (Đệ quy quay lui):** Duyệt mọi đường đi có thể. Rất tốt để luyện code Đệ quy, nhưng sẽ bị TLE do độ phức tạp $O(2^{m+n})$. Khắc phục bằng cách thêm **Memoization** (lưu mảng nhớ) biến nó thành DP Top-down.

---

## Phần 3: Đếm toán học (Math) & Sinh cấu hình (itertools)

### Bài 6: Xếp chỗ ngồi không cạnh nhau

Có $N$ nam và $N$ nữ cần xếp thành một hàng dọc. In ra tất cả các cách xếp sao cho không có 2 bạn nữ nào đứng cạnh nhau.

- **Gợi ý luyện tập (Code cả 2 cách):**
  - **Cách 1 - Dùng `itertools.permutations`:** Sinh TẤT CẢ cấu hình rồi dùng hàm check (điều kiện `if`). Code cực nhanh, dễ đọc. Hạn chế: Khi $N$ lớn, sinh toàn bộ hoán vị sẽ tràn RAM trước khi kịp lọc.
  - **Cách 2 - Tự code Backtracking với Cắt tỉa (Pruning):** Đang xếp dở mà thấy 2 bạn nữ đứng cạnh nhau là `return` (quay lui) ngay lập tức, không sinh tiếp nhánh đó. Tối ưu vượt trội so với `itertools` trong trường hợp có nhiều ràng buộc.

### Bài 7: Số cách lập đội tuyển thi đấu (Counting Combinations)

Trường có $N$ học sinh giỏi. Cần chọn ra đúng $K$ học sinh để đi thi. Không cần in ra danh sách, chỉ cần trả về **số lượng** đội tuyển khác nhau có thể tạo ra. Biết $N$ có thể lên tới $10^5$.

- **Gợi ý luyện tập (So sánh 2 cách):**
  - **Cách 1 - Dùng `len(list(itertools.combinations(arr, K)))`:** Chắc chắn sập (Memory Error hoặc TLE) vì cố tình sinh ra mảng chứa hàng tỷ phần tử chỉ để đếm.
  - **Cách 2 - Dùng Toán học `math.comb(n, k)` (hoặc `math.perm` nếu có thứ tự):** Độ phức tạp $O(K)$, tính trực tiếp ra kết quả bằng công thức tổ hợp. Luôn ưu tiên dùng hàm này khi bài toán chỉ yêu cầu ĐẾM.

---

## Phần 4: Luyện tập mô phỏng `itertools` (Bài tập Hardcore)

Yêu cầu: KHÔNG được `import itertools`. Hãy viết các hàm (Functions) bằng **Python Generator (sử dụng từ khóa `yield`)** kết hợp **Recursion / Backtracking** để mô phỏng lại y hệt cách thư viện chuẩn hoạt động.

### Bài 8: Tự build hàm `my_permutations(iterable, r=None)`

Mô phỏng lại `itertools.permutations`. Hàm nhận vào một chuỗi hoặc mảng `iterable`, sinh ra các hoán vị độ dài `r` (nếu không truyền `r` thì mặc định `r = len(iterable)`).

- **Kiến thức đạt được:** Nắm vững cách Backtracking kết hợp với `yield` thay vì lưu tất cả kết quả vào một List toàn cục.

### Bài 9: Tự build hàm `my_combinations(iterable, r)`

Mô phỏng lại `itertools.combinations`. Sinh ra các tổ hợp chập `r` của `iterable` theo đúng thứ tự vị trí xuất hiện (không quan tâm giá trị).

- **Lưu ý:** Backtracking của Combinations khác Permutations ở chỗ: biến lặp vòng `for` phải bắt đầu từ chỉ số tiếp theo `start_index` thay vì duyệt lại từ đầu, để tránh sinh ra các tập hợp trùng lặp (vd: sinh ra `[1,2]` rồi không sinh `[2,1]` nữa).

### Bài 10: Tự build hàm `my_product(*iterables)`

Mô phỏng lại `itertools.product` (Tích Đề-các). Nhận vào nhiều mảng (số lượng tham số không cố định, dùng `*args`), sinh ra tất cả các bộ kết quả bằng cách lấy mỗi mảng 1 phần tử.

- **Gợi ý:** Đây là dạng bài Đệ quy sinh cấu hình đa chiều. Yêu cầu truyền `level` (mức đệ quy hiện tại đang xét mảng thứ mấy). Phù hợp nhất cho bài toán sinh Mật khẩu từ các bộ ký tự khác nhau.

---

[⬅️ Quay lại trang chính README](../README.md)
