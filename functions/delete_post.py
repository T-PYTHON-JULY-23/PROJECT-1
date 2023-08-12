from classes.pet import PetPost


def deletePost(posts:dict, postId:int):
    petPost:PetPost = posts.get(postId)
    if postId in posts:
        del posts[postId]
        print("post deleted")
    else:
        print("post not found") #raise error