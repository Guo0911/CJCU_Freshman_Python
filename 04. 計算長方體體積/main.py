x, y, z = input().split() # 讀入一行輸入，並依照空格分隔

x = int(x) # 轉換為整數型態
y = int(y) # 轉換為整數型態
z = int(z) # 轉換為整數型態

volume = (x * y * z) # 計算體積

print('您輸入的長為', x, '、寬為', y, '和高為', z, '，體積為', volume) # 按照格式輸出體積