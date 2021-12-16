python image_source.py --trte val --output ckps/source/ --da uda --gpu_id 0 --dset visda --net resnet101 --lr 1e-3 --max_epoch 10 --s 0

python image_target.py --cls_par 0.3 --da uda --dset visda --gpu_id 2 --s 0 --output_src ckps/source/ --output ckps/target/ --net resnet101 --lr 1e-3
