import numpy as np
import torch
def partition_assign(a, n):
    idx = np.argpartition(a,-n,axis=1)[:,-n:]
    #out = np.zeros(a.shape, dtype=int)
    np.put_along_axis(a,idx,1,axis=1)
    return a
a= torch.tensor([[0.1,0.2,0.3,0.4],[0.2,0.4,0.2,0.2]])
b=torch.rand(1,4)
c= torch.tensor([0.2,0.3,0.2,0.5])
d= torch.tensor([0.2,0.3])
print(a)
print(b)
maxvalue,maxindex = torch.max(a,dim=-1)
print(maxvalue)
print(c[maxindex])
print(maxvalue.ge(c[maxindex])*d)

print(maxvalue)
print(maxvalue.mean())

print(a.mean(0))

print(a.mean(0)+b)
maxvalue1,maxindex1 = torch.max(a.mean(0),dim=0)
print(maxvalue1)
print(a.mean(0)/maxvalue1)
print((a.mean(0)/maxvalue1)*2)


# b=torch.tensor(partition_assign(a,2),dtype=torch.float)
# b=torch.tensor(partition_assign(a.cpu().numpy(),1),dtype=torch.float)
# print(b)
# print(b.cuda())

