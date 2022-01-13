from collections import Counter

import numpy as np
import pandas as pd

if __name__ == '__main__':
    bank = int(input("input gamers bank (money to split among two players): "))
    experiments = int(input("numbers of experiments: "))
    winner = np.random.choice(['player_a', 'player_b'], size=experiments, replace=True)
    df = pd.DataFrame([Counter(winner)])

    print("Player A scored {} points and got {} dollars".format(df['player_a'], round((df['player_a']/experiments)[0]*bank)))
    print("Player B scored {} points and got {} dollars".format(df['player_b'], round((df['player_b']/experiments)[0]*bank)))