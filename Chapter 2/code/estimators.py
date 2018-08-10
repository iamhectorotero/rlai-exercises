import numpy as np


class Estimator(object):
    def __init__(self, action_value_initial_estimates):
        self.action_value_estimates = action_value_initial_estimates
        self.k_actions = len(action_value_initial_estimates)
        self.action_selected_count = np.full(self.k_actions, fill_value=0, dtype="int64")

    def select_action(self):
        raise NotImplementedError("Need to implement a method to select actions")

    def update_estimates(self):
        raise NotImplementedError("Need to implement a method to update action value estimates")

    def select_greedy_action(self):
        return np.argmax(self.action_value_estimates)

    def select_action_randomly(self):
        return np.random.choice(self.k_actions)


class SampleAverageEstimator(Estimator):
    def __init__(self, action_value_initial_estimates, epsilon):
        super(SampleAverageEstimator, self).__init__(action_value_initial_estimates)
        self.epsilon = epsilon

    def update_estimates(self, action_selected, r):
        self.action_selected_count[action_selected] += 1

        qn = self.action_value_estimates[action_selected]
        n = self.action_selected_count[action_selected]

        self.action_value_estimates[action_selected] = qn + (1.0 / n) * (r - qn)

    def select_action(self):
        probability = np.random.rand()
        if probability >= self.epsilon:
            return self.select_greedy_action()

        return self.select_action_randomly()


class WeightedEstimator(SampleAverageEstimator):
    def __init__(self, action_value_initial_estimates, epsilon=0, alpha=0.5):
        super(WeightedEstimator, self).__init__(action_value_initial_estimates, epsilon)
        self.alpha = alpha

    def update_estimates(self, action_selected, r):
        qn = self.action_value_estimates[action_selected]

        self.action_value_estimates[action_selected] = qn + self.alpha * (r - qn)


class UCBEstimator(WeightedEstimator):
    def __init__(self, action_value_initial_estimates, epsilon=0, alpha=0.5, c=2):
        super(UCBEstimator, self).__init__(action_value_initial_estimates, epsilon, alpha)
        self.c = c
        self.t = 0

    def select_action(self):
        self.t += 1
        probability = np.random.rand()
        if probability >= self.epsilon:
            return self.select_greedy_action()

        return self.select_ucb_action()

    def calculate_action_potential(self, action_i):
        q_t = self.action_value_estimates[action_i]
        ln_t = np.log(self.t)
        n_t = self.action_selected_count[action_i]

        return q_t + self.c * np.sqrt(ln_t / n_t)

    def select_ucb_action(self):
        greedy_action = self.select_greedy_action()

        if 0 in self.action_selected_count:
            actions_never_selected = [action_i for action_i in range(self.k_actions)
                                      if self.action_selected_count[action_i] == 0]
            selected_action = np.random.choice(actions_never_selected)
            self.action_selected_count[selected_action] += 1
            return selected_action

        action_potential = [self.calculate_action_potential(action_i) for action_i in range(self.k_actions)]
        action_potential[greedy_action] = -1

        return np.argmax(action_potential)


class GradientBandit(Estimator):
    def __init__(self, action_value_initial_estimates, alpha):
        super(GradientBandit, self).__init__(action_value_initial_estimates)
        self.average_reward = 0
        self.numerical_preference = np.full(self.k_actions, fill_value=0.)
        self.alpha = alpha

    def update_average_reward(self, r):
        qn = self.average_reward
        self.average_reward = qn + self.alpha * (r - qn)

    def update_estimates(self, action_selected, r):
        self.update_average_reward(r)

        P = self.get_actions_probabilities()
        baseline = self.average_reward

        ht = self.numerical_preference
        htp1 = ht - self.alpha * (r - baseline) * P
        htp1[action_selected] = ht[action_selected] + self.alpha * (r - baseline) * (1 - P[action_selected])

        self.numerical_preference = htp1

    def get_actions_probabilities(self):
        exp_numerical_preference = np.exp(self.numerical_preference)
        return exp_numerical_preference / np.sum(exp_numerical_preference)

    def select_action(self):
        return np.random.choice(a=self.k_actions, p=self.get_actions_probabilities())
