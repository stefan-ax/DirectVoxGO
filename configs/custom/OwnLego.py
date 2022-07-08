# inherit default setting for custom forward-facing
# _base_ = './default_forward_facing.py'
_base_ = './default_ubd_inward_facing.py'

# name your scene
expname = 'MyScene'

data = dict(
    datadir='./data/custom/lego-custom/dense',  # path to the root of your images
    factor=2,                               # the training images resolution
)