# implement a flexible event logging system for applications and libraries

import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from orderbook import Orderbook


class Trade_Environment(gym.Env):
    metadata = {'render.modes' : ['human']}
    """
    Description:
        The environment that agent can see is sequence of limit order book.
        The goal is to achieve maximum revenue through putting only market orders.

    Observation:

    Actions:
        Type: Discrete(3)
        Num     Action
        0       Buy
        1       Sell
        2       Wait

        Note: The agent is trading futures meaning the agent can sell first and buy back later.

    Reward: Depends if inventory if we have positive inventory or negative inventory

    Starting State: random starting state generated in Orderbook class

    Episode Termination: When there is no more data next bid or next ask terminate

    """

    def __init__(self):
        self.observation_space = spaces.Box(-float(9999999999), float(9999999999), shape=(20,1), dtype=np.float64)
        self.action_space = spaces.Discrete(3)
        self.inventory = 0
        self.seed()
        self.state = None

    def step(self, action):

        assert self.action_space.contains(action)

        try:
            self.orderbook.append(self.data_generator.next())
        except StopIteration:
            done = True

        best_bid = Orderbook.getBestBid()
        best_ask = Orderbook.getBestAsk()

        next_bid = Orderbook.getNextBestBid()
        next_ask = Orderbook.getNExtBestAsk()

        # Buy
        if action == 0:
            self.inventory += 1
        # Sell
        elif action == 1:
            self.inventory -= 1
        if self.inventory > 0:
            start = best_ask
            end = next_bid
        elif self.inventory <= 0:
            start = best_bid
            end = next_ask

        reward = (end/start -1) * self.inventory
        self.state += 1
        done = False

        return reward, done, {}

    def reset(self):

        return

    def render(self, mode='human', close=False):
        pass

    def seed(self, seed=None):
        self.np_random, seed - seeding.np_random(seed)
        return [seed]
