from classes.pet import PetPost


def makeUnavailable(posts:dict, postId:int):
    petPost:PetPost = posts.get(postId)
    if petPost and petPost.getavailable() == True:
         petPost.setAvailable(False)
    else:
        raise ValueError