from gym_maze import envs
from itertools import count
import time


env = envs.MazeEnvRandom10x10()

observation = env.reset()

for i in count():
    env.render()
    time.sleep(1/12)

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    if done:
        break




