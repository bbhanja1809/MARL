from functools import partial
from envs.multiagentenv import MultiAgentEnv
import sys
import os

from metadrive import (
    MultiAgentMetaDrive,
    MultiAgentTollgateEnv,
    MultiAgentBottleneckEnv,
    MultiAgentIntersectionEnv,
    MultiAgentRoundaboutEnv,
    MultiAgentParkingLotEnv
)

def env_fn(env, **kwargs):
    print(env)
    del kwargs['seed']
    return MultiAgentEnv(env(kwargs))

REGISTRY = {}

REGISTRY["MultiAgentMetaDrive"] = partial(env_fn, env=MultiAgentMetaDrive)
REGISTRY["MultiAgentTollgateEnv"] = partial(env_fn, env=MultiAgentTollgateEnv)
REGISTRY["MultiAgentBottleneckEnv"] = partial(env_fn, env=MultiAgentBottleneckEnv)
REGISTRY["MultiAgentIntersectionEnv"] = partial(env_fn, env=MultiAgentIntersectionEnv)
REGISTRY["MultiAgentRoundaboutEnv"] = partial(env_fn, env=MultiAgentRoundaboutEnv)
REGISTRY["MultiAgentParkingLotEnv"] = partial(env_fn, env=MultiAgentParkingLotEnv)
