import numpy as np
from step import step

def OptimalPath(mdp, nIt, grade_print=print):
    """
    Inputs:
        mdp: MDP
            The MDP class is a representation of a Markov Decision Process (MDP). Here’s a breakdown of its components:
            P: A dictionary representing the state transition and reward probabilities. It is structured as a nested dictionary:
                - The first key is the state (an integer).
                - The second key is the action (an integer).
                - The value is a list of tuples, each representing a possible outcome of taking that action in that state:
                    - Probability: The probability of this transition.
                    - Nextstate: The resulting state after taking the action.
                    - Reward: The reward received after taking the action.
            nS: The number of states in the MDP. For the Frozen Lake environment, this is 16.
            nA: The number of actions available in each state. For the Frozen Lake environment, this is 4 (representing West, South, East, North).
    Outputs:
        (value_functions, policies)

    len(value_functions) == nIt+1 and len(policies) == nIt
    """

    grade_print("Iteration | max|V-Vprev| | # chg actions | V[0]")
    grade_print("----------+--------------+---------------+---------")
    Vs = [np.zeros(mdp.nS)]
    pis = []
    for it in range(nIt):
        oldpi = pis[-1] if len(pis) > 0 else None
        Vprev = Vs[-1]

        pi = np.zeros(mdp.nS, dtype=int)
        V = np.copy(Vprev)

        V, pi = step(mdp, V, pi, Vprev)

        max_diff = np.abs(V - Vprev).max()
        nChgActions = "N/A" if oldpi is None else (pi != oldpi).sum()
        grade_print("%4i      | %6.5f      | %4s          | %5.5f" % (it, max_diff, nChgActions, V[0]))
        Vs.append(V)
        pis.append(pi)

    return Vs, pis