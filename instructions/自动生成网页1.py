from PIL import Image
import os, sys,qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import *
header="""<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="author" content="Administrator">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <style type="text/css">
    <!--
    .s1 {
      font-family: monospace;
      font-weight: normal;
      font-size: 30pt;
    }

    p {
      text-align: center;
      font-family: monospace;
      font-weight: normal;
      font-size: 20pt;
    }

    .s2 {
      font-family: monospace;
      font-weight: normal;
      font-size: 16pt;
    }

    .s3 {
      color: #F90;
      font-family: monospace;
      font-weight: normal;
      text-decoration: underline;
      font-size: 12pt;
    }
        img {
        background-size:contain|cover;
        width:100%;
        height: auto;
        pointer-events: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
}
    div {width="100%"; height=auto}
    -->
  </style>
</head>

<body>
<div style="text-align: center;width:100%;">"""


def openwin1():    
 root = tk.Tk()
 root.withdraw()
 filepath = filedialog.askopenfilenames(title=u'打开图片目录')
 return filepath   

def renam():
 i=1
 newfile=[]
 for j in range(len(filepath)):
    k = "%03d" % i
    path = os.path.dirname(filepath[i-1])
    os.rename(filepath[i-1],path+"/"+k+".jpg")
    newfile.append(k+".jpg")
    i=i+1     
 return newfile

 
'''
def fname():
  root = tk.Tk()
  root.withdraw()
  fname=filedialog.asksaveasfilename(title=u'菫晏ｭ路TML譁?莉ｶ', filetypes=[("HTML", ".html")])+".html"
  return fname
'''  
   
    

 
def gettitle():
    global title
    title=en.get()
    root.destroy()
def gettitle2():
 global root
 root = tk.Tk()
 root.title('输入标题')
 rowidth=root.winfo_screenwidth()
 roheight=root.winfo_screenheight()
 alignstr = '%dx%d+%d+%d' % (400, 200, (rowidth-200)/2, (roheight-100)/2)
 root.geometry(alignstr)
 global en
 en=Entry(root,show=None,width="45")
 en.pack()
 tk.Button(root,text="确定",command=gettitle).pack() #command扈大ｮ夊執蜿匁枚譛ｬ譯?蜀?螳ｹ譁ｹ豕?
 root.mainloop()
 return title

def makehtml():
    f=open(dirname1+".html",'w',encoding='utf-8')
    f.write(body)
    f.close

def makeqrcode():
    img = qrcode.make(qrcodeurl)
    img= img.convert("RGBA")
    img.save("qr_code.png")





title=gettitle2().capitalize()+" Paper Model Instruction"
title= """<p class="s1">"""+title+"""</p>"""
filepath=openwin1()
dirname=filepath[0]

end_pos = dirname.rfind('/')  # 蛟呈焚隨ｬ荳荳ｪ"/"逧?菴咲ｽｮ蜀榊ｷｦ遘ｻ荳菴?
start_pos = dirname.rfind('/', 0, end_pos)+1  # 鄂大捩莉主ｼ蟋区穐閾ｳ蛻ｰend_pos逧?菴咲ｽｮ?ｼ御ｻ主承蠕蟾ｦ蜃ｺ邇ｰ逧?隨ｬ荳荳ｪ"/"荵溷ｰｱ譏ｯ謌台ｻｬ隕∵伽逧?蛟呈焚隨ｬ莠御ｸｪ"/"
dirname1 = dirname[slice(start_pos,end_pos)]  # 謌ｪ蜿也ｽ大捩逧?蛟呈焚隨ｬ莠御ｸｪ "/" 蜷朱擇逧?蜀?螳ｹ

newfile=renam()
urls=""
for j in newfile:
    j=dirname1+"/"+j
    j="""<img src=\""""+j+"""\">"""
    urls=urls+j
#fname=fname()
qrcodeurl="https://jiko-pm.github.io/instructions/"+dirname1+".html"
print(qrcodeurl)
print(urls)

urls=urls+"""</div></body>"""
body=header+title+urls
makehtml()
makeqrcode()





