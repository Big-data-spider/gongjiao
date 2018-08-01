import pprint
import get_content
from time import sleep
import numpy
import json


def get_station(url):
    '''
    获取所有公交站
    :param url:
    :return:
    '''
    try:
        content, dom = get_content.get_content(url)
        line_name = dom.xpath('//div[@class="gj01_line_header clearfix"]/h1/text()')[0]
        go_list = dom.xpath('//ul[@class="gj01_line_img JS-up clearfix"]//li/a/text()')
        back_list = dom.xpath('//ul[@class="gj01_line_img JS-down clearfix"]//li/a/text()')
        station_list = list(set(go_list + back_list))
        line_info = {line_name: station_list}
        line_info['url'] = url
        pprint.pprint(line_info)
        return line_info
    except:
        print('惊了，竟然没获取到内容，快检查一下,20秒的时间')
        sleep(20)
        return None


def city_s_infos(content):
    f = open('./temp_file/city_s_infos.json', 'w', encoding='utf-8')
    cont = json.dumps(content, ensure_ascii=False, indent=4)
    f.write(cont)
    f.close()
    print('#' * 30 + '保存完成' + '#' * 30)


def all_infos(content):
    f = open('./res_file/all_infos.json', 'w', encoding='utf-8')
    cont = json.dumps(content, ensure_ascii=False, indent=4)
    f.write(cont)
    f.close()
    print('#' * 30 + '保存完成' + '#' * 30)


def save_one_info(content):
    f = open('./temp_file/one_infos.json', 'w', encoding='utf-8')
    cont = json.dumps(content, ensure_ascii=False, indent=4)
    f.write(cont)
    f.close()
    print('#' * 30 + '保存完成' + '#' * 30)


def get_urls():
    f = open('./work_file/lin_url.json', 'r', encoding='utf-8')
    jstr = json.load(f)
    f.close()

    return jstr


def fin_lists():
    f = open('./temp_file/one_infos.json', 'r', encoding='utf-8')
    fin_list = json.load(f)
    f.close()
    fin = []
    if len(fin_list) != 0:
        for its in fin_list:
            url = its.get('url')
            fin.append(url)
        fin = list(set(fin))

    return fin, fin_list


def get_all():
    '''
    获取全部站点名
    :return:
    '''
    jstr = get_urls()
    fin, fin_list = fin_lists()
    all_list = []
    stat_list = []
    one_lists = fin_list
    # 遍历获取并保存数据
    for dics in jstr:
        for cname, url_list in dics.items():
            for url in url_list:
                print(url)
                if url not in fin:
                    line_info = get_station(url)
                    if line_info != None:
                        pprint.pprint(line_info)
                        one_lists.append(line_info)
                        # one_lists = list(set(one_lists))
                        save_one_info(one_lists)
                        stat_list.append(line_info)
                        sleep(numpy.random.randint(3, 7))
                        print('\r\n' * 2 + '#' * 70 + '\r\n' * 2)
                else:
                    print('处理过了。下一个')
            city_line_list = {cname: stat_list}
            pprint.pprint(city_line_list)
            city_s_infos(city_line_list)
            print('\r\n' * 3 + '#' * 70 + '\r\n' * 3)
        all_list.append(city_line_list)
        # all_list = list(set(all_list))
        all_infos(all_list)
        pprint.pprint(all_list)
        print('\r\n' * 4 + '#' * 70 + '\r\n' * 4)


get_all()
