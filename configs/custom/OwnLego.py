# inherit default setting for custom forward-facing
# _base_ = './default_forward_facing.py'
_base_ = './default_ubd_inward_facing.py'

# name your scene
expname = 'OwnLego'

data = dict(
    datadir='./data/custom/lego-custom/dense',  # path to the root of your images
    factor=2,                               # the training images resolution
    dataset_type='blender',
    white_bkgd=True
)

fine_train = dict(
    N_iters=5000,
)

fine_model_and_render = dict(
    num_voxels=160**3,
    num_voxels_base=160**3
)