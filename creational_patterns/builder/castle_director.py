from house_builder import HouseBuilder

class CastleDirector:

    @staticmethod  
    def construct():  
        "Constructs and returns the final product"  
        return HouseBuilder()\
               .set_building_type("Castle")\
               .set_wall_material("Sandstone")\
               .set_number_doors(100)\
               .set_number_windows(200)\
               .get_result()