#!env python
import numpy as np
import scipy as sp
import dit
import scipy.io
import itertools

dat = sp.io.loadmat('pyP.mat')
P = np.squeeze(dat['P'])
s = P.shape
Nvar = len(P.shape)
d = dit.Distribution(*zip(*np.ndenumerate(P)))

from dit.algorithms.scipy_optimizers import maxent_dist

pairwise_marginals = list(itertools.combinations(range(Nvar),2))
me2 = maxent_dist(d, pairwise_marginals) 
me2.make_dense()

P2 = me2.pmf.reshape(s,order='C')
dat['P2'] = P2
sp.io.savemat('pyP.mat',dat)
