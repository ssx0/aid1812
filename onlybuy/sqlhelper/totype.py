# -*- encoding:utf-8 -*-

import pymysql

a =[
"INSERT INTO `goods_type`(`id`, `title`, `desc`, `isDelete`) VALUES (1, '拉杆箱', '最美拉杆箱', 1);",
"INSERT INTO `goods_type`(`id`, `title`, `desc`, `isDelete`) VALUES (2, '手提包', '最美手提包', 1);",
"INSERT INTO `goods_type`(`id`, `title`, `desc`, `isDelete`) VALUES (3, '背包', '最美背包', 1);",
]
conn = pymysql.connect(database='onlybuyp',user='root',port=3306,host='127.0.0.1',password='123456',use_unicode=True,charset='utf8')
cur = conn.cursor()

for i in a:
    cur.execute(i)
    conn.commit()

cur.close()
conn.close()
