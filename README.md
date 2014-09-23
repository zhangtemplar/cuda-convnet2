cuda-convnet2
=============

This repository is cloned from https://code.google.com/p/cuda-convnet2 for my own research.

start
=============
If you found errors related to some libaray not found, please use the following command export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-6.5/lib64/:$root-cuda-convnet2/nvmatrix/bin/release


files
=============

results
=============
  imagenet 2014, classification, 5000 images per batch, full validation and full training, 90 epochs, default configurations "python convnet.py --data-path /usr/local/storage/akrizhevsky/ilsvrc-2012-batches --train-range 0-417 --test-range 1000-1016 --save-path /usr/local/storage/akrizhevsky/tmp  --epochs 90 --layer-def layers/layers-imagenet-1gpu.cfg --layer-params layers/layer-params-imagenet-1gpu.cfg --data-provider image --inner-size 224 --gpu 0 --mini 128 --test-freq 201 --color-noise 0.1". Results is 86.518% on validation set with multiview method 0.
