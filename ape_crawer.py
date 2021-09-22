import requests
import re
from bs4 import BeautifulSoup


def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.text


def get_content(html, page):
    output = """第{}页 song：{} baiduyun：{} password：{} \n"""
    soup = BeautifulSoup(html, 'html.parser')
    con_list = soup.find_all('div', class_='download')
    # for i in con_list:
    #     a = i.find('div', class_='ips').find('input', class_='path').get('value')
    #     print("77777", type(a))
    #     print("55555", a)
    #     print("66666", a.string[3:7])
    # # a = con_list.input['value']
    # print("55555", a)
    # for i in con_list[0]:
    #     print("44444", i)
    #     a = con_list.input['value']
    #     print("55555", a)
        # a = con_list.find('input')
        # print("333333", a.get_text())
    # print(con_list)
    for i in con_list:
        # d=i.find('a').get('href')  
        # print(type(i))
        e=i.get('href')
    # c=con_list.find_all(name='baidu',attrs={"href":re.compile(r'^http:')})
        # print("333333", e)
        # print("1111", d)
    
    # for i in con_list:
    #     print("11111", i)
    #     url = con_list.get('href')
    #     url_lst.append(url)
    #     print("2222", url)
    # url_lst = list(filter(lambda url_str: 'http' in url_str, url_lst))
    # print(url_lst)
    # b = con_list.find_all(href = re. compile ( 'pan.baidu.com' ))
    


    for i in con_list:
        # print(i)
        # print(i.find('div', class_='tit'))
        print(type(i.find('div', class_='tit').string))
        name = i.find('div', class_='tit').string[9:30]  # 获取名字
        print("密码为", name)
        code = i.find('div', class_='_tips').string[3:7]  # 获取密码
        print("密码为", code)
        html = soup.find('div', class_='ips').find('input', class_='path').get('value')# 获取网址
        print("网址为", html)
        save_txt(output.format(page, name, html, code))


def save_txt(*args):
    for i in args:
        with open('ape1.txt', 'a', encoding='utf-8') as f:
            f.write(i)

def save_json(*args):
    name = ['page','name','html','password']
    filename='ape.json'
    for i in args:
        with open(filename,'w') as file_obj:
            json.dump(name,file_obj)


def main():
    # 我们点击下面链接，在页面下方可以看到共有13页，可以构造如下 url，
    # 当然我们最好是用 Beautiful Soup找到页面底部有多少页。
    for i in range(1, 50000):
        try:
            url = 'https://www.ape8.cn/music/{}.html'.format(i) 
            html = download_page(url)
            get_content(html, i)
        except:
            print("{}行异常退出".format(i))
            continue

if __name__ == '__main__':
    main()
