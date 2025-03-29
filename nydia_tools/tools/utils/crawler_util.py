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

def save_to_file(data, filename='news', format='txt'):
    """保存数据到本地文件"""
    try:
        # 创建保存目录（如果不存在）
        os.makedirs('news_data', exist_ok=True)
        
        # 生成带时间戳的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"news_data/{filename}_{timestamp}.{format}"
        
        # 根据格式保存文件
        if format == 'txt':
            with open(filename, 'w', encoding='utf-8') as f:
                for idx, item in enumerate(data, 1):
                    f.write(f"{idx}. [{item['time']}] {item['title']}\n")
                    f.write(f"   链接: {item['link']}\n\n")
        
        elif format == 'csv':
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['序号', '时间', '标题', '链接'])
                for idx, item in enumerate(data, 1):
                    writer.writerow([idx, item['time'], item['title'], item['link']])
        
        elif format == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"数据已保存到：{os.path.abspath(filename)}")
        return True
    
    except Exception as e:
        print(f"文件保存失败: {str(e)}")
        return False

if __name__ == "__main__":
    # 获取新闻数据
    news_data = get_latest_news()
    
    if news_data:
        # 同时保存三种格式
        save_to_file(news_data, format='txt')
        save_to_file(news_data, format='csv')
        save_to_file(news_data, format='json')
        
        # 打印前3条结果预览
        print("\n最新新闻预览：")
        for idx, news in enumerate(news_data[:3], 1):
            print(f"{idx}. [{news['time']}] {news['title']}")
    else:
        print("没有获取到新闻数据")