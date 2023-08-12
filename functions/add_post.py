

from classes.pet import PetPost


countPostId = 1
def addPost(posts:dict, petPost:PetPost):
    global countPostId
    petPost.setId(countPostId)
    posts[countPostId] = petPost
    countPostId = countPostId +1

