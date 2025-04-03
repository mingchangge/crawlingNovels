# coding: utf-8
'''
仅限用于研究代码
勿用于商业用途
请于24小时内删除

使用异步协程的爬取方式--完整版
安装依赖命令：
./.venv/bin/python -m pip install beautifulsoup4 colorama termcolor readchar requests
安装异步协程爬取依赖
./.venv/bin/python -m pip install asyncio aiohttp
'''

import time
# 导入Python的正则表达式模块 re，它提供了处理字符串模式匹配的功能
import re
# 从Python的内置模块random中导入两个函数 choice。
from random import choice
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入在命令行中输出彩色文本的库
from colorama import init
# 导入为终端文本添加颜色和样式的库
from termcolor import colored
# 导入读取键盘输入的库
from readchar import  readkey
# 导入异步库
import asyncio
import aiohttp

# 定义全局变量
FGS = ['green', 'yellow', 'blue', 'cyan', 'magenta', 'red']
# 基础url
baseUrl = 'https://fuxs1.com/'
# 书籍类型
catalog = 'chuanyue'
# 书籍ID
book_id = 24105
# 章节列表
chapters_list = []
# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
# 最大并发量
MAX_NUM = 10 

# 获取并解析html内容
async def get_html_content(url):
    '''
    获取html内容
    :param url:
    :return: html内容
    '''
    # 限制最大并发量
    async with asyncio.Semaphore(MAX_NUM):
        # 发送请求
        async with aiohttp.ClientSession(headers=headers) as session:
            print("地址--------------：", url)
            async with session.get(url) as response:
                # 随机延时-模拟人类行为，随机延时1-9秒
                await asyncio.sleep(choice(range(1, 10)))
                # 手动设置编码
                response.encoding = 'utf-8'  
                # 检查请求是否成功   
                if response.status == 200:
                    html = await response.text()
                    soup = bf(html, 'html.parser')
                    return soup
                else:
                    print(colored(f"请求失败，状态码：{response.status}", choice(FGS)))
                    return None

# 遍历章节列表，获取章节内容，将所有章节内容拼接成一篇文章
async def get_chapter_detail(chapters_list):
    '''
    获取章节内容
    :param chapters_list:
    :return: 章节内容
    '''
    # 存储所有章节（除第一页）内容的字符串
    book_content = ""
    # 创建异步任务列表
    task_list = []
    # 遍历章节列表，获取章节内容
    for chapter in chapters_list:
        chapter_url = chapter['href']
        # 插入异步操作-使用create_task()方法来创建asyncio的并发任务
        task_list.append(asyncio.create_task(get_html_content(f"{baseUrl}{chapter_url}")))
        results = await asyncio.gather(*task_list)
    # 遍历请求返回的结果
    for result in results:
        if result:
            # 获取章节内容
            content_div = result.find('div', class_='co-by').get_text()
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
async def book_page_list(catalog,book_id):
    '''
    通过传入的catalog,book_id,获取此书的所有章节目录
    :param catalog:
    :param book_id:
    :return: 章节目录及章节地址
    '''
    soup = await get_html_content(f"{baseUrl}/{catalog}/{book_id}.html")
    book_title = soup.find('title').get_text()
    # 获取书籍内容-第一页内容获取
    book_describe = soup.find('div', class_='co-by').get_text()
    # 获取所有章节，返回一个列表（第一页无href属性被剔除）
    chapters_list= soup.find('div', class_='xiapage').find_all('a', string=re.compile(r'^\d+$'), href=True)
    # 获取章节内容
    book_content = await get_chapter_detail(chapters_list)
    print(colored(f"书名:{book_title}",choice(FGS)))
    print(colored(f"简介:{book_describe}",choice(FGS)))
    book = book_title+ "\n\n"+ book_describe+ "\n\n"+ book_content
    # 下载txt文件
    download_txt(book_title,book)


async def main():
    # 初始化 colorama,确保在不同操作系统（如 Windows 和 Unix 系统）上正确显示彩色文本。
    init()
    # 打印信息
    print(colored('已搜索完毕！',choice(FGS)))
    print(colored('x:全部下载',choice(FGS)))
    print(colored('q:退出阅读',choice(FGS)))
    # 定义键盘输入
    my_key = ['q','x']

    move=None
    # 等待用户输入
    while move not in my_key:
        move = readkey()
        print(colored('请按下 x 或 q 键继续', choice(FGS)))
    # 根据用户输入执行操作
    if move == 'q':  # 用户按下 'q' 键退出
        print(colored("退出程序", choice(FGS)))
        return

    if move == 'x':  # 用户按下 'x' 键开始下载
        print('#' * 50)
        t1 = time.time()  # 开始时间
        await book_page_list(catalog, book_id)
        t2 = time.time()  # 结束时间
        print(colored(f"下载完成，耗时{t2-t1:.2f}秒", choice(FGS)))
        print('#' * 50)
        return
# 调用main函数
asyncio.run(main())


