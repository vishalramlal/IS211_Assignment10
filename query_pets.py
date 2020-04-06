#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Assignment 10 Part 2

import sqlite3 as lite
import sys

sys.path.append("/home/vr12046461/Desktop/IS211/IS211_Assignment10")


con = lite.connect('pets')


with con:

    cur = con.cursor()
    
    def displayP():
        pid = input("Enter the person ID : ")
        if pid == "-1":
            print("Exiting")
            sys.exit()
        else:
            person = cur.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (pid,)).fetchone()
            pet = cur.execute("SELECT  name, breed, age, dead FROM pet INNER JOIN person_pet on person_pet.pet_id = pet.id WHERE person_pet.person_id = ?", (pid,)).fetchone()
            if person == None:
                print("No person with this ID exists.")
            else:
                if pet[3] == "0":
                    print("{} {} owns {}, a {}, {} years old".format(person[0], person[1], pet[0], pet[1], pet[2]))
                    print("Person is {} {}, {} years old".format(person[0], person[1], person[2]))
                else:
                    print("Person is {} {}, {} years old.".format(person[0], person[1], person[2]))
                    print("{} {} owned {}, a {}, and was {} years old".format(person[0], person[1], pet[0], pet[1], pet[2]))
    
    
def main():
    displayP()
    
while True:
    if __name__ == "__main__":
        main()


# In[ ]:




