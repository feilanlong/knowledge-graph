import requests
import re

#下载网页内容
def download(keyword):

    url = 'http://baike.baidu.com/item/{}'.format(keyword)
    if url is None:
        return None
    else:
        print(f"抓取网址：{url}")
    # 浏览器请求头
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    headers={'User-Agent':user_agent}
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    return None

#提取百科词条简介
def get_data(html):
    #regex = re.compile('<meta name="description" content="(.*?)">')
    regex = re.compile('<div class="lemma-summary" label-module="lemmaSummary">(\s*?)<div class="para" label-module="para">([\s\S]*?)</div>\s*?</div>')
  
    #data = [('\n', 'Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。', '\n')]
    print(re.findall(regex, html))
    data = re.findall(regex, html)[0][1]
    print(data[0])
    return data

def save_data():
    #输入词条
    keyword = input('please input keyword:')
    html_cont = download(keyword)
    path = 'data/'+keyword+'.txt'
    try:
        data = get_data(html_cont)
        data = re.sub(r'<[\s\S]*?>|&nbsp;|\n|\s','',data)
        print(data)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
            f.close()
        print("爬取数据保存成功！")
        return path,keyword
    except Exception as e:
        print("错误：",e)
        print(keyword, 'is not exist,crawl failed !')
    
if __name__ == '__main__':
    save_data()
