# PyTorch forward-mode is not mature yet
from torch.func import hessian, jacfwd, jvp
from torch._functorch.vmap import chunk_vmap
from .batch_norm_replacement import replace_all_batch_norm_modules_
from functorch import functionalize
