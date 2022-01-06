from igloo_director import IglooDirector
from castle_director import CastleDirector
from houseboat_director import HouseBoatDirector

igloo = IglooDirector.construct()
castle = CastleDirector.construct()
house_boat = HouseBoatDirector.construct()

print(igloo)
print(castle)
print(house_boat)