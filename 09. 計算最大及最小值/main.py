a, b, c, d, e, f = input().split() # 讀入多個字並以空格分隔

a = int(a) # 轉換為整數型態
b = int(b) # 轉換為整數型態
c = int(c) # 轉換為整數型態
d = int(d) # 轉換為整數型態
e = int(e) # 轉換為整數型態
f = int(f) # 轉換為整數型態

Max = max(a, b, c, d, e, f) # 計算最大值並存到 Max

Min = min(a, b, c, d, e, f) # 計算最小值並存到 Min

print("您輸入的數值為 :", a, b, c, d, e, f) # 按照格式輸出當前輸入的數值

print("最大值 : ", Max, " 及最小值 : ", Min, sep = '') # 按照格式輸出最大及最小值