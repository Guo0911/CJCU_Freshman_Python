# 輸入：2 3 -7 2 5 -9
# 輸出：求出的解為 x = 2.0, y = 1.0

a, b, c, e, f, g = input().split() # 讀入一行輸入，並依照空格分隔

a = int(a) # 轉換為整數型態
b = int(b) # 轉換為整數型態
c = int(c) # 轉換為整數型態
e = int(e) # 轉換為整數型態
f = int(f) # 轉換為整數型態
g = int(g) # 轉換為整數型態

"""

ax + by + c = 0

ex + fy + g = 0

"""

times = (e / a) # 計算兩方程式的倍數差

a2 = a * times # 使兩方程式的 x 係數相同
b2 = b * times # 使兩方程式的 x 係數相同
c2 = c * times # 使兩方程式的 x 係數相同

"""

a2x + b2y + c2 = 0 ... (1)

ex + fy + g = 0 ... (2)

此時 a2 = e

"""

y = (((c2 - g) * -1) / (b2 - f)) # 因為 x 係數相同，因此當 (2) - (1) 時會將 x 消除

"""

     b2y + c2 = 0
  -)  fy +  g = 0
  ---------------
     (b2y - fy) + (c2 - g) = 0
  => (b2 - f)y = -(c2 - g) ... (3)

  當 (3) 除 (b2 - f) 後，則 y 的係數為 1，如 (4) 即可解出 y 的值

    [(b2 - f) / (b2 - f)] y = [-(c2 - g) / (b2 - f)]
  => y = [-(c2 - g) / (b2 - f)] ... (4)

"""

x = ((((b2 * y) + c2) * -1) / a2) # 將 y 代入 (1) 計算出 x 的數值；a2x + b2y + c2 = 0 ... (1)

"""
    a2x + b2y + c2 = 0
  =>a2x + b2y  = -c2
  =>a2x = -b2y - c2
  =>a2x = -(b2y + c2)


    a2x = -b2y - c2 = -(b2y + c2)
  =>  (a2x / a2) = [-(b2y + c2) / a2]
  =>  (a2 / a2)x = [-(b2y + c2) / a2]
  =>  x = [-(b2y + c2) / a2]

"""

print('求出的解為 x = ', x, ', y = ', y, sep = '') # 按照格式輸出 x 與 y