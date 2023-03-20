####### 1) პროგრამამ უნდა დათვალოს რამდენჯერ განმეორდა ერთი და იგივე ელემენტები ლისტში.
# list1 =  ['hi', 'hello', 'hi', 'hi','bye', 'no']
# for i in list1:
#     qntt = (i, 'გამეორდა', list1.count(i), 'ჯერ')
#     print (qntt)
##### იგივე ამოცანა, count() მეთოდის გარეშე
# list1 =  ['hi', 'hello', 'hi', 'hi','bye', 'no']
# set1_list1 = list(set (list1))
# print (list1)
# qntt = 0
# for i in set1_list1:
#     for j in list1:
#         if i == j:
#             qntt = qntt + 1
#     print (i, '- გამეორდა', qntt, 'ჯერ')
#     qntt = 0



####### 2) პროგრამამ უნდა წამოიღოს ყველა ქე და ველიუ სათითადო.
####### {'gio':25, 'mari':24, 'ninuca':20, 'ika':26}
# my_dict = {'gio':25, 'mari':24, 'ninuca':20, 'ika':26}
# print (my_dict.keys())
# print (my_dict.values())
# print (my_dict.items()) # ან ზედა ორი, ან ეს 



####### 3) პროგრამამ უნდა წამოიღოს ყველა ქე და ველიუ სათითადო მაგრამ გამოიყენეთ ფორ ლუპი.
####### {'gio':25, 'mari':24, 'ninuca':20, 'ika':26}
# my_dict = {'gio':25, 'mari':24, 'ninuca':20, 'ika':26}
# for i, j in my_dict.items():
#     print (i, j) 
##### იგივე ამოცანა ასეც
# my_dict = {'gio':25, 'mari':24, 'ninuca':20, 'ika':26}
# for i in my_dict:
#     print ('my dict kye ---> ', i)
#     print ('my dict value ---> ', my_dict[i])



####### 4) პროგრამამ უნდა ჩაამატოს ლისტში ქი და ველიუები.
# my_dictionary = {
#     'rail' : 'Rail Way Bill',
#     'sea' : 'Bill of Lading',
#     'truck' : 'CMR',
# }
# my_dictionary ['air'] = 'AWB'
# print (my_dictionary)
# my_dictionary.update ({'AWB': 'Montreal Convention'})
# print (my_dictionary)



#######  5) პროგრამამ უნდა შეავსოს ორი ლისტი 5 რენდომ რიცხვით, პიველი ლისთი უნდა იყოს ქიები და მეორე ლისტი ვალუები უნდა იყოს 
# import random
# my_dictionary = {}
# for i in range (0, 10):
#     rand_val = {random.choice(range (10, 30)) : random.choice(range (100, 120))}
#     my_dictionary.update(rand_val)
# print ('random dictionary', my_dictionary)
# key_list = []
# value_list = []
# for i in range (0, 5):
#     key_list.append(random.choice(list(my_dictionary.keys())))
#     value_list.append(random.choice(list(my_dictionary.values())))
# print ('list with random keys', key_list)
# print ('list with random values', value_list)



###### 6) პროგრამამ უნდა დათვალოს ფაილში სტრინგების და სიმბოლოების რაოდენობა.
# import os 
# f = open('text1.txt', 'r')
# data = f.read()
# strings = data.split()
# string_num = len (strings)
# print('String numbers in "text1.txt": ', string_num)
# f.close()

# f = open('text1.txt', 'r')
# lines = len (f.readlines())
# print ('Line numbers in "text1.txt": ', lines)
# f.close()

# f = open('text1.txt', 'r')
# data = f.read().replace(' ', '')
# char_num = len (data)
# print('Charecter numbers in "text1.txt": ', char_num - lines + 1)
# f.close()



####### 7) შემქენით ფაილი და ყოველი ახალი ჩანაწერის შეცვალეთ კოდით.
# import os 
# my_text = input('Please input text -  ') 
# f = open('text.txt', 'w')  
# f.write(my_text)
# f.close()

