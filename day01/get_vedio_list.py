# from urllib.parse import urljoin
import requests
# from bs4 import BeautifulSoup
from lxml import etree


UA_list = [
    {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
    {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
    {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)"},
    {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1"},
    {"User-Agent":"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"},
    {"User-Agent":"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11"},
    {"User-Agent":"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"},
    {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)"},
    {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"},
]

cookies = {
    '__cfduid': 'd50f15e9b7e8356cb72f9b62e90d52bfb1536461741',
    '__utmz': '142428154.1536461759.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)',
    'CLIPSHARE': 'dpmggskgi82g4hckvanas4gn05',
    'show_msg': '1',
    '__utmc': '142428154',
    '__51cke__': '',
    'watch_times': '3',
    '__utma': '142428154.141622933.1536461759.1537332924.1537341575.4',
    '__utmb': '142428154.0.10.1537341575',
    '__tins__3878067': '^%^7B^%^22sid^%^22^%^3A^%^201537341639733^%^2C^%^20^%^22vd^%^22^%^3A^%^206^%^2C^%^20^%^22expires^%^22^%^3A^%^201537343894597^%^7D',
    '__51laig__': '17',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


params = (
    ('next', 'watch'),
)

# 视频列表1-4462
# http://91.91p16.space/v.php?next=watch&page=4462
# base_url = "http://91.91p16.space/video.php?category=rf&page="
base_url = "http://91.91p16.space/v.php?next=watch&page="



def get_url_list(base_url):
    pass

# 使用requests发送HTTP请求，返回HTML的内容
def parse_url(url):
    res = requests.get(url, headers=headers, params=params, cookies=cookies)
    return res.text

# 通过HTML的内容获取里面的url列表
def get_content_list(content):
    html = etree.HTML(content)
    div_list = html.xpath("//div[@class='listchannel']")
    print(div_list)
    content_list = []
    for div in div_list:
        item = {}
        item["vedio_detail_url"] = div.xpath("./a/@href")[0] if len(div.xpath("./a/@href"))>0 else None
        item["title"] = div.xpath("./a/@title")[0] if len(div.xpath("./a/@title"))>0 else None
        item["image_url"] = div.xpath("./div/a/img/@src")[0]
        string = div.xpath("string(.)").replace(" ", "").replace("\n", "").replace("\t", "").strip().split(":")
        item["length"] = ":".join([string[1], string[2][:2]])
        item["added_time"] = string[3][:-2]
        item["author"] = string[4][:-2]
        item["views"] = string[5][:-3]
        item["star"] = string[6][:-2]
        item["comment"] = string[7][:-3]
        item["score"] = string[8]
        print("item %s", item)
        content_list.append(item)
    return content_list


# 获取视频网址
def get_video_url(detail_content):
    detail_html = etree.HTML(detail_content)
    url = detail_html.xpath("//video[@id='vid_html5_api']/source/@src")
    return url

# 保存内容
def save_content_list():
    pass

# 程序启动入口函数
def run():
    pass


if __name__ == "__main__":
    url = base_url + str(1)
    print(base_url)
    print(url)
    content = parse_url(url)
    
    content_list = get_content_list(content)
    # 取出视频详情页的视频网址
    for content in content_list:
        vedio_detail_url = content['vedio_detail_url']
        detail_content = parse_url(vedio_detail_url)
        vedio_url = get_video_url(detail_content)
        print(detail_content)


    print(content_list)
