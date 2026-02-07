from __future__ import annotations

# PYTORCH
import torch as pt
import torch.nn as nn


# 1. TENSOR

t = pt.tensor([1,2,3])
print(t)        # tensor([1, 2, 3])
print(type(t))  # <class 'torch.Tensor'>
print(t.shape)  # torch.Size([3])
print(t.dtype)  # torch.int64
print(t.device) # cpu


# 2. DIFFERENTES FACON CREER TENSOR

# 2.1 A partir de listes/tableaux python

t1 = pt.tensor([1.0, 2.0, 3.0])    # vecteur 1D
t2 = pt.tensor([[1, 2], [3, 4]])   # matrice 2x2
t3 = pt.tensor([1, 2, 3], dtype=pt.float32)

print(t2)       # tensor([[1, 2], [3, 4]])

print(t2.dtype) # torch.float32
print(t3.dtype) # torch.int64

print(type(t2)) # <class 'torch.Tensor'>
print(t2.shape) # torch.Size([2, 2])
print(t2.device)# cpu


# 2.2 Tenseurs “vides” : zeros, ones, random

a = pt.zeros(3, 4) # matrice 3x4 remplie de 0
b = pt.ones(2, 2)  # matrice 2x2 remplie de 1
c = pt.rand(3, 3)  # valeurs aléatoires entre 0 et 1
d = pt.randn(3, 3) # aléatoire ~ N(0, 1) (loi normale)

print(a)
print(b)
print(c)
print(d)

'''
tensor([[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]])
        
tensor([[1., 1.],
        [1., 1.]])
        
tensor([[0.5407, 0.5808, 0.6711],
        [0.2036, 0.5588, 0.1908],
        [0.5383, 0.2865, 0.5331]])
        
tensor([[-0.4368,  1.2665, -0.3445],
        [ 0.2364, -0.0081, -0.6510],
        [-1.8620, -0.5569,  1.3451]])
'''


# 2.3 Création “like” un autre tenseur

x = pt.rand(2, 3)
z0 = pt.zeros_like(x)    # même shape que x, que des 0
z1 = pt.ones_like(x)     # même shape que x, que des 1

print(x)
print(z0)
print(z1)

""" 
tensor([[0.2363, 0.3220, 0.2719],
        [0.7737, 0.9476, 0.2401]])
        
tensor([[0., 0., 0.],
        [0., 0., 0.]])
        
tensor([[1., 1., 1.],
        [1., 1., 1.]])
"""


# 3. Opérations de base sur les tenseurs

x = pt.tensor([1.0, 2.0, 3.0])
y = pt.tensor([4.0, 5.0, 6.0])

print(x + y)        # pt([5., 7., 9.])
print(x - y)        # pt([-3., -3., -3.])
print(x * y)        # pt([ 4., 10., 18.])
print(x / y)        # pt([0.2500, 0.4000, 0.5000])


# 4. Produit scalaire/matrice

A = pt.tensor([[1, 2], [3, 4]])
B = pt.tensor([[2, 1], [6, 10]])
C = A @ B           # ou pt.matmul(A, B)

print(C)            # tensor([[14, 21], [30, 43]])
print(C.shape)      # [2, 2]


# 5. Indexation / slicing

M = pt.tensor([[10, 11, 12],
               [20, 21, 22],
               [30, 31, 32]])

print(M[0, 0])     # 10
print(M[1])        # [20, 21, 22]
print(M[:, 1])     # deuxième colonne -> [11, 21, 31]
print(M[0:2, :])   # lignes 0 et 1


# 6. Changer la forme : view / reshape

x = pt.rand(2, 3, 4)    # shape [2, 3, 4]
y = x.view(2, -1)       # aplatis les 2 dernières dimensions
z = x.reshape(2, 12)    # pareil que y

print(x)
print(y)
print(z)
print(y.shape)
print(z.shape)

""" 
tensor([[[0.9853, 0.9358, 0.7876, 0.8036],
         [0.8037, 0.9424, 0.7104, 0.3340],
         [0.9440, 0.8380, 0.6935, 0.1380]],

        [[0.5449, 0.7929, 0.3227, 0.8956],
         [0.2248, 0.2116, 0.1179, 0.0529],
         [0.7427, 0.0903, 0.7179, 0.9919]]])
         
tensor([[0.9853, 0.9358, 0.7876, 0.8036, 0.8037, 0.9424, 0.7104, 0.3340, 0.9440, 0.8380, 0.6935, 0.1380],
        [0.5449, 0.7929, 0.3227, 0.8956, 0.2248, 0.2116, 0.1179, 0.0529, 0.7427, 0.0903, 0.7179, 0.9919]])
        
tensor([[0.9853, 0.9358, 0.7876, 0.8036, 0.8037, 0.9424, 0.7104, 0.3340, 0.9440, 0.8380, 0.6935, 0.1380],
        [0.5449, 0.7929, 0.3227, 0.8956, 0.2248, 0.2116, 0.1179, 0.0529, 0.7427, 0.0903, 0.7179, 0.9919]])
         
torch.Size([2, 12])
torch.Size([2, 12])
"""


# 7. Operations de réductions

x = pt.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])

print(x.sum())          # 21.0 (somme de tous les éléments)
print(x.mean())         # 3.5 (moyenne globale)
print(x.max())          # 6.0 (valeur max)
print(x.min())          # 1.0

print(x.sum(dim=0))   # somme colonne par colonne -> [5., 7., 9.]
print(x.sum(dim=1))   # somme ligne par ligne    -> [6., 15.]

values, indices = x.max(dim=1)
print(values)
print(indices)

""" 
tensor(21.)
tensor(3.5000)
tensor(6.)
tensor(1.)

tensor([5., 7., 9.])
tensor([ 6., 15.])

tensor([3., 6.])
tensor([2, 2])
"""

# 8 Concaténer / empiler des tenseurs : cat vs stack

a = pt.tensor([[1, 2],
                  [3, 4]])

b = pt.tensor([[5, 6],
                  [7, 8]])

c = pt.cat([a, b], dim=0)
# c = [[1, 2],
#      [3, 4],
#      [5, 6],
#      [7, 8]]

d = pt.cat([a, b], dim=1)
# d = [[1, 2, 5, 6],
#      [3, 4, 7, 8]]

s = pt.stack([a, b], dim=0)
print(s)
# shape: [2, 2, 2]
# s[0] = a, s[1] = b


# 9. Masques booléens & filtrage

x = pt.tensor([1, 2, 3, 4, 5])
mask = x > 3              # tensor([False, False, False, True, True])
print(x[mask])            # tensor([4, 5])

a = pt.tensor([1, 2, 3, 4])
b = pt.tensor([10, 20, 30, 40])
mask = a % 2 == 0

c = pt.where(mask, b, a)
# si mask[i] == True -> prend b[i], sinon a[i]
# -> [1, 20, 3, 40]

x = pt.tensor([1., 2., 3.])
x.add_(1.0)     # x devient [2., 3., 4.]


# 10. Autograd

x = pt.tensor(2.0, requires_grad=True)
y = x**3 + 4*x   # y = x³ + 4x

y.backward()      # dy/dx calculé automatiquement
print(x.grad)     # 3x² + 4 = 3*4 + 4 = 16


# 11. .detach() et with torch.no_grad()

#with pt.no_grad():
    #output = model(x)   # pas de gradient calculé

#tensor.detach() permet de prendre une valeur sans le lien grad :

#y = x.detach()

