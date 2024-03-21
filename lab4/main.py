import yaml
import random
import math

random.seed(422)

class AntColony:
    def __init__(self) -> None:
        self.cities = self.read_file()
        
    def read_file(self):
        with open('lab4/tsp.yaml') as file:
            data = yaml.safe_load(file)
        
        return data
    
if __name__ == '__main__':
    ant_colony = AntColony()
    print(ant_colony.cities)