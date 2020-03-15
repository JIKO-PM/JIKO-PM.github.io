from PIL import Image
import os, sys,qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os,sys,xlwt
dir1=os.walk(sys.path[0])
all=[]
dir=[]
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



 


def makehtml():
    f=open("tianqi"+".html",'w',encoding='utf-8')
    f.write(body)
    f.close










for root,dirs,files in dir1:
    all.append(dirs)
for i in all[0]:
    dir.append(i)
urls=""
j=0
for i in dir:
    urlsx="<a href=\"https://jiko-pm.github.io/instructions/"+dir[j]+"\">"+dir[j]+"</a></br>"
    urls=urls+urlsx
    j=j+1

title="<p class="+"s1"+">"+"说明书超链接"+"</p>"

urls=urls+"""</div></body>"""
body=header+title+urls
makehtml()





