#shooping list app in python by HASAN esemds
#2018/Nov/06 (^-^)

#a list for what we choose
my_list = []

#the main function
def shop():

    #main profile info >>> 
    print("IF YOU NEED HELP TYPE -h FOR MORE INFORMATION")

    #a loop for adding items
    while True:

        #an input to recieve itesms
        item = str(raw_input(">>> "))

        #help command
        if item == "-h":
            app_help()
            continue
        #quit command
        elif item == '-q':
            break
        #show command
        elif item == "-s":
            app_show()
            continue

        #append command
        else:
            app_add(item)

    #for final step
    app_show()
    

#help function
def app_help():
    print"""Hello Planet Earth.
esem code stuio presents.
if you want to see your list type -s
if you want to quit app type -q ."""

#show function
def app_show():
    print("What is in your list?")
    for name in my_list:
        print(name)

#add item function
def app_add(new_item):
     my_list.append(new_item)
     print("{} added. Now You have {} items in your basket.".format(new_item,len(my_list)))


#function calling (^-^)
shop()