from franchise import Franchise
from helper import Helper
class Simulation:

    def run_simulation(self) -> None:
        first_franchise = Franchise(1)
        second_franchise = Franchise(2)
        third_franchise = Franchise(3)

        first_franchise.place_order()
        first_franchise.place_order()
        second_franchise.place_order()
        third_franchise.place_order()
        second_franchise.place_order()
        third_franchise.place_order()
