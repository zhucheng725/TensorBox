# TensorBox
Thanks to http://github.com/russell91/tensorbox and backup here in order to  study easily.(https://arxiv.org/abs/1506.04878)(End-to-end people detection in crowded scenes)<br>
```
1.git clone https://github.com/zhucheng725/TensorBox
2.cd Tensorbox
3.cd /path/to/Tensorbox/utils &&mkdir build && python3 setup.py install && cd ..
4.python3 evaluate_lift.py --weights output/ckpt/save.ckpt-10000  --min_conf 0.95
```
You can modify model_lift.py<br>
```
img1_path = '/media/kirito/1T/procedure/TensorBox/data/testdata/img/'+str(i) + '.jpg'
imname = '/media/kirito/1T/procedure/TensorBox/data/testdata/result_'+ str(i) +'.jpg'
```
and modify evaluate_lift.py<br>
```
parser.add_argument('--iou_threshold', default=0.9, type=float)
parser.add_argument('--tau', default=0.1, type=float)
parser.add_argument('--min_conf', default=0.98, type=float)
parser.add_argument('--show_suppressed', default=False, type=bool)
```
if you want<br>

