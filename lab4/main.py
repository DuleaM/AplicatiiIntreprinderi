import yaml
import random
import math

random.seed(422)

class AntColony:
    def __init__(self) -> None:
        self.cities = self.read_file()
        self.distance_matrix = self.get_distance_matrix(self.cities)
        self.pheromone_matrix = [[1 for _ in range(len(self.cities))] for _ in range(len(self.cities))]
        
        #vars
        ants = 10
        iterations = 100
        rho = 0.2
        
        
    def read_file(self):
        with open('lab4/tsp.yaml') as file:
            data = yaml.safe_load(file)
        
        return data[:11]


    def get_distance(self, city1, city2):
        return ((city1['X'] - city2['X'])**2 + (city1['Y'] - city2['Y'])**2)**0.5

    def get_distance_matrix(self, cities):
        distance_matrix = []
        for city1 in cities:
            distance_line = []
            for city2 in cities:
                distance_line.append(self.get_distance(city1, city2))
            
            distance_matrix.append(distance_line)
        
        return distance_matrix
    
    def update_pheromone(self):
        for i in range(len(self.pheromone_matrix)):
            for j in range(len(self.pheromone_matrix[i])):
                self.pheromone_matrix[i][j] = (1 - self.rho) * self.pheromone_matrix[i][j]

    
    def main(self):
        pass
    
if __name__ == '__main__':
    ant_colony = AntColony()
    print(ant_colony.cities)