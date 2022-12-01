# Qテーブルのサイズ調整や更新手法、行動選択方法を記述するファイル

import numpy as np

# 区画数
NUM_DIZITIZED = 5

# 学習用パラメータ
alpha = 0.5     # 学習係数
gamma = 0.99    # 時間割引率

class State:
    # q_tableの作成
    # コンストラクタ
    def __init__ (self, num_states, num_actions):
        self.num_actions = num_actions

        self.q_table = np.random.uniform(low=-1, high=1, size=(NUM_DIZITIZED**num_states, num_actions))

    # 観測した状態をデジタル変換する閾値を求める
    # numpy.linspace(<開始値>, <終了値>, <要素数>)
    def bins(self, clip_min, clip_max, num):
        return np.linspace(clip_min, clip_max, num + 1)[1 : -1]

    # アナログデータのデジタル変換
    def analog2digitize(self, observation):
        cart_pos, cart_speed, pole_angle, pole_speed = observation
        # numpy.digitize(<元データ>, bins=<区画の設定 ex) [-50, -10, 0, 10, 50]>)
        # <元データ>がbinsのどこの区画に属するかを返す
        digitized = [
            np.digitize(cart_pos, bins=self.bins(-2.4, 2.4, NUM_DIZITIZED)),
            np.digitize(cart_speed, bins=self.bins(-3.0, 3.0, NUM_DIZITIZED)),
            np.digitize(pole_angle, bins=self.bins(-0.5, 0.5, NUM_DIZITIZED)),
            np.digitize(pole_speed, bins=self.bins(-2.0, 2.0, NUM_DIZITIZED))
        ]

        return sum([x * (NUM_DIZITIZED**i) for i, x in enumerate(digitized)])

    # q_tableの更新
    def update_Q_table(self, observation, action, reward, observation_next):
        # 受け取った値をデジタルデータへ変換する
        state = self.analog2digitize(observation)
        state_next = self.analog2digitize(observation_next)
        Max_Q_next = max(self.q_table[state_next][:])

        # q_tableの更新
        self.q_table[state, action] = self.q_table[state, action] + alpha * (reward + gamma * Max_Q_next - self.q_table[state, action])

    # 行動の選択
    def get_action(self, observation, episode):
        state = self.analog2digitize(observation)
        epsilon = 0.5 * (1/(episode + 1))

        if epsilon <= np.random.uniform(0, 1):
            # 最も価値の高い行動を選択
            action = np.argmax(self.q_table[state][:])
        else:
            # ランダムに行動
            action = np.random.choice(self.num_actions)

        return action