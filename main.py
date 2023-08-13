import colorama
from recommendation import about as ab
from recommendation import entertaiment as en
from colorama import Fore,Back,Style
colorama.init(autoreset=True) 
import matplotlib.pyplot as pyplot
import threading
import matplotlib.pyplot as plt
lables = 'Restaurants','Coffee','Entertainment'
sizes = [5,20,10]
plt.rcParams.update({'font.family':'cursive'})
fig,ax = plt.subplots()
ax.pie(sizes,labels=lables, autopct='%1.0f%%',colors=["red", "maroon","darkgray"])
ax.set_title('if You Feel Confused what to choose, this is A hint For You!',size=15)
plt.show(block=False)
print(Fore.RED + Back.WHITE+ Style.BRIGHT +"✦Hello to The Quick SFU !..I'm here to suggest for you The Best Places in Riyadh✦")
#from progtest import Restorent as re
re1 = ab ("Entrecote" '\n', 4.7 , 199 - 575  , "STRIPLOIN FILET" '\n'  , "instagram : @entrecote.sa" '\n' , "https://maps.app.goo.gl/dpRzN7uDqUsJXZ8D6?g_st=iw")
re2 = ab ("nac" '\n' , 3.8 , 42 - 120, "mushroom risotto" '\n' , "instagram : @nacriyadh" '\n' , "https://maps.app.goo.gl/wMn1isT2kMBc1Esy7?g_st=iw")
re3 = ab ("oulu" '\n' , 4.1 , 35 - 96 , "Curly Truffle" '\n' , "instagram : @oulu.sa" '\n' , "https://maps.app.goo.gl/sFcHanp9aTh3dWN17?g_st=iw")
co1 = ab ("groon" '\n' , 4.3 ,18 - 26 , "Ice tea" '\n' , "instagram : @groon.sa" '\n' , "https://maps.app.goo.gl/hUbV2ns34tZ4KdLp7?g_st=iw")
co2 = ab ("clay" '\n' , 4.3 , 22 - 62 , "Ice v60 mix berry" '\n', "instagram : @claycafesa" '\n' , "https://maps.app.goo.gl/RoF1TzavR4EjMNYo9?g_st=iw")
co3 = ab ("volume" '\n' , 4.4 , 11 - 28 , "LATIE" '\n' , "instagram : @volumecoffee_sa" '\n' , "https://maps.app.goo.gl/VPLgGgT4KbT2VuWV9?g_st=iw")
en1 = en ("404 not found" '\n' , 4.5 , "instagram: @wefound404")
en2 = en ("alsaqeefa" '\n' , 4.1 , '\n' "instagram : @alsaqeefa")
en3 = en ("4padl" '\n', 4.7 , '\n' "instagram : @4padel.sa")


