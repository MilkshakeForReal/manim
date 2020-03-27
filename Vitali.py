import numpy as np
from manimlib.imports import *
from scipy.spatial.distance import cdist
c_rng = (-3,3)
r_rng = (0.2,1)
n = 50

def generate_balls(n=n, c_rng = c_rng , r_rng=r_rng):
    cs = np.random.uniform(c_rng[0],c_rng[1],(n,3))
    cs[:,2:]=0
    rs = np.random.uniform(r_rng[0],r_rng[1],n)
    return list(zip(cs,rs))

def find_subcllection(balls):
    cs,rs = list(zip(*balls))
    cs = np.array(cs)[:,:-1]
    rs = np.array(rs)

    all = list(range(n))
    sub = []
    sub.append(np.argmax(rs))
    k=0
    while True:
        candidates = np.array(list(set(all) - set(sub)))
        dists = cdist(cs[candidates,:], cs[sub,:],'euclidean')
        rad_sum = rs[candidates].reshape(-1,1)+rs[sub].reshape(1,-1)
        disjoint = np.all(dists>=rad_sum, axis =1)
        if np.sum(disjoint)==0:
            break
        #disjoint = list(map(int, disjoint))
        candidates = candidates[disjoint]
        j = np.argmax(rs[candidates])
        #if j in sub:
        #    break
        sub.append(candidates[j])
    return sub

class Graph(GraphScene):
    CONFIG = {
        "y_max" : (c_rng[1]+5*r_rng[1])*3,
        "y_min" : (c_rng[0]-5*r_rng[1])*3,
        "x_max" : (c_rng[1]+5*r_rng[1])*3,
        "x_min" : (c_rng[0]-5*r_rng[1])*3,
        #"axes_color" : BLUE,
    }
    def construct(self):
        data,balls = self.get_balls()
        sub = find_subcllection(data)

        for i in range(n):
            self.play(ShowCreation(balls[i]), run_time = 0.2)
            self.wait(1/30)
        self.wait(2)

        copys = []
        for i in sub:
            copy = Circle(
                radius=balls[i].radius,
                color = YELLOW,
                fill_color = DARK_BLUE
            ).move_to(balls[i].get_center())
            copys.append(copy)
            self.play(ShowCreation(copy), run_time = 0.3)
            self.wait(1/30)

        self.wait(3)
        self.play(Group(*self.mobjects).scale, 1 / 3,run_time = 2)
        self.wait(3)

        self.play(*[
            ApplyMethod(i.scale,3) for i in copys
        ])
        self.wait(3)

    def get_balls(self):
        data = generate_balls(n, c_rng, r_rng)
        balls = []
        for i in range(n):
            circle = Circle(radius=data[i][1], color=BLUE).move_to(data[i][0])
            balls.append(circle)
        return data, balls

