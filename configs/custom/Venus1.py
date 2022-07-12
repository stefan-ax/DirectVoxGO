# inherit default setting for custom forward-facing
# _base_ = './default_forward_facing.py'
_base_ = './default_ubd_inward_facing.py'

# name your scene
expname = 'Venus-1'

data = dict(
    datadir='./data/custom/venus-rough-1/dense',  # path to the root of your images
    factor=4,                               # the training images resolution
)

fine_train = dict(
    N_iters=5000,
)

fine_model_and_render = dict(
    num_voxels=160**3,
    num_voxels_base=160**3
)