#user_input = ' '
while True:
    dic={'Restaurants':['entrecote','nac' , 'oulu'],"Coffee":['groon','clay','volume'],"Entertainment":['404 not found','alsaqeefa','4padel']}
    def_1={'Entrecote':'This classic Parisian-style restaurant serves a sumptuous steak frites set menu enhanced by a secret sauce','nac':'NAC is a lovely restaurant that is specialises in serving international cuisine','oulu': 'A One of the best Italian cuisines in riyadh',
                  'groon':'coffee place & bakery in Riyadh and they have the best ice tea','clay': 'coffee place,Great for working and meeting friends','volume':'Volume coffee Roaster from Riyadh!one of the best coffee places in Riyadh',
                  '404 not found':' 404 Riyadh is already calling itself the*it hangout spot in Riyadh*. The entertainment hub promises music, classic arcade games, bowling, billiards and board games. Game on. Foodies can also refuel on two different menus.'
                  ,'alsaqeefa':'The place’s concept is so fun with so many different games to pick from and enjoy it with your freinds&family.they also serve a coffee!',
                  '4padel':'Padel tennis in Riyadh is pretty straight forward in terms of game rules and court design. 4padel has taken it up a notch by expanding a bit beyond the usual.'}
   #r1 = re ("entrecote",5,"saudi cool","https://maps.app.goo.gl/ghdQvCcysEnpAErP9g_st=ic")
    #r2 = re("for",5,"mom","mo")
    #list=[r1,r2]
    #try:
    user_input = input(
        'Pick one: 1) Restaurant | 2) Coffee | 3) Entertainment [1/2/3]? ')
    #except ValueError:
       #print("Please Enter number 1 or 2 or 3")

    if user_input == '1':
        print(Fore.BLACK+Style.BRIGHT+Back.LIGHTBLUE_EX+"You picked Restaurant",dic['Restaurants'])
        res_input = input('Now choose from these Restaurants: ')

        if res_input == 'entrecote':
          print(Style.BRIGHT+def_1['Entrecote'])
          print(re1.details())
          #print(r1.information())
          review= ["★★★  nice dining with family with good menu of stakes service nice and quality of steaks good bit expensive" 
                    ,"★★★★  the restaurant is Authentic and have a very nice view. the steak is amazing, french fries are perfect","★★★★★   this restaurant is one of the best in Riyadh. it has different style food and a fantastic 360 Degs. view of Riyadh. the atmosphere, location and service is great."]
          mystring = "\n".join(map(str,review))
          review_in= input('Do you want see the reviews? Pick 1 for Yes & 2 for No: ')
          if review_in == '1':
             print(Fore.RED+"******"*20)
             print(Style.BRIGHT+Fore.LIGHTRED_EX+mystring)
             print(Fore.RED+"******"*20)
          elif review_in == '2':
             append_inp = input('Do you want append Your review? Pick 1 for yes & 2 for No: ')
             if append_inp == '1':
                your_review = input ('write your review:')
                review.append(your_review)
                print (Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
          #continue
             
               
        elif res_input == 'nac':
           print(def_1['nac']) 
           print(re2.details())
           review_2 = ["★ ★ ★  Amazing service and lovely place to have drinks outside! The staff there is so friendly and helpful! I will definitely go back!!!","★ ★ ★ ★   Food, service, decor, loved it!","★ ★ ★  What a lovely place!Nac restaurant is definitely one of my favourite place"]
           mystring2 = "\n".join(map(str,review_2))
           review_in2 = input('Do you want see the reviews ? Pick 1 for Yes & 2 for No: ')
           if review_in2 == '1':
              print(Fore.RED+"******"*20)
              print(mystring2)
              print(Fore.RED+"******"*20)
           elif review_in2 == '2':
              append_inp2 = input ('Do you want append your review ? Pick 1 for Yes & 2 for No: ')
              if append_inp2 == '1':
                 your_review2 = input ('write your review: ')
                 review_2.append(your_review2)
                 print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
           #continue
        elif res_input == 'oulu':
           print(def_1['oulu'])
           print(re3.details())
           review_3 = ["★★  The food is very delicious and there are many choices.Service is excellent.Highly recommended.","★★★  Food is so yummy and they have a lot of choices. It is ma favorite","★★★★  A quiet and cozy place, Nice open area"]
           mystring3 = "\n".join(map(str,review_3))
           review_in3 = input ('Do you want see the reviews ? Pick 1 for Yes & 2 for No:  ')
           if review_in3 == '1':
              print(Fore.RED+"******"*20)
              print(mystring3)
              print(Fore.RED+"******"*20)
           elif review_in3 == '2':
              append_inp3 = input ('Do you want append your review ? Pick 1 for Yes & 2 for No: ')
              if append_inp3 == '1' :
                 your_review3 = input ('write your review: ')
                 review_3.append(your_review3)
                 print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
           #continue
    




    elif user_input == '2':
      print(Fore.WHITE+Style.BRIGHT+Back.GREEN+'You picked Coffee',dic['Coffee'])
      coffe_inp = input ('Now choose from these coffe :')
      if coffe_inp == 'groon':
         print(def_1['groon'])
         print(co1.details())
         review_4 = ["★★★  it was very nice The place is calm, I tried ice v60 ethiopian coffee it was very tast",'★★  They have a variety of options for drinks. A wonderful place to gather with friends.',"★★★★★ They have the Best ice tea in Riyadh"]
         mystring4 = "\n".join(map(str,review_4))
         review_in4 = input ('Do you want see the reviews? Pick 1 for Yes & 2 for No: ')
         if review_in4 == '1':
            print(Fore.RED+"******"*20)
            print(mystring4)
            print(Fore.RED+"******"*20)
         elif review_in4 == '2':
            append_inp4 = input (' Do you want append your review ? Pick 1 for Yes & 2 for No: ')
            if append_inp4 == '1':
               your_review4 = input(' write your review: ')
               review_4.append(your_review4)
               print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
         #continue
      elif coffe_inp == 'clay':
         print(def_1['clay'])
         print(co2.details())
         review_5 = ["★★★  A nice place. Good for work. Serve wonderful coffee and have a good selection of pastries. Their taste in music is great ","★★  We had a great experience to celebrate our friends birthday in clay coffee boutique","★★★★  their desserts were all delicious especially the san sebastian and the lemon blueberry cake"]
         mystrin5 = "\n".join(map(str,review_5))
         review_in5 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
         if review_in5 == '1':
            print(Fore.RED+"******"*20)
            print(mystrin5)
            print(Fore.RED+"******"*20)
         elif review_in5 == '2':
            append_inp5 = input ('Do you want append your review? Pick 1 for yes & 2 for No: ')
            if append_inp5 == '1':
               your_review5 = input (' write your revirew: ')
               review_5.append(your_review5)
               print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
         #continue
               
      elif coffe_inp == 'volume':
         print(def_1['volume'])
         print(co3.details())
         review_6 = ["★★★  The place is wonderful and coffee is amazing ","★★  Volume is good coffe is nice","★★★★  Best coffee roaster in riyadh"]
         mystring6 = "\n".join(map(str,review_6))
         review_in6 = input ('Do you want to see the reviews ? Pick 1 for Yes & 2 for No: ')
         if review_in6 == '1':
            print(Fore.RED+"******"*20)
            print(mystring6)
            print(Fore.RED+"******"*20)
         elif review_in6 == '2':
            append_inp6 = input ('Do you want append your review ? Pick 1 for yes & 2 for No: ')
            if append_inp6 == '1':
               your_review6 = input ('write your review: ')
               review_6.append(your_review6)
               print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
         #continue
      #break
    elif user_input == '3':
     print(Fore.GREEN+Style.BRIGHT+Back.BLACK+'You picked Entertainment',dic['Entertainment'])
     inter_inp = input ('Now choose from Entertainment:')
     if inter_inp == '404 not found':
        print(def_1['404 not found'])
        print(en1.details_2())
        review_7 = ["★★★★★  What an AMAZING & awesome place!","★★  Fun place to hangout and play board games, they have 2 bowling lanes but you need to be early because the place gets crowded fast","★★★  Really amazing place for hanging out with friends . Have multiple games"]
        mystring7 = "\n".join(map(str,review_7))
        review_in7 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
        if review_in7 == '1':
           print(Fore.RED+"******"*20)
           print(mystring7)
           print(Fore.RED+"******"*20)
        elif review_in7 == '2':
           append_inp7 = input ('Do you want append your review? Pick 1 for yes & 2 for No: ')
           if append_inp7 == '1':
              your_review7 = input ('write your review: ')
              review_7.append(your_review7)
              print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
        #continue
     elif inter_inp == 'alsaqeefa':
           print(def_1['alsaqeefa'])
           print(en2.details_2())
           review_8 = ["★★★  One of the greatest experiences that I had in Riyadh, the place is so much fun","★★★★★  I really recommend this place!!!","★★  he idea is amazing and we had so much fun! We will definitely come back again and repeat it as much as we can. Recommending it for everyone"]
           mystring8 = "\n".join(map(str,review_8))
           review_in8 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No')
           if review_in8 == '1':
              print(Fore.RED+"*****"*20)
              print(mystring8)
              print(Fore.RED+"******"*20)
           elif review_in8 == '2':
              append_inp8 = input ('Do you want append your review? Pick 1 for Yes & 2 for No: ')
              if append_inp8 == '1':
                 your_review8 = input('write your review: ')
                 review_8.append(your_review8)
                 print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
           #continue
     elif inter_inp == '4padel':
        print(def_1['4padel'])
        print(en3.details_2())
        review_9 = ["★★★  All balls and rackets available, comfy seating area and a cafe to refresh after the game","★★  Amazing place indoor with coffee shop too","★★★★★  Friendly staff and one of the best indoor courts"]
        mystring9="\n".join(map(str,review_9))
        review_in9 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
        if review_in9 == '1':
           print(Fore.RED+"******"*20)
           print(mystring9)
           print(Fore.RED+"******"*20)
        elif review_in9 == '2':
           append_inp9 = input ('Do you want append your review? Pick 1 for Yes & for No: ')
           if append_inp9 == '1':
              your_review9 = input('write your review: ')
              review_9.append(your_review9)
              print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"Your review has been added successfully! Thank you!")
        #continue

    #break
    #else:
     #print('Type a number 1-3')
