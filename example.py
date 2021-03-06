import gym
from gymhearts import env as hearts_env

env = hearts_env.HeartsEnv()

env.render()

observation = env.get_observation()

done = False
while not done:
    action = observation['valid_hand_cards'][0]
    observation, reward, done, info = env.step(action)
    env.render()
