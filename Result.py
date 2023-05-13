
# probability, char_pro, tag_pro, day_pro, time_pro = 0;

print(" \n \n")

chars = int(input("Enter number of characters in your Title (At max 100) : "))

if(chars < 10):
    char_pro = 0
elif(chars <= 20):
    char_pro = (22/872)
elif(chars <= 30):
    char_pro = (84/872)
elif(chars <= 40):
    char_pro = (116/872)
elif(chars <= 50):
    char_pro = (127/872)
elif(chars <= 60):
    char_pro = (106/872)
elif(chars <= 70):
    char_pro = (78/872)
elif(chars <= 80):
    char_pro = (81/872)
elif(chars <= 90):
    char_pro = (110/872)
elif(chars <= 100):
    char_pro = (148/872)

print(" \n ")

tags = int(input("Enter number of tags in your Video(At max 100) : "))

if(tags < 10):
    tag_pro = (37/872)
elif(tags <= 20):
    tag_pro = (86/872)
elif(tags <= 30):
    tag_pro = (74/872)
elif(tags <= 40):
    tag_pro = (112/872)
elif(tags <= 50):
    tag_pro = (131/872)
elif(tags <= 60):
    tag_pro = (147/872)
elif(tags <= 70):
    tag_pro = (177/872)
elif(tags <= 80):
    tag_pro = (80/872)
elif(tags <= 90):
    tag_pro = (18/872)
elif(tags <= 100):
    tag_pro = (1/872)

print(" \n ")

day = input("Enter your day of Uploading Video : ")

if(day == "Sunday" or day == "sunday"):
    day_pro = (74/872)
elif(day == "Monday" or day == "monday"):
    day_pro = (103/872)
elif(day == "Tuesday" or day == "tuesday"):
    day_pro = (154/872)
elif(day == "Wednesday" or day == "wednesday"):
    day_pro = (147/872)
elif(day == "Thursday" or day == "thursday"):
    day_pro = (144/872)
elif(day == "Friday" or day == "friday"):
    day_pro = (148/872)
elif(day == "Saturday" or day == "saturday"):
    day_pro = (102/872)

print(" \n ")

time = int(input("Enter time of uploading video in (24hr HH) format : "))

if(time <= 6):
    time_pro = (235/872)
elif(time <= 12):
    time_pro = (276/872)
elif(time <= 18):
    time_pro = (296/872)
else:
    time_pro = (61/872)

# highest = 21.433

probability = ((char_pro*0.4) + (tag_pro*0.3) + (time_pro*0.2) + (day_pro*0.1)) * 100

p = (probability/21.433) * 100

print(" \n \n Probability Percentile is :  " , '%.3f'%p)


print("\n ")


if(p >= 100):
    print(" \n Your Inputs are Accurate, Video has high chances of becoming a Trending Video ! \n")
else:
    print("You Need to change your Paramters in the Video, for increasing chances of Video going to trending Page, here are some suggestions you can use :  ")
    
    if(char_pro < (148/872)):
        print("\n \t → Keep your Title Character length between 90 to 100 nad using keywords like - The, Year")
    if(tag_pro < (170/872)):
        print("\n \t → Use Tags while uploading your Video to increase virality of content, and try to keep number of tags between 60 to 70.")
    if(day_pro < (154/872)):
        print("\n \t → For increasing chances of Video going to trending Page, upload it on Tuesday.")
    if(time_pro < (296/872)):
        print("\n \t → For increasing chances of Video going to trending Page, upload the video in the Afternoon, between 12Pm to 6PM \n")


