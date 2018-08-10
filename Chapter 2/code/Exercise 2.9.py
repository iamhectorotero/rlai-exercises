import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from testbed import K_armed_testbed
from estimators import SampleAverageEstimator, WeightedEstimator, GradientBandit, UCBEstimator

np.random.seed(250)


def plot_performance_of_parameter_settings(parameter_settings, estimator_names, performance_results):

    for estimator_i, estimator_results in enumerate(performance_results):
        average_parameter_results = []
        for parameter_setting_results in estimator_results:
            average_run_results = np.average(parameter_setting_results, axis=0)
            average_step_rewards = np.average(average_run_results)
            average_parameter_results.append(average_step_rewards)

        plt.plot(parameter_settings, average_parameter_results, label=estimator_names[estimator_i])

    plt.legend()
    plt.xlabel("ε, α, c, Q0")
    plt.xscale("log", basex=2)
    plt.ylabel("Average reward over last %d steps" % AVERAGE_OVER_LAST_N_STEPS)
    plt.show()


if __name__ == "__main__":
    with open("runs.csv", "w+") as csvfile:
        csvfile.write("algorithm_id,parameter_setting,run_i\n")
    K = 10
    N_STEPS = 200000
    N_RUNS = 10
    N_ESTIMATORS = 4
    AVERAGE_OVER_LAST_N_STEPS = 100000

    starting_index = N_STEPS - AVERAGE_OVER_LAST_N_STEPS

    parameter_settings = [1.0/128, 1.0/64, 1.0/32, 1.0/16, 1.0/8, 1.0/4, 1.0/2, 1.0, 2.0, 4.0]

    rewards = np.full((N_ESTIMATORS, len(parameter_settings), N_RUNS, AVERAGE_OVER_LAST_N_STEPS), fill_value=0.)

    for parameter_setting_i, parameter_setting in tqdm(enumerate(parameter_settings), total=len(parameter_settings)):
        for run_i in tqdm(range(N_RUNS)):

            testbed = K_armed_testbed(k_actions=K)

            action_value_estimates = np.full(K, fill_value=0.0)
            sample_average_estimator = SampleAverageEstimator(action_value_estimates.copy(), epsilon=parameter_setting)
            weighted_estimator = WeightedEstimator(action_value_estimates.copy(), epsilon=0.1, alpha=parameter_setting)
            ucb = UCBEstimator(action_value_estimates.copy(), epsilon=0.1, alpha=0.1, c=parameter_setting)
            gradient_bandit = GradientBandit(action_value_estimates.copy(), alpha=parameter_setting)

            estimators = [sample_average_estimator, weighted_estimator, ucb, gradient_bandit]

            for step_i in tqdm(range(N_STEPS)):
                for estimator_i, estimator in enumerate(estimators):
                    action_selected = estimator.select_action()
                    reward = testbed.sample_action(action_selected)
                    estimator.update_estimates(action_selected, reward)

                    if step_i >= starting_index:
                        rewards[estimator_i][parameter_setting_i][run_i][step_i - starting_index] = reward

                testbed.random_walk_action_values()

    estimator_names = ["Sample Average Estimator", "Constant Step-size Estimator", "UCB", "Gradient Bandit"]
    plot_performance_of_parameter_settings(parameter_settings, estimator_names, rewards)
