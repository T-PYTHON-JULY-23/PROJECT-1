

from classes.pet import PetPost


def displayRequest(request:dict):
    for postId, petPost in request.items():
        petPost:PetPost = request.get(postId)
        print(f'-----(ID:{postId})-----')
        print(f"Name{petPost.getPetName()} type: {petPost.getPetType()}, color: {petPost.getColor()}, age: {petPost.getAge()}, location: {petPost.getCity()}\n {'Waiting for acceptance' if petPost.getavailable() else 'Accepted'}")
