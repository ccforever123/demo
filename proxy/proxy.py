import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getProxy():
    headers = {"User-Agent": "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}
    url = 'https://www.xicidaili.com/'
    source = getSource(url, headers)
    ip_list = getIps(source)
    ip_list_comfirmed = verifyProxy(ip_list, headers)
    for ip in ip_list_comfirmed:
        print('ip: {}'.format(ip))

def getSource(url, headers):
    r = requests.get(url, verify=False, headers=headers)
    r.encoding = r.apparent_encoding
    source = r.text
    # print(source)
    return source


def getIps(source):
    ip_list = []
    reg_ips = re.compile(r'<td class=\"country\"><img src=\"//fs.xicidaili.com/.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td class=\"country\">(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>', re.S)
    ips = reg_ips.findall(source)
    for item in ips:
        ip = item[0]
        port = item[1]
        address = item[2]
        anonymous = item[3]
        proxy_type = item[4].lower()
        lifetime = item[5]
        verifytime = item[6]
        if anonymous == '高匿':
            proxy = '{}://{}:{}'.format(proxy_type, ip, port)
            ip_dict = {
                "address": address,
                "proxy": proxy,
                "proxy_type": proxy_type,
                "lifetime": lifetime,
                "verifytime": verifytime
            }
            ip_list.append(ip_dict)
    return ip_list


def verifyProxy(ip_list, headers):
    ip_list_comfirmed = []
    
    for item in ip_list:
        proxy = item['proxy']
        proxy_type = item['proxy_type']
        checkResult = checkProxy(proxy, proxy_type, headers)
        if checkResult == True:
            ip_list_comfirmed.append(item)
        else:
            print('{} is invild.'.format(proxy))
    return ip_list_comfirmed


def checkProxy(proxy, proxy_type, headers):
    web_proxy_type = 'http'
    url = '{}://m.jd.com'.format(proxy_type)
    if proxy_type == web_proxy_type:
        proxies = {"https": proxy}
        try:
            r = requests.get(url, verify=False, headers=headers, proxies=proxies, timeout=10)
            status_code = r.status_code
            if status_code == 200:
                return True
            return False
        except:
            pass

if __name__ == "__main__":
    getProxy()