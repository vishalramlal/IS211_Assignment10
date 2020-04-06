#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Assignment 10 Part 2

import sqlite3 as lite
import sys

sys.path.append("/home/vr12046461/Desktop/IS211/IS211_Assignment10")


con = lite.connect('pets')


with con:  
    cur = con.cursor()
    cur.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(1,'James','Smith',41);")
    cur.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(2, 'Diana', 'Greene', 23);")
    cur.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(3, 'Sara', 'White', 27);")
    cur.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(4, 'William','Gibson', 23);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(1, 'Rusty', 'Dalmation',4,1);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(2, 'Bella', 'Alaskan Malamute',3,0);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(3, 'Max', 'Cocker Spaniel',1,0);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(4, 'Rocky', 'Beagle',7,0);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(5, 'Rufus', 'Cocker Spaniel',1,0);")
    cur.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(6, 'Spot', 'Bloodhound',2,1);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1,1);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1,2);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(2,3);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(2,4);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(3,5);")
    cur.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(4,6);")

con.close()






# In[ ]:




