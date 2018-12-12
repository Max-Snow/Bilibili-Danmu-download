import urllib;
import requests;
lis=range(1284780,1284819+1);
i=1
for num in lis:
  url='http://comment.bilibili.com/'+str(num)+'.xml';
  data=requests.get(url);
  with open('天龙八部'+str(i)+'.xml',"wb") as f:
    f.write(data.content);
    i=i+1;
