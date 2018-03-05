from knowit import know
import os
pathname = r"C:\Users\wangh\Downloads\stanford _machine_learning"
filenames = [x for x in os.listdir(pathname) if os.path.splitext(x)[1] == '.mkv']
# filenames = [x for x in os.listdir(pathname) if os.path.isfile(x) and os.path.splitext(x)[1] == '.mkv']
filenames.sort(key=lambda x:int(x[:2])) #列出所有视屏文件并排序
duration_time = []
for i in filenames:
    print(know(pathname+'\\'+i)['duration'],i)

    # duration_time =duration_time.append(know(filename+'.'+i)['duration'])

# print(filenames)
# filename = r"C:\Users\wangh\Downloads\stanford _machine_learning\1.mkv"
# duration_time = know(filename)['duration']
