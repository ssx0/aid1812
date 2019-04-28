import pymysql

a = [
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (1, '#20英寸#24英寸#26英寸#28英寸', 10, 1);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (2, '#20英寸', 78, 2);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (3, '#20英寸', 29, 3);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (4, '#20英寸#24英寸#26英寸#28英寸', 41, 4);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (5, '#20英寸#24英寸#28英寸', 89, 5);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (6, '#24英寸', 62, 6);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (7, '#20英寸', 13, 7);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (8, '#20英寸#24英寸#29英寸#26英寸', 46, 8);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (9, '#20英寸#24英寸#28英寸', 61, 9);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (10, '#20寸#24寸#26寸#29寸', 10, 10);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (11, '#24英寸#20英寸#25英寸', 55, 11);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (12, '#20英寸#29英寸#26英寸', 63, 12);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (13, '#19寸#20寸#24寸#28寸', 36, 13);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (14, '#24英寸', 86, 14);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (15, '#26英寸', 97, 15);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (16, '#22英寸#24英寸', 14, 16);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (17, '#20英寸#24英寸#28英寸', 40, 17);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (18, '#18英寸', 93, 18);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (19, '#24英寸', 20, 19);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (20, '#30英寸', 95, 20);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (21, '#20英寸#24英寸#26英寸#29英寸', 92, 21);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (22, '#20英寸#22英寸#24英寸#26英寸#28英寸', 56, 22);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (23, '#18英寸', 12, 23);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (24, '#20英寸#26英寸', 71, 24);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (25, '#20英寸#24英寸#28英寸', 37, 25);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (26, '#24英寸', 47, 26);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (27, '#20英寸', 88, 27);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (28, '#20英寸#24英寸#28英寸', 73, 28);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (29, '#24英寸#20英寸#28英寸#20+28英寸', 14, 29);",
"INSERT INTO `memberapp_goodsdetail`(`id`, `specifice`, `stock`, `goods_id`) VALUES (30, '#20英寸#24英寸#26英寸#29英寸', 68, 30);",
]

conn = pymysql.connect(database='onlybuyp',user='root',password='123456',port=3306,host='127.0.0.1',use_unicode=True,charset='utf8')
cur = conn.cursor()
for i in a:
    cur.execute(i)
    conn.commit()
cur.close()
conn.close()
