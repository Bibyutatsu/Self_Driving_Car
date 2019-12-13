# Self_Driving_Car
A python implementation for [Deep Reinforcement Learning using Genetic Algorithm for Parameter Optimization](https://arxiv.org/pdf/1905.04100.pdf) and [Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning](https://arxiv.org/abs/1712.06567)

There are many implementations of this idea which can be found on git but most of them are implemented in Unity with C#. So I have tried contributing to the python lovers and implemented a basic simulation of this idea in an environment created using `pymunk` and `pyglet`. 

The basic idea is to use Genetic Algorithm to find the best weights of a Neural Network which outperforms the traditional advanced reinforcement learning algorithms in learning how to play a game. Here I have created a very basic game using pymunk and pyglet in which a car needs to go from one end to the other.

So for this we created 10 cars at each epoch and assigned random neural networks to each of them and then gave rewards based on the distance it travels without colliding. This reward is used for sorting the neural networks from worst to best. So at each epoch the Genetic Algorithm evolves the Neural Networks and we get new Neural Networks slightly better than the previous generation. The best model for each epoch is saved in `Model`

For experimenting and playing with it run `window.py`.


## Dependencies
- Pymunk
- Pyglet
- Pytorch