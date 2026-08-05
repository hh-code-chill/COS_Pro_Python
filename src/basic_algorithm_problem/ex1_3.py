def mang_con_tong_bang_k (arr: list[int], k: int):
    tong_tich_luy = 0
    mang_tich_luy = {0: [-1]}
    ke_qua = []
    len_arr = len(arr)

    for i in range(len_arr):
        tong_tich_luy += arr[i]
        hieu_tich_luy_va_k = tong_tich_luy - k

        if(hieu_tich_luy_va_k in mang_tich_luy):
            for idx in mang_tich_luy[hieu_tich_luy_va_k]:
                idx_left = idx + 1
                idx_right = i
                mang_thoa_man = arr[idx_left : idx_right + 1]
                ke_qua.append((idx_left, idx_right, mang_thoa_man))

        if(tong_tich_luy not in mang_tich_luy):
            mang_tich_luy[tong_tich_luy] = []

        mang_tich_luy[tong_tich_luy].append(i)

    return ke_qua

arr = [5, 2, 3, 4, 5, 3, 1, 1, 1, 1, 1, 1, 2, 2, 3, 6, 2, 3, 5]
k = 5
result = mang_con_tong_bang_k(arr, k)
DO_DAI_CUA_SO = 4
tong_so_ket_qua = len(result)
print("Index: ", "".join(f"{x:>{DO_DAI_CUA_SO}}" for x in range(len(arr))))
print("Array: ", "".join(f"{x:>{DO_DAI_CUA_SO}}" for x in arr))
print(f"Có {tong_so_ket_qua} kết quả thỏa mãn điều kiện:")
for idx_left, idx_right, mang_thoa_man in result:
    print(f"Từ {idx_left:>{DO_DAI_CUA_SO}} đến {idx_right:>{DO_DAI_CUA_SO}}: {mang_thoa_man}")