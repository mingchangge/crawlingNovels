# coding: utf-8 #勿删，删除过，之后终端会有乱码
'''
仅限用于研究代码
勿用于商业用途
请于24小时内删除

使用单线程的爬取方式--只爬取前三章
'''

import time
import requests as Request
import re
from random import choice
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
from colorama import init
from termcolor import colored
from readchar import  readkey

# 定义全局变量
FGS = ['green', 'yellow', 'blue', 'cyan', 'magenta', 'red']
# 基础url
baseUrl = 'https://fuxs1.com/'
# 书籍类型
catalog = 'chuanyue'
# 书籍ID
book_id = 24061
# 章节列表
chapters_list = []
# 创建会话，便于维持长链接
session = Request.Session()
# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}

# 获取并解析html内容
def get_html_content(url):
    '''
    获取html内容
    :param url:
    :return: html内容
    '''
    # 发送请求
    time.sleep(choice(range(1, 10))) # 随机延时-模拟人类行为，随机延时1-9秒
    print("地址--------------：", url)
    response = session.get(url,headers=headers)
    response.raise_for_status()  # 检查请求是否成功
    response.encoding = 'utf-8'  # 设置编码格式
    # 解析 HTML 文档
    # soup = bf(response.text, 'lxml')
    # 没有安装lxml，使用 BeautifulSoup 库来解析 HTML 文档
    return bf(response.text,'html.parser')

# 遍历章节列表，获取章节内容，将所有章节内容拼接成一篇文章
def get_chapter_detail(chapters_list):
    '''
    获取章节内容
    :param chapters_list:
    :return: 章节内容
    '''
    # 存储所有章节内容的字符串
    book_content = ""
    for chapter in chapters_list:
        chapter_url = chapter['href']
        soup = get_html_content(f"{baseUrl}{chapter_url}")
        content_div = soup.find('div', class_='co-by').get_text()
        if content_div:
          book_content += content_div + "\n\n"  
    return book_content

# 下载txt文件
def download_txt(book_title,book):
    file_name = book_title + '.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(book.replace('\u3000\u3000', '\n'))
    print(colored(f'文件 {file_name} 下载完成！',choice(FGS)))


# 获取书籍列表
def book_page_list(catalog,book_id):
    '''
    通过传入的catalog,book_id,获取此书的所有章节目录
    :param catalog:
    :param book_id:
    :return: 章节目录及章节地址
    '''
    soup = get_html_content(f"{baseUrl}/{catalog}/{book_id}.html")
    book_title = soup.find('title').get_text()
    book_describe = soup.find('div', class_='co-by').get_text()
    # 查找所有章节，返回一个列表（第一页无href属性被剔除）
    chapters_list= soup.find('div', class_='xiapage').find_all('a', string=re.compile(r'^\d+$'), href=True)
    # 获取章节内容-只爬取前三章
    book_content = get_chapter_detail(chapters_list[:3])
    #book_content = get_chapter_detail(chapters_list)
    book = book_title+ "\n\n"+ book_describe+ "\n\n"+ book_content
    print(colored(f"书名:{book_title}",choice(FGS)))
    print(colored(f"简介:{book_describe}",choice(FGS)))
    # 下载txt文件
    download_txt(book_title,book)



# 读取键盘输入
init() ## 命令行输出彩色文字
print(colored('已搜索完毕！',choice(FGS)))
print(colored('x:全部下载',choice(FGS)))
print(colored('q:退出阅读',choice(FGS)))
# 定义键盘输入
my_key = ['q','x']
t1=None
# 读取键盘输入
while True:
    while True:
        move = readkey()
        if move in my_key:
            break
    if move == 'q': ## 键盘‘Q’是退出
        break  
    if move == 'x':  ## 这里只是演示为主，不循环下载所有数据了
        print('#' * 50)
        t1 = time.time()  # 开始时间
        book_page_list(catalog,book_id)
        break

t2 = time.time()  # 结束时间
print(colored(f"下载完成，耗时{t2-t1:.2f}秒", choice(FGS)))
print('#' * 50)

