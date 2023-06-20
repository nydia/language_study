import urllib.request;


def getHtml(url):  # 获取html的内容
    html = urllib.request.urlopen(url).read()  # bytes 如果不用read()，html会是一个↓
    return html                                # http.client.HTTPResponse的变量


def saveHtml(fileName, fileContent):
    with open(fileName, "wb") as f:  # 以wb打开文件
        f.write(fileContent)  # 写入


def main():
    url = "https://www.javamall.com.cn/docs/7.2.3_upgrade/standard/dev-flow"  # url
    html = getHtml(url)  # 调用函数获取bytes
    saveHtml("C:\temp\javashop.html", html)  # 保存
    print("保存网页完成")  # 提示语


if __name__ == "__main__":  # 主函数
    main()