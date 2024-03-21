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
        self.ants = 10
        self.iterations = 100
        self.rho = 0.2
        self.Q = 5
        
    def read_file(self):
        with open('lab4/tsp.yaml') as file:
            data = yaml.safe_load(file)
        
        return data[:11]


    def get_distance(self, city1, city2):
        return ((city1['X'] - city2['X'])**2 + (city1['Y'] - city2['Y'])**2)**0.5

    def get_total_distance(self):
        return sum([self.get_distance(self.cities[i], self.cities[i+1]) for i in range(len(self.cities) - 1)])

    def get_distance_matrix(self, cities):
        distance_matrix = []
        for city1 in cities:
            distance_line = []
            for city2 in cities:
                distance_line.append(self.get_distance(city1, city2))
            
            distance_matrix.append(distance_line)
        
        return distance_matrix
    
    def lower_pheromone(self):
        for i in range(len(self.pheromone_matrix)):
            for j in range(len(self.pheromone_matrix[i])):
                self.pheromone_matrix[i][j] = (1 - self.rho) * self.pheromone_matrix[i][j]

    def update_pheromone(self, visited):
        for index in range(len(visited) - 1):
            city1 = visited[index]
            city2 = visited[index + 1]
            self.pheromone_matrix[city1][city2] += self.Q/self.get_total_distance()
            
    def setup_first_iteration(self):
        num_cities = len(self.cities)
        visited = []
        
        for i in range(self.ants):
            visited = []
            
            while len(visited) != num_cities:
                random_index = random.randint(0, num_cities-1)
                print(random_index)
                if random_index not in visited:
                    visited.append(random_index)
        
        print(visited)
        self.update_pheromone(visited)

    def main(self):
        self.setup_first_iteration()

        print(self.pheromone_matrix)


if __name__ == '__main__':
    ant_colony = AntColony()
    print(ant_colony.main())