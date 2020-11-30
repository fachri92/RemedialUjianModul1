# #1
# def find_short(a):
#     kata = a.split(' ')
#     print(f'The shortest word has {len(min(kata, key=len))} char(s)')

# find_short('as book is aa window')
# find_short('Create new file after this morning')

# 2
# def persistence(a):
#     if a < 0:
#         print( "Please input positive number only!")
#     elif len(str(a))==1:
#         print(0)
#         print(f'{a} is already single digit') 
#     else:
#         counter = 0
#         while len(str(a))!=1:
#             counter+=1
#             total=1
#             for i in str(a):
#                 total=total* int(i)
#             a=total
#         print(counter)

# persistence(1)
# persistence(-2)
# persistence(999)



