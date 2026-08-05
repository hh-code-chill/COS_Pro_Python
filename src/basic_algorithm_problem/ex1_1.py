def mang_con_co_tong_bang_k(arr: list[int], k: int):
    n = len(arr)
    count = 0
    result = {} # (idx đầu tiên, số phần tử): mảng xuất hiện
    for so_phan_tu_con in range(1, n + 1):
        tong_mang = sum(arr[:so_phan_tu_con])
        if(tong_mang == k):
            count += 1
            result[(0,so_phan_tu_con)] = arr[:so_phan_tu_con]

        for i in range(so_phan_tu_con , n):
            tong_mang += arr[i] - arr[i - so_phan_tu_con]
            if(tong_mang == k):
                count += 1
                idx_phan_tu_dau = i - so_phan_tu_con + 1
                result[(idx_phan_tu_dau, so_phan_tu_con)] = arr[idx_phan_tu_dau: idx_phan_tu_dau + so_phan_tu_con]
    return count, result

# arr = list(map(int, input().split()))
# k = int(input())

arr = [1, 2, 3, 4, 5, 3]
k = 3
print([x for x in range(len(arr))])
print(arr)
print(k)
dem, ke_qua = mang_con_co_tong_bang_k(arr, k)
print(f'Tổng số mảng thỏa mãn: {dem} \nDanh sách các mảng:')
print(ke_qua)