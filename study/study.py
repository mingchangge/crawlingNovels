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

# 变量
a = 123
print(a) # 输出：123
a='ABC'
print(a) # 输出：ABC
a = True
print(a) # 输出：True
a = None
print(a) # 输出：None

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''
print(n, f, s1, s2, s3, s4) # 输出：123 456.789 Hello, world Hello, 'Adam' Hello, "Bart" Hello, Bob!
print("------------------------------------字符串-----------------------------------------------------")
print(ord("中")) # 输出：20013==》20013十进制转为16进制为4e2d
print(chr(20013)) # 输出：中
print(chr(0x4e2d)) # 输出：中
print('\u4e2d') # 输出：中==》\u 用于在字符串中以十六进制的形式表示一个 Unicode 字符。它后面紧跟着四位十六进制数字，这四位数字代表了 Unicode 字符集中的码点。当解释器遇到 \u4e2d 时，它会将这四位十六进制数 4e2d 转换为对应的 Unicode 字符 “中”。
print('中' == chr(0x4e2d)) # 输出：True
print('ABC'.encode('ascii')) # 输出：b'ABC'  # 将字符串编码为字节串
print('中文'.encode('utf-8')) # 输出：b'\xe4\xb8\xad\xe6\x96\x87'  # 将字符串编码为字节串
print(b'ABC'.decode('ascii')) # 输出：ABC  # 将字节串解码为字符串
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 输出：中文  # 将字节串解码为字符串
print(len('ABC')) # 输出：3  # 字符串长度
print(len('中文')) # 输出：2  # 字符串长度
print(len('ABC'.encode('utf-8'))) # 输出：3 # 字节串长度
print(len('中文'.encode('utf-8'))) # 输出：6  # 字节串长度
print('hello, %s' % 'world') # 输出：hello, world
print('hello, %s,you have $%d.' % ('anna',100))    # 输出：hello, anna,you have $100.
print('%2d-%02d' % (3, 1)) # 输出： 3-01
print('%2d-%02d' % (3, 13)) # 输出： 3-13
print('%2d-%02d' % (3, 153)) # 输出： 3-153
print('%.2f' % 3.1415926) # 输出：3.14
print('rate:%d%%' % 60) # 输出：rate:60%
print('hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) # 输出：hello, 小明, 成绩提升了 17.1%
r=2.5
s=3.14*r**2
print(f'圆的半径是{r},面积是{s:.2f}') # 输出：圆的半径是2.5,面积是19.62

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print(f'小明的成绩提升了{r:.1f}%') # 输出：小明的成绩提升了18.1%
print(','.join('abc')) #输出：a,b,c
print(';'.join(['a', 'b', 'c'])) # 输出：a;b;c
print('------------------------------------------list,tuple--------------------------------------------------------------')
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates) # 输出：['Michael', 'Bob', 'Tracy']
print(classmates[0]) # 输出：Michael
print(classmates[1]) # 输出：Bob
print(classmates[2]) # 输出：Tracy
# print(classmates[3]) # 输出：IndexError: list index out of range
print(classmates[-1]) # 输出：Tracy
print(classmates[-2]) # 输出：Bob
print(classmates[-3]) # 输出：Michael
print(classmates[0:2]) # 输出：['Michael', 'Bob']
print(classmates[0:3]) # 输出：['Michael', 'Bob', 'Tracy']
print(classmates[0:4]) # 输出：['Michael', 'Bob', 'Tracy']
print(len(classmates)) # 输出：3
print(classmates.append('Admin')) # 输出：None
print(classmates) # 输出：['Michael', 'Bob', 'Tracy', 'Admin']
print(classmates.insert(1, 'lucy')) # 输出：None
print(classmates) # 输出：['Michael', 'lucy', 'Bob', 'Tracy', 'Admin']
print(classmates.pop()) # 输出：Admin
print(classmates) # 输出：['Michael', 'lucy', 'Bob', 'Tracy']
print(classmates.pop(1)) # 输出：lucy
print(classmates) # 输出：['Michael', 'Bob', 'Tracy']
classmates[1] = 100
print(classmates) # 输出：['Michael', 100, 'Tracy']
classmates[2] = [1, 2, 3]
print(classmates) # 输出：['Michael', 100, [1, 2, 3]]
print(classmates[2][0]) # 输出：1
print(len(classmates)) # 输出：3
print(len([])) # 输出：0
# tuple
classmateTuple = ('Michael', 100, [1, 2, 3])
print(classmateTuple) # 输出：('Michael', 100, [1, 2, 3])
print(classmateTuple[0]) # 输出：Michael
# classmateTuple.append('Admin') # 输出：AttributeError: 'tuple' object has no attribute 'append'
t=(1)
print(t) # 输出：1
print(type(t)) # 输出：<class 'int'>
t=(1,)
print(t) # 输出：(1,)
print(type(t)) # 输出：<class 'tuple'>
classmateTuple[2][0] = 'A'
print(classmateTuple) # 输出：('Michael', 100, ['A', 2, 3])
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t) # 输出：('a', 'b', ['X', 'Y'])
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])
print(L[-1][-1])

