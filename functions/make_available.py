from classes.pet import PetPost


def makeAvailable(posts:dict, postId:int):
    petPost:PetPost = posts.get(postId)
    if petPost.getavailable() == False:
         petPost.setAvailable(True)
    else:
        print("not found") 