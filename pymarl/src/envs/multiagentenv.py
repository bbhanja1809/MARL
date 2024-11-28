import gym
from gym import Wrapper
class MultiAgentEnv(Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.episode_limit = 1000
        self.n_agents = self.default_config()["num_agents"]

    def step(self, actions):
        """ Returns reward, terminated, info """
        return self.step(actions)

    def get_obs(self):
        """ Returns all agent observations in a list """
        combined_obs = list(self._get_observations().values())
        return combined_obs
 
    def get_obs_agent(self, agent_id):
        """ Returns observation for agent_id """
        agent_obs = self._get_observations()[agent_id]
        return agent_obs

    def get_obs_size(self):
        """ Returns the shape of the observation """
        obs_dict = self._get_observations()
        size = obs_dict.values().shape()
        return size

    def get_state(self):    
        return self.get_obs()        

    def get_state_size(self):
        """ Returns the shape of the state"""
        return self.get_obs_size()        

    def get_avail_actions(self):
        return self.action_space        

    def get_avail_agent_actions(self, agent_id):
        """ Returns the available actions for agent_id """
        return self.action_space[agent_id]        

    def get_total_actions(self):
        """ Returns the total number of actions an agent could ever take """
        # TODO: This is only suitable for a discrete 1 dimensional action space for each agent
        raise NotImplementedError

    def reset(self):
        """ Returns initial observations and states"""
        return self.reset()

    def render(self):
        return self.render()

    def close(self):
        return super.close()

    def seed(self):
        return 123

    def save_replay(self):
        raise NotImplementedError

    def get_env_info(self):
        env_info = {"state_shape": self.get_state_size(),
                    "obs_shape": self.get_obs_size(),
                    "n_actions": self.get_total_actions(),
                    "n_agents": self.n_agents,
                    "episode_limit": self.episode_limit}
        return env_info
