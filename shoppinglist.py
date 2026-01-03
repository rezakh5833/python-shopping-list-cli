import json
import pandas as pd



def load_list():                             #تابع لود لیست برای ورود داده از فایل shopping_list
   try:
      with open("shopping_list.json" , "r" ) as f:
         return json.load(f)
   except FileNotFoundError:
      return []

def save_list(shopping_list):                #تابع ذخیره لیست در فایل برای استفاده مجدد از روی سیستم
   with open("shopping_list.json" , "w") as f:
      json.dump(shopping_list , f)

shopping_list = load_list()


def add_item(shopping_list):                  #تابع اضاف کردن ایتم به لیست
    while True:
        item = input ("enter item: ").strip().lower()

        if item == "back":
           break
        if item in shopping_list:
           print("item alredy exist:" , item)
        else:
           shopping_list.append(item)
           save_list(shopping_list)
           print("added:" , item)

def show_list_by_index(shopping_list):         #تابع نمایش لیست
      print("shopping list:" , shopping_list)
      if not shopping_list:
         print("shopping list is empty")
      else:
         for i ,item in enumerate(shopping_list , start=1):
          print(f"{i} . {item}")

def remove_item_by_index(shopping_list):     #تابع حذف ایتم از روی اعداد لیست
    if not shopping_list:
           print("shopping_list is empty")
    else :
            for i ,item in enumerate(shopping_list, start=1):
               print(f"{i}. {item}")
               
            index = input("enter number to remove: ").strip() 
            if index.isdigit():
               idx = int(index) - 1
               
               if 0 <= idx <len(shopping_list):
                  remove_item = shopping_list.pop(idx) 
                  save_list(shopping_list)
                  print("item removed:" , remove_item)

               else:
                  print("number out of range")
               
            else:
                  print("enter number")           
while True:
    print("\n1. add item")
    print("2. show list ")
    print("3. remove")
    print("4. exit")


    choice = input ("choose: ").strip()

    if choice == "1":
      add_item(shopping_list)
    
    elif choice == "2":
       show_list_by_index(shopping_list)
       

    elif choice == "3":
       remove_item_by_index(shopping_list)
       save_list(shopping_list)
    elif choice == "4":
       print("bye")
       break
   
    else:
       print("invalid choice") 
        
