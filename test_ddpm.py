import mindspore
from mindspore import value_and_grad
from ddm import Unet, GaussianDiffusion
from ddm.ops import randn

model = Unet(
    dim = 64,
    dim_mults = (1, 2, 4, 8)
)

diffusion = GaussianDiffusion(
    model,
    image_size = 128,
    timesteps = 1000,   # number of steps
    loss_type = 'l1'    # L1 or L2
)

training_images = randn((1, 3, 128, 128)) # images are normalized from 0 to 1
grad_fn = value_and_grad(diffusion, None, diffusion.trainable_params())

loss, grads = grad_fn(training_images)
# after a lot of training

sampled_images = diffusion.sample(batch_size = 1)
print(sampled_images.shape) # (4, 3, 128, 128)