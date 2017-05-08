## HW2 ##

-	張培堯 7105056035
-	2017/5/8
-	[題目](https://drive.google.com/file/d/0B8_tOdBna60vSW41emMxcC1ETEk/view?usp=sharing)

### 執行方式 ###


1. 	將7topo_info.py放置ryu/ryu/app路徑下
2. 	開啟一個終端機，輸入`sudo mn --topo=tree,3 --switch=ovsk,protocols=OpenFlow13 --controller=remote`
3.	開啟另一個終端機，輸入`ryu-manager --observe-links topo_info.py` 就會顯示結果

