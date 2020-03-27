import numpy as np
from manimlib.imports import *
from scipy.spatial.distance import cdist

c_rng = (-3,3)
r_rng = (0.2,1)
n = 40

def generate_balls(n=n, c_rng = c_rng , r_rng=r_rng):
    cs = np.random.uniform(c_rng[0],c_rng[1],(n,3))
    cs[:,2:]=0
    rs = np.random.uniform(r_rng[0],r_rng[1],n)
    return list(zip(cs,rs))

def find_subcllection(balls):
    cs,rs = list(zip(*balls))
    cs = np.array(cs)[:,:-1]
    rs = np.array(rs)
    print(cs)

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
        print(sub)
    return sub

balls = generate_balls(n, c_rng, r_rng)

sub = find_subcllection(balls)