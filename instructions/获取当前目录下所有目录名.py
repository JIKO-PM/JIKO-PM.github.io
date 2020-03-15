import os,sys,xlwt
dir1=os.walk(sys.path[0])
all=[]
dir=[]
for root,dirs,files in dir1:
    all.append(dirs)
for i in all[0]:
    dir.append(i)
print(dir)
file= xlwt.Workbook()
table = file.add_sheet('1')
for i in range(len(dir)):
    table.write(i,0,dir[i])

#file.save('文件夹列表.xls')
