import torch
from torch import nn
#随机生成一个神经网络的最后一层，3行4列，那就是有4个标签
input = torch.randn(3,4)
#input的第一行设置为标签1，第二行为标签0,
label = torch.tensor([1,0,2])

#人工设置种子，不然每次计算loss不一样，我们通过固定种子就可以固定loss
torch.manual_seed(2)

#定义损失函数为NLLLoss
loss = nn.CrossEntropyLoss()

#计算损失，损失就是一个值。
loss_value = loss(input,label)
print(loss_value)


# input = torch.randn(3,4)
# #input的第一行设置为标签1，第二行为标签0,
# label = torch.tensor([1,0,2])

#人工设置种子，不然每次计算loss不一样，我们通过固定种子就可以固定loss
torch.manual_seed(2)

#定义损失函数为NLLLoss
loss = nn.NLLLoss()
#定义log softmax函数，也就是将input中的每一行转化为带有负号的数字
m = nn.LogSoftmax(dim=1)
#计算损失，损失就是一个值。
loss_value = loss(m(input),label)
print(loss_value)