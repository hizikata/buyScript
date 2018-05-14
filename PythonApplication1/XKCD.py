#!python3
#!从 www.xkcd.com 连续下载图片

import requests,os,bs4

url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
print('current work directory：')
cwd=os.getcwd()
print(cwd)
while not url.endswith('#'):
    #下载网页
    print('Downloading page %s...' %url)
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,"html.parser")
    #找到图片所在的元素
    #匹配图片的选择器？
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('could not find comic image.')
    else:
        comicUrl='https:'+ comicElem[0].get('src')
        #下载图片
        print('Downloading image %s...' % (comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status()
    #将图片保存到./xkcd目录下
    imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #获取"下一张"按钮
    prevLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevLink.get('href')
print('Done')
