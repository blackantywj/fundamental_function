import torch
import torch.nn.functional as F
from torch import nn
import numpy as np
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

def cross_entropy_np(x, y):
    x_softmax = [softmax(x[i]) for i in range(len(x))]
    x_log = [np.log(x_softmax[i][y[i]]) for i in range(len(y))]
    loss = - np.sum(x_log) / len(y)
    return loss
def get_logits( image_features, text_features, logit_scale):
    # 计算image_features @ text_features.T相似度矩阵
    logits_per_image = logit_scale * image_features @ text_features.T
    logits_per_text = logit_scale * text_features @ image_features.T
    return logits_per_image, logits_per_text

def cal_clip_loss(image_features, text_features, logit_scale):
    device = image_features.device
    logits_per_image, logits_per_text = get_logits(image_features, text_features, logit_scale)
    labels = torch.arange(logits_per_image.shape[0], device=device, dtype=torch.long)
    total_loss = (
        F.cross_entropy(logits_per_image, labels) +
        F.cross_entropy(logits_per_text, labels)
    ) / 2
    li = logits_per_image.detach().numpy().tolist()
    lt = logits_per_image.detach().numpy().tolist()
    la = labels.detach().numpy().tolist()
    print(li, lt, la)
    print((
        cross_entropy_np(li, la) +
        cross_entropy_np(lt, la)
    ) / 2)
    return {"contrastive_loss": total_loss}
# 实际代码：image_features =encode_image(image, normalize=True)
image_features = torch.randn(32, 768)
# 实际代码：text_features =encode_text(text, normalize=True)
text_features = torch.randn(32, 768)
logit_scale = 0.01
print(cal_clip_loss(image_features,text_features,logit_scale))