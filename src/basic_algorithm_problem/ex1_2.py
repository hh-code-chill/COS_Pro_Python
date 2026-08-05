def mang_con_co_tong_bang_k (arr: list[int], k: int):
    left = 0
    current_total = 0
    count = 0
    result = [] # (index đầu, mảng con)
    len_arr = len(arr)

    for right in range(len_arr):
        current_total += arr[right]

        while (left < right and current_total > k):
            current_total -= arr[left]
            left += 1

        if current_total == k:
            count += 1
            result.append((left, arr[left : right + 1]))

    return count, result

arr = [5, 2, 3, 4, 5, 3, 1, 1, 1, 1, 1, 1, 2, 2, 3, 6, 2, 3, 5]
k = 5

print("Index:", "".join(f"{x:>4}" for x in range(len(arr))))
print("Array:", "".join(f"{x:>4}" for x in arr))
print(f"K = {k}")
print("-" * 10)

dem, ke_qua = mang_con_co_tong_bang_k(arr, k)

print(f'Tổng số mảng thỏa mãn: {dem}')
print('Danh sách các mảng:')
for idx, mang_con in ke_qua:
    print(f"  • Tại index {idx:>4} → {mang_con}")
