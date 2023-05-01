import argparse
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--exp_name', '-xn', type=str, default='my_exp', help='name of the experiment')
    # args = parser.parse_args()
    # params = vars(args)

    # Load pkl-file containing the learning (reward) history
    for i in sys.argv[1:]:
        file_name = i 
        with open(file_name, 'rb') as f:
            ro_reward = pickle.load(f)
        sns.lineplot(data=ro_reward, linestyle='--', label=i)
            
    # file_name = params['exp_name'] + '.pkl'
    # with open(file_name, 'rb') as f:
    #     ro_reward = pickle.load(f)

    # Plot the data
    
    plt.xlabel('rollout', fontsize=25, labelpad=-2)
    plt.ylabel('reward', fontsize=25)
    plt.title('Learning curve for CartPole', fontsize=30)
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
