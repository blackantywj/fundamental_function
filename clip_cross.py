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

#NT_BXENT_LOSS B是binary
class NT_BXENT_LOSS(nn.Module):
    def __init__(self):
            super(NT_BXENT_LOSS,self).__init__()
 
    def forward(self, x, pos_indices, temperature):
        assert len(x.size()) == 2
 
        # Add indexes of the principal diagonal elements to pos_indices
        pos_indices = torch.cat([
            pos_indices,
            torch.arange(x.size(0)).reshape(x.size(0), 1).expand(-1, 2),
        ], dim=0)
        
        # Ground truth labels
        target = torch.zeros(x.size(0), x.size(0))
        target[pos_indices[:,0], pos_indices[:,1]] = 1.0
        target = target.cuda()
 
        # Cosine similarity
        xcs = F.cosine_similarity(x[None,:,:], x[:,None,:], dim=-1)
        # Set logit of diagonal element to "inf" signifying complete
        # correlation. sigmoid(inf) = 1.0 so this will work out nicely
        # when computing the Binary cross-entropy Loss.
        xcs[torch.eye(x.size(0)).bool()] = float("inf")
 
        # Standard binary cross-entropy loss. We use binary_cross_entropy() here and not
        # binary_cross_entropy_with_logits() because of
        # https://github.com/pytorch/pytorch/issues/102894
        # The method *_with_logits() uses the log-sum-exp-trick, which causes inf and -inf values
        # to result in a NaN result.
        loss = F.binary_cross_entropy((xcs / temperature).sigmoid(), target, reduction="none")
        
        target_pos = target.bool()
        target_neg = ~target_pos
        
        pos_zero = torch.zeros(x.size(0), x.size(0))
        neg_zero = torch.zeros(x.size(0), x.size(0))
        pos_zero, neg_zero = pos_zero.cuda(), neg_zero.cuda()
 
        loss_pos = pos_zero.masked_scatter(target_pos, loss[target_pos])
        loss_neg = neg_zero.masked_scatter(target_neg, loss[target_neg])
        loss_pos = loss_pos.sum(dim=1)
        loss_neg = loss_neg.sum(dim=1)
        num_pos = target.sum(dim=1)
        num_neg = x.size(0) - num_pos
 
        return ((loss_pos / num_pos) + (loss_neg / num_neg)).mean()


# NT_Xent loss
def nt_xent_loss(x, temperature):
  assert len(x.size()) == 2

  # Cosine similarity
  xcs = F.cosine_similarity(x[None,:,:], x[:,None,:], dim=-1)
  xcs[torch.eye(x.size(0)).bool()] = float("-inf")

  # Ground truth labels
  target = torch.arange(8)
  target[0::2] += 1
  target[1::2] -= 1

  # Standard cross-entropy loss
  return F.cross_entropy(xcs / temperature, target, reduction="mean")
