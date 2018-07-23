from tqdm import tqdm
from numpy.random import normal as GaussianDistribution
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(250)


class K_armed_testbed():
    # Q*-values for each one of the k possible actions start out equal
    # and then take independent random walks

    def __init__(self, k_actions):
        self.k = k_actions
        # self.action_values = GaussianDistribution(loc=0, scale=1, size=self.k)
        self.action_values = np.full(self.k, fill_value=0.0)

    def random_walk_action_values(self):
        increment = GaussianDistribution(loc=0, scale=0.01, size=self.k)
        self.action_values += increment

    def sample_action(self, action_i):
        return GaussianDistribution(loc=self.action_values[action_i], scale=1, size=1)[0]

    def get_optimal_action(self):
        return np.argmax(self.action_values)

    def get_optimal_action_value(self):
        return self.action_values[self.get_optimal_action()]

    def is_optimal_action(self, action_i):
        return float(self.get_optimal_action_value() == self.action_values[action_i])

    def __str__(self):
        return "\t".join(["A%d: %.2f" % (action_i, self.action_values[action_i]) for action_i in range(self.k)])


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
        probability = np.random.uniform(0, 1)
        if probability >= self.epsilon:
            return self.select_greedy_action()

        return self.select_action_randomly()


class WeightedEstimator(Estimator):
    def __init__(self, action_value_initial_estimates, epsilon=0, alpha=0.5):
        super(WeightedEstimator, self).__init__(action_value_initial_estimates)
        self.epsilon = epsilon
        self.alpha = alpha

    def update_estimates(self, action_selected, r):
        qn = self.action_value_estimates[action_selected]

        self.action_value_estimates[action_selected] = qn + self.alpha * (r - qn)

    def select_action(self):
        probability = np.random.rand()
        if probability >= self.epsilon:
            return self.select_greedy_action()

        return self.select_action_randomly()


def plot_performance(estimator_names, rewards, action_optimality):
    for i, estimator_name in enumerate(estimator_names):
        average_run_rewards = np.sum(rewards[i], axis=0) / N_RUNS
        plt.plot(average_run_rewards, label=estimator_name)

    plt.legend()
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    plt.show()

    for i, estimator_name in enumerate(estimator_names):
        average_run_optimality = np.sum(action_optimality[i], axis=0) / N_RUNS
        plt.plot(average_run_optimality, label=estimator_name)
    plt.legend()
    plt.xlabel("Steps")
    plt.ylabel("% Optimal action")
    plt.show()


if __name__ == "__main__":
    K = 10
    n_steps = 10000
    N_RUNS = 2000
    N_ESTIMATORS = 2

    rewards = [[[] for _ in range(N_RUNS)] for _ in range(N_ESTIMATORS)]
    optimal_selections = [[[] for _ in range(N_RUNS)] for _ in range(N_ESTIMATORS)]

    for run_i in tqdm(range(N_RUNS)):

        testbed = K_armed_testbed(k_actions=K)
        sample_average_estimator = SampleAverageEstimator(action_value_initial_estimates=np.full(K, fill_value=0.0), epsilon=0.1)
        weighted_estimator = WeightedEstimator(action_value_initial_estimates=np.full(K, fill_value=0.0), epsilon=0.1, alpha=0.1)

        estimators = [sample_average_estimator, weighted_estimator]

        for step_i in range(n_steps):
            for estimator_i, estimator in enumerate(estimators):
                action_selected = estimator.select_action()
                is_optimal = testbed.is_optimal_action(action_selected)
                reward = testbed.sample_action(action_selected)
                estimator.update_estimates(action_selected, reward)

                rewards[estimator_i][run_i].append(reward)
                optimal_selections[estimator_i][run_i].append(is_optimal)

            testbed.random_walk_action_values()

    plot_performance(["Ɛ=0.1", "Ɛ=0.1 α=0.1"], np.array(rewards), np.array(optimal_selections))
