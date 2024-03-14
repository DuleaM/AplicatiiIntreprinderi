import pandas as pd
import math


class KnapSack:
    
    def __init__(self, input) -> None:
        dataframe = pd.read_csv(input)
        
        self.df = dataframe.sort_values(by='carat')
        
    def __convert_to_gram(self, carat):
        gram = carat * 5
        return math.floor(gram)

    def get_weights(self) -> list:
        weights = list(
            map(
                self.__convert_to_gram,
                self.df['carat']
            )
        )

        return weights
    
    def get_prices(self) -> list:
        prices = list(self.df['price'])
        
        return prices
    

    def knap_sack(self, max_weight=5):
        max_weight = max_weight * 1000
        weights = self.get_weights()
        prices = self.get_prices()
        
        dp = [0 for _ in range(max_weight + 1)]
        
        for index in range(len(weights)):
            
            for weight in range(max_weight, 0, -1):
                if weights[index] < weight:
                    
                    dp[weight] = max(
                        dp[weight],
                        dp[weight - weights[index]] + prices[index]
                    )

        return dp[-1]

if __name__ == "__main__":
    ks = KnapSack(input='lab2/diamonds.csv')
    print(ks.knap_sack())




