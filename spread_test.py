"""
@ref https://pettingzoo.farama.org/environments/mpe/simple_adversary/
"""
from pettingzoo.mpe import simple_spread_v3

def aec():
    env = simple_spread_v3.env(render_mode="human")
    env.reset(seed=42)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
        else:
            # this is where you would insert your policy
            action = env.action_space(agent).sample()

        print(action)

        env.step(action)

    env.close()

def parallel():
    env = simple_spread_v3.parallel_env(render_mode="human")
    observations, infos = env.reset()
    while env.agents:
        print("curstep: ", env.aec_env.steps)
        # this is where you would insert your policy
        actions = {agent: env.action_space(agent).sample() for agent in env.agents}
        observations, rewards, terminations, truncations, infos = env.step(actions)
        print("current entities id: ", env.entities)
        print(observations)

    env.close()

def main():
    #aec()
    parallel()

if __name__ == "__main__":
    main()
