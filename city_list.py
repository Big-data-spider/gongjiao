import pprint
import get_content
from time import sleep
import numpy
import json


def get_city_list():
    '''
    获取城市主页列表
    :return:
    '''
    url = 'http://www.gongjiao.com/'
    content, dom = get_content.get_content(url)
    city_list = dom.xpath('//div[@class="g-cities2"]/dl//dd//a/@href')
    pprint.pprint(city_list)
    city_list = list(set(city_list))
    return city_list


def get_all_line():
    '''
    获取所有线路的详情页url
    :return:
    '''
    print('#' * 70)
    cilist = get_city_list()
    all_linse = []
    for city in cilist:
        city = city + 'lines_all.html'

        print(city)
        content, dom = get_content.get_content(city)
        city_name = dom.xpath('//div[@class="f-fl"]/a/span/text()')[0]
        city_linse = dom.xpath('//div[@class="list"]/ul//li/a/@href')
        print('#' * 70)
        print(city_name)
        print(city_linse)

        city_dict = {city_name: city_linse}
        all_linse.append(city_dict)

        sleep(numpy.random.randint(3, 6))

    jstr = json.dumps(all_linse, ensure_ascii=False, indent=4)
    f = open('./work_file/lin_url.json', 'w', encoding='utf-8')
    f.write(jstr)
    f.close()


get_all_line()
