department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456
DN1= 'Department1 name'
DN2= 'Department2 name'
M= 'Manager'
CF='COURSE FEES'
line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department2,depart2_m,COURSE_FEES_Python)
line3 = '{:<10}:{:<10} {:<6}:{:<10} {:>10}:{:<10.2f} {:<5}'.format(DN1,department1,M,depart1_m,CF,COURSE_FEES_SEC,"The End！")
line4 = '{:<10}:{:<10} {:<6}:{:<10} {:>10}:{:<10.2f} {:<5}'.format(DN2,department2,M,depart2_m,CF,COURSE_FEES_Python,"The End！")
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
length = len(line1)
print('='*length)
print(line3)
print(line4)
print('='*length)