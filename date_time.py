# import datetime as dt
# # tim= dt.datetime.now()
# # print(tim.)

# # tm= dt.datetime(2024,4,5,8,42)
# # print(tm)
# # tm= dt.date

# # string format type
# # tm= dt.datetime.now()
# # print(tm.strftime("%A"))
# # update the bank using a transaction history. the transacttion should caryy the time and date of transection.
# # also there should be a table and the suitable library for that is pretty table
# # from playsound import playsound
# # tm=dt.datetime.now()
# # while True:
# #     if tm.strftime("%I")=="09" and tm.strftime("%M")=="16" and tm.strftime("%S"=="00") and tm.strftime("%p")=="AM":
# #         print("its time to play")
# #         playsound()
    
# # playsound(r"c:\Users\Adeyi Samuel\Music\Manchester City FC - The Boys in Blue.mp3")

# import pygame

# pygame.init()
# pygame.mixer.music.load(r"c:\Users\Adeyi Samuel\Music\Manchester City FC - The Boys in Blue.mp3")
# while True:
#     pygame.init()
#     tm=dt.datetime.now()
#     if tm.strftime("%I")=="09" and tm.strftime("%M")=="27" and tm.strftime("%S"=="00") and tm.strftime("%p")=="AM":
#         print("its time to play")
#         pygame.mixer.music.play()
#         newmin=tm.strftime("%s")
#         if newmin !="20":
#             pygame.mixer.music.stop()
#             pygame.quit

# import math, cmath
# l=[2,4,5,7,3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(5,3))
# print(math.sqrt(93))
# print(math.ceil(6.324525))
# print(math.floor(5.6873))
# print(math.pi)
# print(math.pi*1000+25)

# def add(x,y):
#     return x+y
# z= add(2,3)
# print(z)
# add=lambda x,y:x+y
# print(add(2,3))

sqr= lambda y:[x**2 for x in y]
print(sqr(range(20)))