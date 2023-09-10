#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from core.utils.http import HttpUtils
import time,re,requests
from bs4 import BeautifulSoup
import pandas


class TestScrapy(unittest.TestCase):
    def test_simple(self):
        data_list = []
        for i in range(1,2,1):
            print("正在爬取第" + str(i) + "页")
            #构建访问的网址，这个网址可有讲究了
            first = 'https://rate.tmall.com/list_detail_rate.htm?itemId=596452219968&spuId=1240258038&sellerId=1579115485&order=3&currentPage=1'
            last = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvB9vnvPgvUvCkvvvvvjiPn25pQjlhPFSv0jthPmPy6jiPR2MwAjnjRLF9gjlERphvCvvvphmjvpvhvUCvp8wCvvpvvhHhmphvLvUIUkUaQCAwe1O0747BhCka%2BoHoDOvfjLeAnhjEKBmAdXIaUExreTgcnkxb5ah6Hd8ram56D40OdiUDNrBlHd8reC69D70fd3J18heivpvUvvCCWUB0wV0EvpvVvpCmpJ2vKphv8vvvpHwvvvvvvvCmqvvvv4pvvhZLvvmCvvvvBBWvvvjwvvCHhQvvvxQCvpvVvUCvpvvv2QhvCvvvMMGtvpvhvvCvp86CvChh9P2s3QvvC0ODj6KHkoVQROhCvCLwMbra3rMwznsJWxS5gn1Uzvr4486Cvvyv9mQS7Qvvm4p%3D&needFold=0&_ksTS=1585406932472_453&callback=jsonp454'
            url = first + str(i) + last
            #访问的头文件，还带这个cookie
            headers ={
                # 用的哪个浏览器
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                # 从哪个页面发出的数据申请，每个网站可能略有不同
                'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.464b6bbfQwJmpT&id=596452219968&skuId=4313616443848&areaId=340700&user_id=1579115485&cat_id=2&is_b=1&rn=2aaf4f3d019121cb4b9c1816fe2eb360',
                # 哪个用户想要看数据，是游客还是注册用户,建议使用登录后的cookie
                'cookie':'tk_trace=1; cna=BPoFF17G1wkCASShM8zuMe/z; dnk=%5Cu6211%5Cu624B%5Cu673A%5Cu9762%5Cu5305; uc1=tag=10&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie14=UoTUP2Hg22VKGQ%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&lng=zh_CN&existShop=false&pas=0; uc3=nk2=rUtEsEAPxFiBAw%3D%3D&vt3=F8dBxd9vfOFX6TF0nIU%3D&lg2=UtASsssmOIJ0bQ%3D%3D&id2=UU20sOBlt5YjsA%3D%3D; tracknick=%5Cu6211%5Cu624B%5Cu673A%5Cu9762%5Cu5305; lid=%E6%88%91%E6%89%8B%E6%9C%BA%E9%9D%A2%E5%8C%85; _l_g_=Ug%3D%3D; uc4=nk4=0%40r7rCJKnwPLZ3%2FwyNCMllICP5es7j&id4=0%40U2%2Fz9fRgFErUiIbdThLAqnTeryYw; unb=2565225077; lgc=%5Cu6211%5Cu624B%5Cu673A%5Cu9762%5Cu5305; cookie1=VyVfQs3fk3Q1AMa82%2BACjr%2B92r264TDI3Q1c5WQuXXw%3D; login=true; cookie17=UU20sOBlt5YjsA%3D%3D; cookie2=1cf0a583503c0e1120b70f4ef312f5c5; _nk_=%5Cu6211%5Cu624B%5Cu673A%5Cu9762%5Cu5305; sgcookie=EilyrHs60A8pXOSQMCPEY; sg=%E5%8C%857f; t=0f46f0f89d1ad6a09a42a2e03e34c8ad; csg=af40d9de; _tb_token_=7e358e863e33f; enc=m7O0wanabkvr3U2e%2B%2FVwjIRhdoivog54aY5f614N4hBpuXKXuZzuCOP8Wqjk%2FohRVNzechJXzRihNyJDnIQHxw%3D%3D; l=dBOQ8BwlQB9FA9pWBOfwVsUBXgbOgIOb8sPzcQtKtICPOq1wBiJPWZ43uHTeCnGVh6JwR3laeFr4BMsXcnV0x6aNa6Fy_1Dmn; isg=BKOjn8dx-fVsPLXByTRwZsHRMuFNmDfaBnKiX9UB34JaFMI2XWiVKt1CDuQatI_S'
            }
            #尝试获取数据（这里的数据应该是从json里面获取的）
            try:
                data = requests.get(url,headers = headers).text
                time.sleep(10)
                result = re.findall('rateContent":"(.*?)"fromMall"',data)
                data_list.extend(result)
            except:
                print("本页爬取失败")
        df = pandas.DataFrame()
        df["评论"] = data_list
        df.to_excel("评论_汇总.xlsx")

if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    #suit.addTest(TestHttp("test_simple")) #把这个类中需要执行的测试用例加进去，有多条再加即可
    #suit.addTest(TestHttp("test_http_get_html")) #从上到下先后顺序
    #suit.addTest(TestHttp("test_http_post"))
    suit.addTest(TestScrapy("test_simple"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 