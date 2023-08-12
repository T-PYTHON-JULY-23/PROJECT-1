import time
from classes.credit_card import CreditCard
from classes.pet import PetPost
from functions.add_post import addPost
from functions.delete_post import deletePost
from functions.display_post import displayPosts
from functions.display_request import displayRequest
from functions.make_available import makeAvailable
from functions.make_unavailable import makeUnavailable
cards={} # for payment
posts={} # for post
request={} # when there a request need to accepte
myRequest ={} 
delivery ={}
post1 = PetPost('Mio','cat',1,'black','Riyadh')
post2 = PetPost('meme','dog',2,'broen','Riyadh')
addPost(posts,post1)
addPost(posts,post2)
user=''
while user != 'exit':
    try:
        print('welcome to paws! What do you want to do? \n Enter (1) to view all pets ready for adoption \n Enter (2) to post a pet for adoption \n Enter (3) to adoption request \n Enter (4) to delete post \n Enter (5) to view adoption request \n Enter (6) to view your request \n Enter (7) to accepte request \n Enter (8) to complete the request for adoption \n Enter (9) to view deliveries and pick-ups \n Enter(exit) for exit ')
        user = input('Enter here: ')
        match user:
            case '1':
                displayPosts(posts)
            case '2':
                petName = input('Enter pet name :')
                pettype = input('Enter pet type (cat,dog ..etc) :')
                age = input('Enter pet age: ')
                color = input('Enter pet color: ')
                city =input('Enter your city: ')
                post = PetPost(petName,pettype,int(age),color,city)
                addPost(posts,post)
                print('Post added')
            case '3':
                postId= input('Enter post Id: ')
                postId = int(postId)
                petPost:PetPost = posts.get(postId)
                if isinstance(postId,int):
                    if postId in posts:
                        if petPost.getavailable() == True:
                            print('request has been sent, wait for the owner to accepte, you can check by enter (6)')
                            request[postId] = petPost
                            myRequest[postId] = petPost
                        else:
                            print(f'Sorry {postId} is not availabe for adoption')
                    else:
                        print(f'{postId} does not exist')
                else: raise ValueError
            case '4':
                postId= input('Enter post Id: ')
                petPost:PetPost = posts.get(int(postId))
                if isinstance(int(postId),int):
                    if int(postId) in posts:
                      deletePost(posts,int(postId))  
                    else:
                        print(f'{postId} does not exist')
                else:
                    raise ValueError
            case '5':
                displayRequest(request)
            case '6':
                displayRequest(myRequest)
            case '7':
                postId= input('Enter post Id: ')
                postId = int(postId)
                petPost:PetPost = request.get(postId)
                makeUnavailable(request,postId)
                del request[postId]
                print('Accepted')
            case '8':
                postId1= input('Enter post Id: ')
                postId = int(postId1)
                if isinstance(postId,int):
                    petPost:PetPost = request.get(postId)
                    if postId in posts:
                            print('request has been accepted. \n Enter (r) if you like to receive it yourself, Enter (d) if you want it to delivered to your home (the delivery amount is $8), (c) if you want to cancel')
                            user = input('Enter here: ')
                            if user.lower() == 'r':
                                name = input('Enter your name: ')
                                phonNumber = input('Enter phone number: ')
                                city = input('Enter your city number: ')
                                print('Thank you, the owner will contact you soon')
                                delivery[postId] = {'name':name,'phonNumber':phonNumber,'city':city,'case':'r'}
                            elif user.lower() == 'd':
                                name = input('Enter your name: ')
                                phonNumber = input('Enter phone number: ')
                                city = input('Enter your city number: ')
                                cardHolder =input('Enter the name on card holder: ')
                                cardNumber= input('Enter card number: ')
                                expireDate =input('Enter expireDate: ')
                                cvv=int(input('Enter CVV: '))
                                card1 = CreditCard('khald khalf',6,'378282246310005','02/26',244)
                                card2 = CreditCard('sara ahmad',5000,'378734493671000','03/25',878)
                                cards[card1.get_cardNumber()] = card1
                                cards[card2.get_cardNumber()] = card2
                                if cardNumber in cards:
                                    creditCard:CreditCard = cards.get(cardNumber)
                                    if cardHolder == creditCard.get_cardHolder() and expireDate == creditCard.get_expireDate() and cvv == creditCard.get_cvv():
                                        result= creditCard.withdraw()
                                        print(result)
                                        if result == 'Payment successful':
                                            print('Thank you, the Delivery man will contact you soon')
                                            delivery[postId] = {'name':name,'phonNumber':phonNumber,'city':city,'case':'d'}
                                    else:
                                         print('Verification failed, process has been cancelled')
                                else:
                                     print(f'Verification m failed, process has been cancelled')
                            elif user.lower() == 'c':
                                        print('canceled')
                                        del myRequest[postId]
                                        makeAvailable(posts,postId)
                            else:
                                print('invalid value, process has been cancelled')
                    else:
                        print(f'{postId} does not exist')
                else:
                    raise ValueError
            case '9':
                  for postId, info in delivery.items():
                    print(f'for post Id: {postId}, name: {info["name"]}, phone number: {info["phonNumber"]}, city{info["city"]},  {"pick up" if info["case"]== "r" else "delivery"}')
            case "exit":
                print('thank you for using paws!')
            case _:
                print('invalid value try again')
    except ValueError:
        print('invalid value try again')
    except AttributeError as error:
        print(error)
    except:
         print('something went wrong..')