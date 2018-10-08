import requests
import datetime
import os
import random
import time
from urllib.parse import urljoin

# User-Agent
header_list = [
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

pre_url_list = ["http://185.38.13.159/mp43/", "http://192.240.120.34/mp43/"]
suffix_url_list = [".mp4?st=GBI3QC_suurx7X6reuAMKw&amp;e=1537406494", ".mp4?st=sg-NUiPH1HkrF5paqXc_CQ&e=1537323311"]

for i in range(37966, 290000):
    # url = 'http://192.240.120.34//mp43/6000.mp4?st=sg-NUiPH1HkrF5paqXc_CQ&e=1537323311'
    
    index = random.randrange(0, 2)
    pre_url = pre_url_list[index]
    suffix_url = suffix_url_list[index]

    header = random.choice(header_list)
    url = urljoin(pre_url, str(i)+suffix_url)

    start_time = datetime.datetime.now()
    print('开始输出时间{}'.format(start_time))
    start_down_time = datetime.datetime.now()
    print('开始下载时间{}'.format(start_down_time))

    # 请求要下载的url地址
    attempts = 1
    success = False
    while attempts < 10 and not success:
        try:
            html = requests.get(url, headers=header, timeout=5)
            # content返回的是bytes型也就是二进制的数据。
            html = html.content
            success = True
            print('第{}次HTTP请求成功'.format(attempts))
        except:
            attempts += 1
            time.sleep(5)
            if attempts == 10:
                break

    file_name = os.path.join("E:/video", str(i)+".mp4")
    print(file_name)
    print(url)
    with open(file_name,'wb') as f:
        f.write(html)
    end_time = datetime.datetime.now()
    print('下载结束时间{}'.format(end_time))
    if end_time-start_time < datetime.timedelta(5):
        number = 5
    else:
        number = random.randrange(15, 30)
    time.sleep(number)
    print('程序暂停了{}'.format(number))
    

