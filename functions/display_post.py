from classes.pet import PetPost


def displayPosts(posts:dict):
    for postId, petPost in posts.items():
        petPost:PetPost = posts.get(postId)
        print(f'-----(ID:{postId})-----')
        print(f"{petPost.getPetName()} looking for a new home!\n type: {petPost.getPetType()}, color: {petPost.getColor()}, age: {petPost.getAge()}, location: {petPost.getCity()}\n {'Still availabe for adoption ✓' if petPost.getavailable() else 'Not availabe for adoption X'} ")
