import torch as th
from syft import deserialize

x = th.tensor([1.0, 2, 3, 4], requires_grad=True)

blob = x.serialize()
x2 = deserialize(blob=blob)

assert (x == x2).all()
