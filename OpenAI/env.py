import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import gym

from agent import Agent

# 最大ステップ数
MAX_STEPS = 200
# 最大試行回数
MAX_EPISODES = 1000

class Environment():
    # コンストラクタ
    def __init__(self, toy_env):
        # 環境生成
        self.env = gym.make(toy_env)

        num_states = self.env.observation_space.shape[0]

        num_action = self.env.action_space.n

        self.agent = Agent(num_states, num_action)

    def run(self):
        complete_episode = 0        # 成功した数
        step_list = []
        is_episode_final = False    # 最後の試行
        frames = []                 # 画像保存用変数

        for episode in range(MAX_EPISODES):
            # 環境初期化
            observation, _ = self.env.reset()
            self.env.render()
            for step in range(MAX_STEPS):
                # 最終エピソードを画像として保存
                if is_episode_final:
                    frames.append(self.env.render(mode='rgb_array'))
                
                # 行動の選択
                action = self.agent.get_action(observation, episode)
                # 
                observation_next, _, done, _, _ = self.env.step(action)
                #zzz = self.env.step(action)
                #done = True

                if done:
                    if step < 195:
                        reward = -1
                        complete_episode = 0
                    else:
                        reward = 1
                        complete_episode += 1
                else:
                    reward = 0

                # Qテーブルの更新
                self.agent.update_Q_function(observation, action, reward, observation_next)
                # 次の観測へ
                observation = observation_next

                if done:
                    step_list.append(step+1)
                    break
            
            if is_episode_final:
                es = np.arange(0, len(step_list))
                plt.plot(es, step_list)
                plt.savefig("cartpole.png")
                plt.figure()
                patch = plt.imshow(frames[0])
                plt.axis('off')

                def animate(i):
                    patch.set_data(frames[i])

                anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval=50)
                anim.save('cartpole.mp4', "ffmpeg")
                break

            if complete_episode >= 100:
                print('100回連続成功')
                is_episode_final = True
        
                    

