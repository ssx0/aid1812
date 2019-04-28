#!/bin/bash

a=`pwd`
echo "正在将商品的类型导入数据库"
python3 $a/totype.py
echo "再次将商品的数据导入到数据库中"
python3 $a/tomembersgoods.py
echo '再次将颜色数据导入数据库中'
python3 $a/tocolors.py
echo '将所有的图片信息导入到数据库中'      
python3 $a/toimgs.py
echo '将所有的商品的规格信息导入数据库中'          
python3 $a/togoodsdetail.py
echo '将银行信息导入数据库中...'
python3 $a/tobanklist.py
echo "导入数据库成功!!!"

