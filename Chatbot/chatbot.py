#Data set used: https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot
import webbrowser
myvars = {}
with open("text_file_name.txt") as myfile:
    for line in myfile:
        name, var = line.partition("\t")[::2]
        myvars[name.strip()] = var.strip()
while(True):
    value=input("YOU: ")
    print("BOT: "+myvars[value])
    if value=="bye":
      break
