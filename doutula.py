# !/usr/bin/python3

# 导入request pip install requests
import requests
import parsel
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


def validate_title(title):
    reg = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(reg, "_", title)  # 替换为下划线
    return new_title


def data_each(data):
    # 对结果列表进行循环
    for item in data:
        # 获取每张图片的 alt 值作为图片名
        title = item.xpath('./img/@alt').get()

        # 替换不符合图片命名规则的字符
        new_title = validate_title(title)

        # 获取图片地址 url
        img_url = item.xpath('./img/@data-original').get()

        # 拼接图片名称
        all_title = new_title + '.' + img_url.split('.')[-1]
        print('保存完成：', all_title)

        # 抓取图片并进行二进制转换
        img_data = requests.get(url=img_url, headers=headers).content

        # 保存图片到本地同级目录 images 下
        with open('images\\' + all_title, mode='wb') as file:
            file.write(img_data)


for page in range(1, 3611):
    print('===============正在抓取第 {} 页数据================'.format(page))

    # 获取要抓取的页面地址
    url = 'https://www.doutula.com/photo/list/?page={}'.format(str(page))

    # 模拟浏览器请求
    response = requests.get(url=url, headers=headers)

    # 获取抓取的页面源代码
    html_data = response.text

    # 解析源代码为正常的 html
    selector = parsel.Selector(html_data)

    # 利用 xpath 解析出符合特征的元素信息
    resp_list = selector.xpath('//a[@class="col-xs-6 col-sm-3"]')

    data_each(resp_list)