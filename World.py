import pybullet as p 
import pybullet_data 


class World():



    def __init__(self):


        
        self.envs = []

        origins = [(-5, 0), (-10, 0), (-15, 0)]

        for origin in origins:
            env = Environment(p, origin)
            self.envs.append(envs)

