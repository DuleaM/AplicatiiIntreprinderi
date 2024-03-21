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
        self.alfa = 2
        self.beta = 4
        
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
                if random_index not in visited:
                    visited.append(random_index)
        
        self.update_pheromone(visited)


    def get_prob_matrix(self):
        total_prob = 0
        probs = []
        num_cities = len(self.cities)
        for i in range(num_cities):
            prob = []
            for j in range(num_cities):
                if i == j:
                    current_prob = 0
                else:
                    current_prob = self.pheromone_matrix[i][j] ** self.alfa * (1 / self.distance_matrix[i][j]) ** self.beta
                    total_prob += current_prob
                prob.append(current_prob)

            probs.append(prob)
    
        #normalizare
        for i in range(num_cities):
            for j in range(num_cities):
                probs[i][j] = probs[i][j] / total_prob

        return probs
            
    def get_visited(self, starting_city):
        num_cities = len(self.cities)
        visited = [starting_city]
        
        max_value = -1
        value = random.uniform(0, 1)
        while len(visited) != num_cities:
            last_city = visited[-1]
            probs = self.get_prob_matrix()
            for j in range(num_cities):
                if probs[last_city][j] < value and probs[last_city][j] > max_value and probs[last_city][j] not in visited:
                    max_value = probs[last_city][j]
                    best_city = j

            visited.append(best_city)
        
        return visited


    def main(self):
        self.setup_first_iteration()

        for i in range(self.iterations - 1):
            self.lower_pheromone()
            
            starting_city = random.randint(0, len(self.cities) - 1)
            
            for ant in range(self.ants):
                visited = self.get_visited(starting_city)
                
                self.update_pheromone(visited)
        
        for i in range(len(self.pheromone_matrix)):
            print(self.pheromone_matrix[i])

if __name__ == '__main__':
    ant_colony = AntColony()
    print(ant_colony.main())