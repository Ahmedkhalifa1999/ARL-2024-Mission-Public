from sol import OptimalPath
from helpful import FrozenLakeEnv, make_grader
env = FrozenLakeEnv()
import numpy as np

np.set_printoptions(precision=5)

class MDP(object):
    def __init__(self, P, nS, nA, desc=None):
        self.P = P # state transition and reward probabilities, explained below
        self.nS = nS # number of states 16
        self.nA = nA # number of actions 4
        self.desc = desc # 2D array specifying what each grid cell means (used for plotting)


def create_uniform_mdp_with_rewards(n, m, rewards):
    nS = n * m
    nA = 4  # 4 actions: left, down, right, up
    P = {s: {a: [] for a in range(nA)} for s in range(nS)}
    
    for i in range(n):
        for j in range(m):
            state = i * m + j
            reward = rewards[i, j]  # get the reward for the current state
            for action in range(nA):
                if action == 0:  # left
                    next_state = state if j == 0 else state - 1
                elif action == 1:  # down
                    next_state = state if i == n - 1 else state + m
                elif action == 2:  # right
                    next_state = state if j == m - 1 else state + 1
                elif action == 3:  # up
                    next_state = state if i == 0 else state - m

                probability = 1.0 / nA  # equal probability for each action
                P[state][action].append((probability, next_state, reward))

    desc = np.arange(nS).reshape(n, m)
    return MDP(P, nS, nA, desc)

n, m = 4, 4
rewards = np.array([
    [0, 0, 0, 0],
    [0, -100, 0, -100],
    [0, 0, 0, 100],
    [0, -100, 0, 0]
])
mdp = create_uniform_mdp_with_rewards(n, m, rewards)

expected_output = """Iteration | max|V-Vprev| | # chg actions | V[0]
----------+--------------+---------------+---------
   0      | 25.00000      |  N/A          | 0.00000
   1      | 6.25000      |    3          | 0.00000
   2      | 1.56250      |    2          | 0.00000
   3      | 0.39062      |    3          | 0.00000
   4      | 0.09766      |    3          | 0.00000
   5      | 0.02441      |    1          | 0.02441
   6      | 0.00610      |    0          | 0.02441
   7      | 0.00153      |    0          | 0.02594
   8      | 0.00038      |    0          | 0.02594
   9      | 0.00010      |    0          | 0.02604
  10      | 0.00002      |    0          | 0.02604
  11      | 0.00001      |    0          | 0.02604
  12      | 0.00000      |    0          | 0.02604
  13      | 0.00000      |    0          | 0.02604
  14      | 0.00000      |    0          | 0.02604
  15      | 0.00000      |    0          | 0.02604
  16      | 0.00000      |    0          | 0.02604
  17      | 0.00000      |    0          | 0.02604
  18      | 0.00000      |    0          | 0.02604
  19      | 0.00000      |    0          | 0.02604"""

Vs_VI, pis_VI = OptimalPath(mdp, nIt = 20, grade_print=make_grader(expected_output))

# left: 0, down: 1, right: 2, up: 3
print(np.array(pis_VI[-1]).reshape(4, 4))

# value function for each state (it doesn't depend on the action taken)
print(Vs_VI[-1].reshape(4, 4))