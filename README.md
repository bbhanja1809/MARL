## MARL
Project for Multi Agent RL environments.

```
conda env create -f environment.yml
conda activate rl-project
cd project/pymarl
```

# Commands for training individual environments  
**MultiAgentMetaDrive:**  
```
python3 src/main.py --config=qmix --env-config=metadrive
```
**MultiAgentTollgateEnv:**
```
python3 src/main.py --config=qmix --env-config=metadrive_tollgate
```
**MultiAgentBottleneckEnv:**
```
python3 src/main.py --config=qmix --env-config=metadrive_bottlekneck
```
**MultiAgentIntersectionEnv:**
```
python3 src/main.py --config=qmix --env-config=metadrive_intersection
```
**MultiAgentRoundaboutEnv:**
```
python3 src/main.py --config=qmix --env-config=metadrive_roundabout
```
**MultiAgentParkingLotEnv:**
```
python3 src/main.py --config=qmix --env-config=metadrive_parkinglot
```
