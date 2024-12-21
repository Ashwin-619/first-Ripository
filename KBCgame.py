questions=[['Current Railway Minister of India is______?', 'a. Mamta Banarjee','b.Ram Vilash', 'c.Ashwini Vaishnaw','d.Piyush Goyal'],
   ['Which god is also known as ‘Gauri Nandan’?', 'a. Agni', "b. Indra", "c. Hanumaan","d. Ganesh"],
   ["What does not grow on tree according to a popular Hindi saying?", "a. Money", "b. Flower","c. Fruits","d. Leaves"],
   ["Which city is known as the Pink City of India?", "a. Banglore", "b. Maysore", "c. Jaipur","d. Kochi"],
   ["Who wrote India's National Anthem?", "a. Rabindranath Tagore", "b. Lal bahadur shashtri", "c. RK narayan","d. Chetan bhagat"],
   ["How many major religions are there in India?", "a. 6", "b. 7", "c. 8", "d. 9"],
   ["When is the National Hindi Diwas celebrated?", "a. 13 September", "b. 14 September", "c. 14 July", "d. 15 August"],
]


ans=[3,4,1,3,1,1,2]

print("enter 1 for a")
print("enter 2 for b")
print("enter 3 for c")
print("enter 4 for d")

money=0

for i in range(0,len(questions)):
               
      print("Question:")
      print(questions[i][0])
      print(f"{questions[i][1]}    {questions[i][2]}")
      print(f"{questions[i][3]}    {questions[i][4]}")
      lckAns=int(input("enter your answer"))

      if lckAns!=ans[i]:
         print("Sorry it's a wrong answer!")
         break
      else:
         print("Correct!")
   
      money+=10000000


   
    

if money<30000000:
   print("F")
   money=0

if money>=30000000 and money<70000000:
   print("Well played!")
   money=30000000

if money==70000000:
    print("Congratulation you answered all questions correctly!!!!")  

print(f"Cash won = {money}Rs")