plt.show()

#print(Fore.RED + Back.WHITE+ Style.BRIGHT +"Hello to program plans")
#from progtest import Restorent as re


#user_input = ' '
'''while True:
    dic={'Restaurants':['entrecote','nac' , 'oulu'],"Coffee":['groon','clay','volume'],"Entertainment":['404 not found','alsaqeefa','4padel']}
    def_1={'Entrecote':'This classic Parisian-style restaurant serves a sumptuous steak frites set menu enhanced by a secret sauce','nac':'NAC is a lovely restaurant that is specialises in serving international cuisine','oulu': 'A One of the best Italian cuisines in riyadh',
                  'groon':'coffee place & bakery in Riyadh and they have the best ice tea','clay': 'coffee place','volume':'Volume coffee Roaster from Riyadh!one of the best coffee places in Riyadh',
                  '404 not found':' 404 Riyadh is already calling itself the*it hangout spot in Riyadh*. The entertainment hub promises music, classic arcade games, bowling, billiards and board games. Game on. Foodies can also refuel on two different menus.'
                  ,'alsaqeefa':'The place’s concept is so fun with so many different games to pick from and enjoy it with your freinds&family.they also serve a coffee!',
                  '4padel':'Padel tennis in Riyadh is pretty straight forward in terms of game rules and court design. 4padel has taken it up a notch by expanding a bit beyond the usual.'}
    #r1 = re ("entrecote",5,"saudi cool","https://maps.app.goo.gl/ghdQvCcysEnpAErP9g_st=ic")
    #r2 = re("for",5,"mom","mo")
    #list=[r1,r2]
    
    user_input = input(
        'Pick one: 1) Restaurant | 2) Coffee | 3) Entertainment [1/2/3]? ')

    if user_input == '1':
        print('You picked Restaurant',dic['Restaurants'])
        res_input = input('Now choose from these Restaurants: ')

        if res_input == 'entrecote':
          print(def_1['Entrecote'])
          #print(r1.information())
          review= ["nice dining with family with good menu of stakes service nice and quality of steaks good bit expensive" 
                    ,"the restaurant is Authentic and have a very nice view. the steak is amazing, french fries are perfect","this restaurant is one of the best in Riyadh. it has different style food and a fantastic 360 Degs. view of Riyadh. the atmosphere, location and service is great."]
          mystring = "\n".join(map(str,review))
          review_in= input('Do you want see the reviews? Pick 1 for Yes & 2 for No: ')
          if review_in == '1':
             print("******"*20)
             print(mystring)
             print("******"*20)
          elif review_in == '2':
             append_inp = input('Do you want append Your review? Pick 1 for yes & 2 for No: ')
             if append_inp == '1':
                your_review = input ('write your review:')
                review.append(your_review)
                print ("your review submit!")
          continue
             
               
        elif res_input == 'nac':
           print(def_1['nac']) 
           review_2 = ["nice dining with family","the restaurant have a very nice view","one of the best restaurants"]
           mystring2 = "\n".join(map(str,review_2))
           review_in2 = input('Do you want see the reviews ? Pick 1 for Yes & 2 for No: ')
           if review_in2 == '1':
              print("******"*20)
              print(mystring2)
              print("******"*20)
           elif review_in2 == '2':
              append_inp2 = input ('Do you want append your review ? Pick 1 for Yes & 2 for No: ')
              if append_inp2 == '1':
                 your_review2 = input ('write your review: ')
                 review_2.append(your_review2)
                 print(f'updated list{review_2}')
           continue
        elif res_input == 'oulu':
           print(def_1['oulu'])
           review_3 = ["nice","good","not bad"]
           mystring3 = "\n".join(map(str,review_3))
           review_in3 = input ('Do you want see the reviews ? Pick 1 for Yes & 2 for No:  ')
           if review_in3 == '1':
              print("******"*20)
              print(mystring3)
              print("******"*20)
           elif review_in3 == '2':
              append_inp3 = input ('Do you want append your review ? Pick 1 for Yes & 2 for No: ')
              if append_inp3 == '1' :
                 your_review3 = input ('write your review: ')
                 review_3.append(your_review3)
                 print(f'updated list{review_3}')
           continue
    




    elif user_input == '2':
      print('You picked Coffee',dic['Coffee'])
      coffe_inp = input ('Now choose from these coffe :')
      if coffe_inp == 'groon':
         print(def_1['groon'])
         review_4 = ["good",'Best ice tea ever',"it's good"]
         mystring4 = "\n".join(map(str,review_4))
         review_in4 = input ('Do you want see the reviews? Pick 1 for Yes & 2 for No: ')
         if review_in4 == '1':
            print("******"*20)
            print(mystring4)
            print("******"*20)
         elif review_in4 == '2':
            append_inp4 = input (' Do you want append your review ? Pick 1 for Yes & 2 for No: ')
            if append_inp4 == '1':
               your_review4 = input(' write your review: ')
               review_4.append(your_review4)
               print(f'updated list : {review_4}')
         continue
      elif coffe_inp == 'clay':
         print(def_1['clay'])
         review_5 = ["good","a good cafe with your family","so great"]
         mystrin5 = "\n".join(map(str,review_5))
         review_in5 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
         if review_in5 == '1':
            print("******"*20)
            print(mystrin5)
            print("******"*20)
         elif review_in5 == '2':
            append_inp5 = input ('Do you want append your review? Pick 1 for yes & 2 for No: ')
            if append_inp5 == '1':
               your_review5 = input (' write your revirew: ')
               review_5.append(your_review5)
               print(f'updated list : {review_5}')
         continue
               
      elif coffe_inp == 'volume':
         print(def_1['volume'])
         review_6 = ["g","oo","d"]
         mystring6 = "\n".join(map(str,review_6))
         review_in6 = input ('Do you want to see the reviews ? Pick 1 for Yes & 2 for No: ')
         if review_in6 == '1':
            print("******"*20)
            print(mystring6)
            print("******"*20)
         elif review_in6 == '2':
            append_inp6 = input ('Do you want append your review ? Pick 1 for yes & 2 for No: ')
            if append_inp6 == '1':
               your_review6 = input ('write your review: ')
               review_6.append(your_review6)
               print(f'updated list: {review_6}')
         continue
      #break
    elif user_input == '3':
     print('You picked Entertainment',dic['Entertainment'])
     inter_inp = input ('Now choose from Entertainment:')
     if inter_inp == '404 not found':
        print(def_1['404 not found'])
        review_7 = ["r","f","w"]
        mystring7 = "\n".join(map(str,review_7))
        review_in7 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
        if review_in7 == '1':
           print("******"*20)
           print(mystring7)
           print("******"*20)
        elif review_in7 == '2':
           append_inp7 = input ('Do you want append your review? Pick 1 for yes & 2 for No: ')
           if append_inp7 == '1':
              your_review7 = input ('write your review: ')
              review_7.append(your_review7)
              print(f'updated list:{review_7}')
        continue
     elif inter_inp == 'alsaqeefa':
           print(def_1['alsaqeefa'])
           review_8 = ["e","f","d"]
           mystring8 = "\n".join(map(str,review_8))
           review_in8 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No')
           if review_in8 == '1':
              print("*****"*20)
              print(mystring8)
              print("******"*20)
           elif review_in8 == '2':
              append_inp8 = input ('Do you want append your review? Pick 1 for Yes & 2 for No: ')
              if append_inp8 == '1':
                 your_review8 = input('write your review: ')
                 review_8.append(your_review8)
                 print("Your review appended succesf!")
           continue
     elif inter_inp == '4padel':
        print(def_1['4padel'])
        review_9 = ["d","f","d"]
        mystring9="\n".join(map(str,review_9))
        review_in9 = input ('Do you want to see the reviews? Pick 1 for Yes & 2 for No: ')
        if review_in9 == '1':
           print("******"*20)
           print(mystring9)
           print("******"*20)
        elif review_in9 == '2':
           append_inp9 = input ('Do you want append your review? Pick 1 for Yes & for No: ')
           if append_inp9 == '1':
              your_review9 = input('write your review: ')
              review_9.append(your_review9)
              print("sus!!")
        continue

    #break
    else:
     print('Type a number 1-3')'''
#continue
# print("see you next time!") #+ take from user a new plasr he recommending before he live , sould i save it ? 