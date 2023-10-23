import torch
import torch.nn as nn
import torch.nn.functional as F
 
data = torch.randn(2, 6)
print('data:', data, '\n')
 
log_soft = F.log_softmax(data, dim=1)
print('log_soft:', log_soft, '\n')
 
target = torch.tensor([1, 2])
 
entropy_out = F.cross_entropy(data, target)
nll_out = F.nll_loss(log_soft, target)
 
print('entropy_out:', entropy_out)
print('nll_out:', nll_out)