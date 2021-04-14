# TensorBox

Thanks to http://github.com/russell91/tensorbox. And I put his repo to here in order to study his code and this arv:https://arxiv.org/abs/1506.04878 (end to  end people detection in crowded scenes)<br>

1.git clone https://github.com/zhucheng725/TensorBox <br>
2.cd Tensorbox <br>
3.cd /path/to/Tensorbox/utils && python3 setup.py install && cd .. <br>

4.python3 evaluate_lift.py --weights output/ckpt/save.ckpt-10000  --min_conf 0.95 <br>

You can modify the model_lift.py 
``` 
img1_path = '/media/kirito/1T/procedure/TensorBox/data/testdata/img/'+str(i) + '.jpg'
imname = '/media/kirito/1T/procedure/TensorBox/data/testdata/result_'+ str(i) +'.jpg'
cv2.imwrite(imname, new_img)
```



