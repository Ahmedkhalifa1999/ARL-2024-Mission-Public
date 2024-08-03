import numpy as np

def step(mdp, V, pi, Vprev):
    """
    Inputs:
        mdp: MDP
            The MDP class is a representation of a Markov Decision Process (MDP). Here’s a breakdown of its components:
            - P: A dictionary representing the state transition and reward probabilities. It is structured as a nested dictionary:
                - The first key is the state (an integer).
                - The second key is the action (an integer).
                - The value is a list of tuples, each representing a possible outcome of taking that action in that state:
                    - Probability: The probability of this transition.
                    - Nextstate: The resulting state after taking the action.
                    - Reward: The reward received after taking the action.
            - nS: The number of states in the MDP. For the Frozen Lake environment, this is 16.
            - nA: The number of actions available in each state. For the Frozen Lake environment, this is 4 (representing West, South, East, North).
        Vprev: Previous value function (the expected future reward function based on the previous policy). numpy array with shape nS

    Outputs:
        V: Value function (the expected future reward function). numpy array with shape nS
        pi: Policy (best action should I take at a specific state based on the current value). numpy array with shape nS
    """
    ######################################## your Implementation goes here ########################################
    ## your code
    ###############################################################################################################
    return V, pi