import json
import random


class Bot:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(actions)
        else:
            q_values = [self.get_q_value(state, action) for action in actions]
            max_q = max(q_values)
            max_actions = [actions[i] for i in range(len(actions)) if q_values[i] == max_q]
            return random.choice(max_actions)

    def update_q_value(self, state, action, reward, next_state, next_actions):
        old_value = self.get_q_value(state, action)
        future_rewards = [self.get_q_value(next_state, a) for a in next_actions] if next_actions else [0]
        best_future = max(future_rewards)
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * best_future)
        self.q_table[(state, action)] = new_value

    def save_learning(self, filename='qlearning_data.json'):
        with open(filename, 'w') as f:
            json.dump(self.q_table, f)

    def load_learning(self, filename='qlearning_data.json'):
        try:
            with open(filename, 'r') as f:
                self.q_table = json.load(f)
        except FileNotFoundError:
            self.q_table = {}


