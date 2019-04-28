import pymysql

a = [
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (1, '/goods/1686632', '/bigimgs/1', 1);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (2, '/goods/8811991', '/bigimgs/2', 2);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (3, '/goods/100001009067', '/bigimgs/3', 3);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (4, '/goods/1686651', '/bigimgs/4', 4);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (5, '/goods/5140554', '/bigimgs/5', 5);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (6, '/goods/100001826395', '/bigimgs/6', 6);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (7, '/goods/5717123', '/bigimgs/7', 7);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (8, '/goods/1496483833833', '/bigimgs/8', 8);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (9, '/goods/5068358', '/bigimgs/9', 9);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (10, '/goods/41148557411', '/bigimgs/10', 10);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (11, '/goods/980431', '/bigimgs/11', 11);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (12, '/goods/10536190598', '/bigimgs/12', 12);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (13, '/goods/2001495', '/bigimgs/13', 13);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (14, '/goods/5037172', '/bigimgs/14', 14);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (15, '/goods/8811995', '/bigimgs/15', 15);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (16, '/goods/1964546', '/bigimgs/16', 16);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (17, '/goods/6708133', '/bigimgs/17', 17);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (18, '/goods/100000972598', '/bigimgs/18', 18);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (19, '/goods/8484527', '/bigimgs/19', 19);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (20, '/goods/1000632', '/bigimgs/20', 20);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (21, '/goods/11251605629', '/bigimgs/21', 21);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (22, '/goods/1187770724', '/bigimgs/22', 22);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (23, '/goods/41709333859', '/bigimgs/23', 23);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (24, '/goods/42889099222', '/bigimgs/24', 24);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (25, '/goods/4442235', '/bigimgs/25', 25);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (26, '/goods/30394948309', '/bigimgs/26', 26);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (27, '/goods/8484501', '/bigimgs/27', 27);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (28, '/goods/7410797', '/bigimgs/28', 28);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (29, '/goods/3526440', '/bigimgs/29', 29);",
"INSERT INTO `memberapp_goodsimg`(`id`, `goodsimg`, `goodsimgbig`, `goods_id`) VALUES (30, '/goods/10634306339', '/bigimgs/30', 30);"
]

conn = pymysql.connect(database='onlybuyp',user='root',password='123456',port=3306,host='127.0.0.1',use_unicode=True,charset='utf8')
cur = conn.cursor()
for i in a:
    cur.execute(i)
    conn.commit()
cur.close()
conn.close()
