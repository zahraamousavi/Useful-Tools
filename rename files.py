import os


top_dir = os.listdir("C:/Users/user/Desktop/phonecall/")
base_dir = "C:/Users/user/Desktop/phonecall/"

postfix = 1
for file in top_dir:
    os.rename(base_dir + file, 
              base_dir + "PhoneCall_"+ format(postfix, '04d') +".wav")
    postfix += 1
        