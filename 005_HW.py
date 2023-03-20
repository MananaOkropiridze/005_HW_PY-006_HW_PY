#######  სავარჯიშო 1: პროგრამამ რევერსული სახით დაბეჭდოს რევერსული სახით
####### tuple1 = (10, 20, 30, 40, 50)
# str1 = []
# tuple1 = (10, 20, 30, 40, 50)
# len_tpl =  (len (tuple1))
# print ('original tuple: ', tuple1)
# for i in range (0, len_tpl):
#     str1.append(tuple1 [len_tpl - i - 1])
# tuple2 = tuple(str1)
# print ('reversed tuple: ', tuple2)


####### სავარჯიშო 2: პროგრამამ დაბეჭდოს ელემენტის მნიშვნელობა ტუპლიდან
# ##### ("Orange", [10, 20, 30], (5, 15, 25))
# ##### OUTPUT: 20 
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print (tuple1[1][1])


####### სავარჯიშო 3: დაალაგეთ ტუპლები წყვილად
## ვერ გავიგე ზუსტად დავალება და გავაკეთე ორნაირად
### ვერსია1. ავიღე 2ცალი ტუპლი და შესაბამისი ინდექსის წევრები დავაწყვულე ახლა ტუპლში -  tupe_pairs
# tuple_a = (1, 2, 3)
# tuple_b = ('a', 'b', 'c')
# zipper = zip (tuple_a, tuple_b)
# tupe_pairs = tuple (zipper)
# print (tupe_pairs)
### ვერსია2. დავაჯოინე, ანუ "დავაწყვილე" 2ცალი ტუპლი 
# tuple_a = (1, 2, 3)
# tuple_b = ('a', 'b', 'c')
# joined_tpls = tuple_a + tuple_b
# print(joined_tpls)
#######  სავარჯიშო 3 ის განმარტებული ვერსია. (('a', 23),('b', 37),('c', 11), ('d',29)) გაქვს ეს ტუპლი მაგალითად, 
#######ამაზე უნდა გააკეთო სორტირება სწორაად დაალაგო წყვილება. კომპილერმა რაც უნდა მოგცეს პასუხი არის ეს :  (('c', 11), ('a', 23), ('d', 29), ('b', 37))
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# list_tuple = list(tuple1)
# list_tuple.sort(key=lambda x:x[1])  # დაასორტირებს [1] ინდექსის მიხედით
# print (list_tuple)
# list_tuple.sort(key=lambda x:x[0]) # დაასორტირებს [0] ინდექსის მიხედით
# print (list_tuple)


####### სავარჯიშო 4 : დაწერეთ პითონის პროგრამა ლისტის ტუპლად გადაქცევის
# list1 = ["Orange", [10, 20, 30], (5, 15, 25)]
# print (type(list1))
# print ('this data is list: ', list1)
# tuple1 = tuple(list1)
# print (type(tuple1))
# print ('this data is tuple: ', tuple1)


# სავარჯიშო 5: ჩაამატეთ მესამე ელემენტის ადგილას ახალი ელემენტი და გადააქციეთ ახალი ლისტი  ტუპლად
# list1 = ["Orange", [10, 20, 30], (5, 15, 25)]
# print ('Original list: ', list1)
# add_memb_list1 = list1.insert(2, 'banana')
# print ('New list: ', list1)
# print ('this data is list: ', type(list1))
# tuple1 = tuple(list1)
# print ('this data is tuple: ', type(tuple1))
# print ('list into tuple: ', tuple1)

 
####### სავარჯიშო 6 : დაწერეთ პითონის პროგრამა სიმეტრიული ტუპლის ამოსაღებად
# list1 = [(1, 2), (5, 8), ('a', 'b'), ('1', '2'), (8, 5), (9, 10), ('2', '1'), (2, 1), (4, 9), ('b', 'a'), (1, 2), (5, 8), ('a', 'b'), ('1', '2'), (8, 5), (9, 10), ('2', '1'), (2, 1), (4, 9), ('b', 'a'), ('2', '1'), (2, 1), (4, 9), ('b', 'a'), (5, 7), (7, 5)]
# print ('Original list: ', list1)
# symetr_list = [] 
# list1 = list(set(list1)) # დუბლიკატების აცილების მიზნით. თავდან მქონდა dictionaryთ: list(dict.fromkeys(list1)). ისევ გავაlist-ე რომ ინდექსირება შემძლებოდა
# len_list1 = (len (list1))
# print ('Symmetric tuples:')
# for i in range (0, len_list1):
#     for j in range (i + 1, len_list1):
#         if list1 [i][0] == list1 [j][1] and list1 [i][1] == list1 [j][0]:
#             symetr_list.append((list1[i], list1[j]))
#             break
# print (symetr_list)


####### სავარჯიშო 7 : დაწერეთ პროგრამა ტუპლების დასალაგებლად მათი მაქსიმალური ელემენტის მიხედვით
# def max_memb(x):
#     return max(x)
# tuple_list = [(30, 15, 7, 4), (1, 5, 9, 2), (1, 5), (1, 4, 9, 2), (1, 0), (1, 1, 0), (1, 1, 1, 0), (1, 0, 0)]
# print('original list: ', tuple_list)
# tuple_list.sort(reverse = True, key=max_memb) # გავაკეთე სორტირება მაქსიმუმის არჩევით
# print('Sorted Tuples : ', tuple_list)

####### სავარჯიშო 7 : დაწერეთ პროგრამა ტუპლების დასალაგებლად მათი მაქსიმალური ელემენტის მიხედვით
# def max_memb(x):
#     return max(x)
# tuple_list = [(30, 15, 7, 4), (1, 5, 9, 2), (1, 5), (1, 4, 9, 2), (1, 0), (1, 1, 0), (1, 1, 1, 0), (1, 0, 0)]
# print('original list: ', tuple_list)
# tuple_list.sort(reverse = True, key=max_memb) # გავაკეთე სორტირება მაქსიმუმის არჩევით
# print('Sorted Tuples : ', tuple_list)
 
