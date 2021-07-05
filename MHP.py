"""
    Code to simulate the Monty Hall Problem (MHP) (https://en.wikipedia.org/wiki/Monty_Hall_problem) and verify winning probabilities
    Creator: Aditya Basu

    Run the code with: python3 MHP.py <NUMBER OF SIMULATIONS>
    Recommended NUMBER OF SIMULATIONS: 2500-3000 (although the more the merrier)
    Approximate run-time for 2500-3000 simulations: 1 minute

    We also verify the following facts (using a plot):
    (i) probability of winning if you switch = 2/3
    (ii) probability of winning if you stick = 1/3

    Mathematical insight:
    Assume (#winning ratio after switching) as a Bernoulli random variable with p = 2/3
    or,(#winning ratio after sticking) as a Bernoulli random variable with p = 1/3
    The results we get are in accordance with the Law of Large Numbers 
    i.e with very high number of simulations, the winning ratio does converge to its expected value
"""

from numpy import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys

def DidYouWin(prizeIn: int, yourChoice: int, switch: bool):
    """
        Returns: 1 if you win the game
        Returns: 0 if you lose the game
    """
    # list of all doors
    ALL = list(range(1, 4))
    # canShow contains the doors which can be shown
    canShow = [num for num in ALL if (num != prizeIn) and (num != yourChoice)]
    show = random.choice(canShow)  # Door which is shown
    # If you switch (choose the other door)
    if switch:
        newChoice = [num for num in ALL if (num != show) and (num != yourChoice)][0]
        return int(newChoice == prizeIn)
    # If you stick (remain with the same door)
    else:
        return int(yourChoice == prizeIn)

def simulate_switch(num_sims: int):
    """
        Runs the simulation <num_sims> times where we always switch
        Returns: the ratio of simulations where we won after switching
    """
    # Running the simulation and counting the number of wins after switching 
    won: int = 0
    for i in range(num_sims):
        # The door which contains the prize
        prizeIn: int = random.randint(1, 4)
        # You choose a door
        yourChoice: int = random.randint(1, 4)
        won += DidYouWin(prizeIn, yourChoice, True)
    win_ratio = won/num_sims
    return win_ratio

def simulate_stick(num_sims: int):
    """
        Runs the simulation <num_sims> times where we always stick
        Returns: the ratio of simulations where we won after sticking
    """
    # Running the simulation and counting the number of wins after sticking
    won: int = 0
    for i in range(num_sims):
        # The door which contains the prize
        prizeIn: int = random.randint(1, 4)
        # You choose a door
        yourChoice: int = random.randint(1, 4)
        won += DidYouWin(prizeIn, yourChoice, False)
    win_ratio = won/num_sims
    return win_ratio

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Run with python3 MHP.py <NUMBER OF SIMULATIONS>"

    num_sims = int(sys.argv[1])
    switch = dict()
    stick = dict()
    # Simulating 
    for i in tqdm(range(1, num_sims+1)):
        switch[i] = simulate_switch(i)
        stick[i] = simulate_stick(i)
    # Plotting
    keys = list(range(1, num_sims+1))
    switchlist = list(switch.values())
    sticklist = list(stick.values())

    plt.figure(figsize=(20, 6))
    plt.plot(keys, switchlist, label = "After switching")
    plt.plot(keys, sticklist, label = "After sticking")
    plt.axhline(y = 1/3, color = 'k', linestyle = '-')
    plt.axhline(y = 2/3, color = 'k', linestyle = '-')
    plt.ylabel("Winning probability",fontweight = 'bold', fontsize = 14, fontname = 'Arial')
    plt.xlabel("Number of simulations",fontweight = 'bold', fontsize = 14, fontname = 'Arial')
    plt.suptitle("Monty Hall Problem - Winning Probability Convergence", fontweight = 'bold', fontsize = 20, fontname = 'Arial')
    plt.legend(loc = 'upper right')
    plt.show()
