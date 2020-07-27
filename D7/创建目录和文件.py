import os
os.chdir('/root/Python-test/')
# os.mkdir('test')
os.chdir('/root/Python-test/test/test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
os.chdir('/root/Python-test/test/test')

print('文件中包含“qytang”关键字的文件为：')
for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_or_dir):
        for line in open(file_or_dir):
            if 'qytang' in  line:
                print('\t' + file_or_dir)
                break
# if 'qytang' in open((os.listdir(os.getcwd())[1]),'r').read():
#     print(f'{os.listdir(os.getcwd())[1]:>10}')
# else:'e'

#print({'dir':'file'})

