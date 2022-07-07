x, y = input().split() # 讀入一行輸入，並且依照空格分隔

x = int(x) # 將 x 轉換為整數型態
y = int(y) # 將 y 轉換為整數型態

area = (x * y) # 計算面積

print('您輸入的長為', x , '和寬為', y, '，面積為', area) # 按照格式輸出面積