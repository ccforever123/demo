import re
import requests
import json

def get_dict(page_source):
    sub_link_dict = {}
    reg_title = r'<div class="bookMl\"><strong>(.*?)</strong>.*?height:auto;\">(.*?)</div>'
    title_list = re.findall(reg_title, page_source, re.S)
    for i in title_list:
        reg_link = r'href=\"(.*?)\">(.*?)</a>'
        link_list = re.findall(reg_link, i[1])
        sub_link = {}
        for j in link_list:
            sub_link[j[1]] = get_sub_info(j[0])
#            print(j[1])
        sub_link_dict[i[0]] = sub_link
        print(sub_link_dict)
        save2json(sub_link_dict)

def get_sub_info(url):
    r = requests.get(url)
    page_source = r.text
    reg_content = r'<b>(.*?)</b>.*?<div class="contson">\n(.*?)\n</div>'
    info = re.findall(reg_content, page_source, re.S)
    title = info[0][0]
    content = info[0][1]
    reg_content = r'<p><strong>(.*?)</strong><br />(.*?)</p>'
    content = re.findall(reg_content, content)
    print(title, content)
    return (title, content)


def save2json(data):
    with open('bencao.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))


def main():
    url = 'https://www.gushiwen.org/guwen/bencao.aspx'
    r = requests.get(url)
    page_source = r.text
    get_dict(page_source)


def replace():
    with open('bencao.json', 'r', encoding='utf-8') as f:
        content = f.read()
    content = json.loads(content)
    for i in content:
#        print(i)
        for j in content[i]:
            reg_log = r'<p><strong>(.*?)</strong><br />(.*?)</p>'
            log = re.findall(reg_log, content[i][j][1])
            str_log = ''
            print(log)
            for i in log:
                str_i = '{}\n{}\n\n'.format(i[0], i[1].replace('<br />', '\n'))
                str_log +=str_i
                print(str_i)

#    print('new:{}'.format(content))
#    with open('bencao.json', 'w', encoding='utf-8') as f:
#        f.write(content)



if __name__ == '__main__':
    main()