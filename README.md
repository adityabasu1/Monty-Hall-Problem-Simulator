# Monty-Hall-Problem-Simulator


Python code to simulate the Monty Hall Problem (MHP) and verify winning probabilities<br />
   
Run the code with: python3 MHP.py <NUMBER OF SIMULATIONS><br />
Recommended NUMBER OF SIMULATIONS: 2500-3000 (although the more the merrier)<br />
Approximate run-time for 2500-3000 simulations: 1 minute<br />

We also verify the following facts (using a plot):
   
(i) probability of winning if you switch = 2/3<br />
(ii) probability of winning if you stick = 1/3<br />
We also verify the following facts using a generated plot.

Mathematical insight:<br />
Assume (#winning ratio after switching) as a Bernoulli random variable with p = 2/3<br />
or,(#winning ratio after sticking) as a Bernoulli random variable with p = 1/3<br />
The results we get are in accordance with the Law of Large Numbers<br />
i.e with very high number of simulations, the winning ratio does converge to its expected value
   
Useful links: <br />
About the problem: https://en.wikipedia.org/wiki/Monty_Hall_problem <br />
MIT Maths for CS: https://www.youtube.com/watch?v=SmFwFdESMHI
   
