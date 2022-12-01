# エージェントが取る行動を記述したファイル

from state import State

class Agent:
    # コンストラクタ
    def __init__(self, num_states, num_actions):
        self.state = State(num_states, num_actions)

    def update_Q_function(self, observation, action, reward, observation_next):
        # Qテーブルの更新
        self.state.update_Q_table(observation, action, reward, observation_next)

    def get_action(self, observation, step):
        # 行動の選択
        action = self.state.get_action(observation, step)
        
        return action