names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random


student_scores = { student:random.randint(1,100) for student in names}
#print(student_scores)
#Create a dictionary based on data on another dictionary
passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
#print(passed_students)

### Exercise

sentence = "what is the airspeed velocity of an unladen swallow?"

word_list = sentence.split()
#print(word_list)
word_list_count = [len(word) for word in word_list]
#print(word_list_count)

word_list_dict = { word: len(word) for word in word_list}
#print(word_list_dict )

august_payments = {"Cristobal":350, "Sandra":235, "Carlos": 235, "Floria": 213,"Heiner": 340}

august_payments_col = {name:amount * 545 for (name,amount) in august_payments.items()}
august_payments_dict ={"name": ['Cris','Sandra','Carlos','Floria','Heiner'],
                       "amount":[370,245,540,213,0]
                       }
#print(august_payments_col)

#looping through dictionaries
#for(name, amount) in august_payments_col.items():
   # print(name + " ha depositado C: " + str(amount))

import pandas

df = pandas.DataFrame(august_payments_dict)
print(df)


#Loop thru a DF

for(index, row) in df.iterrows():
    #each row is a series, so it is possible to tap into the values

    print(row.name)