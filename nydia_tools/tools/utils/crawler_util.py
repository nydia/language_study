import requests
from bs4 import BeautifulSoup
import re
import csv
import json
from datetime import datetime
import os

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_latest_news():
    url = 'https://news.sina.com.cn/'
    
    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'  # 设置编码
        
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取新闻数据（根据实际网页结构调整选择器）
        news_list = []
        for item in soup.select('.news-item'):
            if len(item.select('h2')) > 0:
                title = item.select('h2 a')[0].text.strip()
                link = item.select('h2 a')[0]['href']
                time_source = item.select('.time')[0].text if item.select('.time') else '未知时间'
                
                # 提取纯文本时间
                time = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', time_source).group() if time_source else '未知时间'
                
                news_list.append({
                    'title': title,
                    'link': link,
                    'time': time
                })

        return news_list[:10]  # 返回最新的10条新闻
    
    except Exception as e:
        print(f"爬取失败: {str(e)}")
        return []

def save_to_file(data, save_dir='news_data', filename='news', format='txt'):
    """保存数据到指定目录"""
    try:
        # 处理路径中的波浪线（~）和空格
        expanded_dir = os.path.expanduser(save_dir)
        expanded_dir = os.path.abspath(expanded_dir)
        
        # 创建保存目录（如果不存在）
        os.makedirs(expanded_dir, exist_ok=True)
        
        # 生成带时间戳的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename}_{timestamp}.{format}"
        full_path = os.path.join(expanded_dir, filename)
        
        # 根据格式保存文件（保持原有逻辑不变）
        # ...（与之前相同的保存逻辑）

        print(f"数据已保存到：{full_path}")
        return True
    
    except Exception as e:
        print(f"文件保存失败: {str(e)}")
        print(f"请检查目录权限或路径有效性：{save_dir}")
        return False

if __name__ == "__main__":
    # 获取新闻数据
    news_data = get_latest_news()
    
    if news_data:
        # 示例：保存到不同目录（按需修改）
        save_to_file(news_data, 
                    save_dir='~/Desktop/news_archive',  # 保存到桌面
                    format='json')
        
        save_to_file(news_data,
                    save_dir='/Users/Shared/news_data',  # 系统共享目录
                    format='csv')
        
        save_to_file(news_data,
                    save_dir='../backup_data',  # 上级目录中的文件夹
                    format='txt')
    else:
        print("没有获取到新闻数据")