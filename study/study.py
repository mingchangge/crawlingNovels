from decimal import Decimal, getcontext

# 数据类型
print(10/3) #输出：3.3333333333333335
print(9/3) #输出：3.0
print(10//3) #输出：3
print(10%3) #输出：1

# 设置精度
getcontext().prec = 20

# 计算 10 / 3
result = Decimal(10) / Decimal(3)
print(result)  # 输出：3.3333333333333333333

# 字符串
print('I\'m "ok"!') # 输出：I'm "ok"!
print('\\\t\\') # 输出：\       \
print(r'\\\t\\') # 输出：\\\t\\
print('''line1
line2
line3''') # 输出：line1 line2 line3