print('------------------------------------------模式匹配--------------------------------------------------------------')
score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

#age = 15
age = 5
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

def match_test(item):
    match item:
        case (x,y) if x==y:
            print(f'匹配到x、y相等的元祖: {item}')
        case (x,y):
            print(f'匹配到x、y不等的元祖: {item}')
        case _:
            print(f'其他情况: {item}')
match_test((1, 1)) # 输出：匹配到x、y相等的元祖: (1, 1)
match_test((1, 2)) # 输出：匹配到x、y不等的元祖: (1, 2)
match_test((1, 2, 3)) # 输出：其他情况: (1, 2, 3)

args = ['gcc', 'hello.c', 'world.c','test.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# 输出：gcc compile: hello.c, world.c, test.c
print('------------------------------------------dict和set--------------------------------------------------------------')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob']) # 输出：75
d['Adam'] = 67
print(d) # 输出：{'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}
# print(d['lucy']) # 输出报错：KeyError: 'lucy'
print('lucy' in d) # 输出：False
print(d.get('lucy')) # 输出：None
print(d.get('lucy', -1)) # 输出：-1
d.pop('Bob')
print(d) # 输出：{'Michael': 95, 'Tracy': 85, 'Adam': 67}
#key=[1,2,3]
#d[key] = 100 # 输出报错：TypeError: unhashable type: 'list'
s={1,2,3}
print(s) # 输出：{1, 2, 3}
s=set([1,2,3])
print(s) # 输出：{1, 2, 3}
s.add(4)
print(s) # 输出：{1, 2, 3, 4}
s={1,2,3,3,4}
print(s) # 输出：{1, 2, 3, 4}
s.remove(3)
print(s) # 输出：{1, 2, 4}
s1= {1, 2, 3}
s2= {2, 3, 4}
print(s1 & s2) # 输出：{2, 3}
print(s1 | s2) # 输出：{1, 2, 3, 4}
print(s1 - s2) # 输出：{1}
print(s2 - s1) # 输出：{4}
print(s1 ^ s2) # 输出：{1, 4}
a=[3,4,1,2,5]
a.sort()
print(a) # 输出：[1, 2, 3, 4, 5]
a='abc'
print(a.replace('a','A')) # 输出：Abc
b=a.replace('a','A')
print(b) # 输出：Abc
print(a) # 输出：abc
d = {'a': 1, 'b': 2, 'c': 3}
t=(1,2,3)
d[t]='abc'
print(d) # 输出：{'a': 1, 'b': 2, 'c': 3, (1, 2, 3): 'abc'}
t1=(1,[2,3])
# d[t1]='abc'# 报错：Traceback (most recent call last):... d[t1]='abc' TypeError: unhashable type: 'list'
s2.add(t)
print(s2) # 输出：{2, 3, 4, (1, 2, 3)}
#s2.add(t1) # 报错：Traceback (most recent call last):...s2.add(t1) TypeError: unhashable type: 'list'
print('------------------------------------------函数--------------------------------------------------------------')
print(int('123')) # 输出：123
print(int(12.34)) # 输出：12
print(int('123', base=8)) # 输出：83
print(int('123', base=16)) # 输出：291
# print(int('123', base=2)) # 报错：Traceback (most recent call last):... print(int('123', base=2))...ValueError: invalid literal for int() with base 2: '123'
print(int('10', base=2)) # 输出：2
print(int('123', base=10)) # 输出：123
print(float('123.456')) # 输出：123.456
print(float(12)) # 输出：12.0
print(str(123)) # 输出：'123'
print(str(12.34)) # 输出：'12.34'
print(bool(1)) # 输出：True
print(bool(0)) # 输出：False