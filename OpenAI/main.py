#!python3.9

from env import Environment

TOY = "CartPole-v1"

def main():
    cartpole = Environment(TOY)
    cartpole.run()

if __name__ == '__main__':
    main()