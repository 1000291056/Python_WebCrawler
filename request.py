import requests
import os
from xpinyin import Pinyin
from bs4 import BeautifulSoup 
from bs4 import  SoupStrainer
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
def getAllNamesForGirls(url):
    namesForGirls=set()
    r= requests.get(url)
    r.encoding="utf-8"
    content=r.text
    #only_tag=SoupStrainer("div",class_="i_cont_s")
    bs=BeautifulSoup(content,"html.parser")
    divs= bs.findAll("div",class_="i_cont_s")
    for div_ in divs:
        tag_as=div_.children
        print(tag_as)
        for a in tag_as:
            if a.has_attr("title"):
                print(a["title"])
                name=a["title"]
                print(name)
                #name=Pinyin.get_pinyin(name)
                if not name.strip():
                   namesForGirls.add(name)           
            
    return namesForGirls
def gernerateUrls(namesForGrils):
    urls=set()
    for name_gril in namesForGrils:
        urls.add ("http://www.win4000.com/mt/"+name_gril+".html")
        
def downLoad(imgs):
    if len(imgs)<=0:
        print("no volid url")
    else:
        print("start download..........................................")
        #del_file(basePATH)
    while len(imgs)>0:
       img_temp=imgs.pop()
       print(img_temp)
       r_img= requests.get(img_temp)
       img_temp_frag=img_temp.split("/")
       file_name=img_temp_frag[len(img_temp_frag)-1]
       path=basePATH+os.sep+file_name
       print(path)
       fo=open(path,"wb+")
       fo.write(r_img.content)
       fo.close()
       pass    
url="http://www.win4000.com/mt/zhaoliying.html"
url_names="http://www.manmankan.com/dy2013/mingxing/neidi/nvmingxing.shtml"
basePATH="C:\\Users\\temp\\Desktop\\image"

downLoad(gernerateUrls(getAllNamesForGirls(url_names)))
#get all tag:img
#for img in bs.findAll("img"):
   

#r_weathor=requests.get(url_json)
#print(r_weathor.json())
