import yaml
import random
import math

random.seed(422)
class SimulatedAnnealing:
    
    def __init__(self) -> None:
        self.cities = self.read_file()
    
    def read_file(self):
        with open('lab3/tsp.yaml') as file:
            data = yaml.safe_load(file)
        
        return data
    
    def get_distance(self, city1, city2):
        return ((city1['X'] - city2['X'])**2 + (city1['Y'] - city2['Y'])**2)**0.5
    
    def get_energy(self, cities):
        energy = 0
        for i in range(0, len(cities) - 1):
            energy += self.get_distance(cities[i], cities[i+1])
        return energy

    def get_neighbor(self, cities):
        neighbour = cities[:]
        
        index1 = random.randint(0, len(neighbour) - 1)
        index2 = random.randint(0, len(neighbour) - 1)
        
        while index1 == index2:
            index2 = random.randint(0, len(neighbour) - 1)
            
        neighbour[index1], neighbour[index2] = neighbour[index2], neighbour[index1]
        
        return neighbour
        

    def simulate_annealing(self):
        temperature = 1000
        cooling_rate = 0.98
        
        cities = self.cities[:]
        
        best_energy = 0
        best_cities = []
        while temperature > 1:
            proposed_neighbour = self.get_neighbor(cities)
            current_energy = self.get_energy(cities)
            neighbour_energy = self.get_energy(proposed_neighbour)
            
            energy_difference = current_energy - neighbour_energy
            
            if energy_difference <= 0 and random.random() > math.exp(energy_difference / temperature):
                best_cities = proposed_neighbour[:]
                best_energy = neighbour_energy
                
                cities = proposed_neighbour
            
            
            temperature *= cooling_rate

        return best_cities, best_energy

    def main(self):
        cities, energy = self.simulate_annealing()
        diesel_price = 1
        consume = 7.5
        total_price = consume * energy / 100
        
        print(total_price)
        

if __name__ == '__main__':
    sa = SimulatedAnnealing()
    sa.main()
    
    