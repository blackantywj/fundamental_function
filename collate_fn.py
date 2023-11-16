import torch
import torch.utils.data as Data
import numpy as np

test = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

inputing = torch.tensor(np.array([test[i:i+3] for i in range(10)]))
target = torch.tensor(np.array([test[i:i + 1] for i in range(10)]))

torch_dataset = Data.TensorDataset(inputing, target)

batch = 3

loader = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=batch,
    collate_fn=lambda x:(torch.cat([x[i][j].unsqueeze(0) for i in range(len(x))], 0) for j in range(len(x[0]))),
)

for (i, j) in loader:
    print(i, j)
    