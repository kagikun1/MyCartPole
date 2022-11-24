import gym
import warnings

#warnings.simplefilter('ignore')

env = gym.make('CartPole-v1', render_mode="human")
observation = env.reset()

for i_episode in range(20):
    observation = env.reset()
    total_reward = 0
    for t in range(100):
        env.render()
        action = 1
        # sum_obs = observation[0] + observation[1] + observation[2] + observation[3]
        # if sum_obs > 0:
        #     action = 1
        # else:
        #     action = 0
        observation, reward, terminated, truncated, info= env.step(action)
        #total_reward += 1

        print(observation, reward, terminated, truncated, info)
        if terminated:
            print("Episode finished after {} timesteps".format(t+1))
            break