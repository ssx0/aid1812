import pymysql

a = [
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (1, '﻿银色', 1);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (2, '星空灰', 2);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (3, '黑色', 3);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (4, '黑色', 4);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (5, '银白色', 5);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (6, '黑色', 6);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (7, '钛金灰', 7);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (8, '银色', 8);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (9, '玫瑰金', 9);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (10, '古典灰', 10);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (11, '黑色', 11);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (12, '玫瑰金', 12);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (13, '灰色', 13);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (14, '黑色', 14);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (15, '星空灰', 15);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (16, '黑色', 16);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (17, '钛金灰', 17);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (18, '冰雪蓝色', 18);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (19, '炫酷黑', 19);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (20, '黑色', 20);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (21, '铝框+银色', 21);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (22, '黑色', 22);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (23, '经典黑', 23);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (24, '蓝色', 24);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (25, '银色', 25);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (26, '星空灰', 26);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (27, '幻影黑', 27);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (28, '商务黑', 28);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (29, '奢华银', 29);",
"INSERT INTO `memberapp_goodscolor`(`id`, `color`, `goods_id`) VALUES (30, '经典黑', 30);",
]

conn = pymysql.connect(database='onlybuyp',user='root',password='123456',port=3306,host='127.0.0.1',use_unicode=True,charset='utf8')
cur = conn.cursor()
for i in a:
    cur.execute(i)
conn.commit()

cur.close()
conn.close()
