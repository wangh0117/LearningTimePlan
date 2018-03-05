from knowit import know
import os
pathname = r"C:\Users\wangh\Downloads\stanford _machine_learning"
filenames = [x for x in os.listdir(pathname) if os.path.splitext(x)[1] == '.mkv']
# filenames = [x for x in os.listdir(pathname) if os.path.isfile(x) and os.path.splitext(x)[1] == '.mkv']
filenames.sort(key=lambda x:int(x[:2])) #列出所有视屏文件并排序
duration_time = []
for i in filenames:
    duration_time.append(know(pathname+'\\'+i)['duration'].seconds)
# print(duration_time)
sum_time = sum([x for x in duration_time if x <1000])
print('total learning time is {} hour {} minutes'.format(int(sum_time/360),int((sum_time-int(sum_time/360)*360)/60)))
# print(filenames)
# filename = r"C:\Users\wangh\Downloads\stanford _machine_learning\1.mkv"
# duration_time = know(filename)['duration']
