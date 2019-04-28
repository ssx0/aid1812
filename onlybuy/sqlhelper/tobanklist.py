import pymysql

a =[
"INSERT INTO `pay_banklist`(`id`, `bank`, `bankimg`) VALUES (1, '工商银行','banklist/gongshang.jpeg');",
"INSERT INTO `pay_banklist`(`id`, `bank`, `bankimg`) VALUES (2, '建设银行','banklist/jianshe.jpeg');",
"INSERT INTO `pay_banklist`(`id`, `bank`, `bankimg`) VALUES (3, '农业银行','banklist/nongye.jpeg');",
"INSERT INTO `pay_banklist`(`id`, `bank`, `bankimg`) VALUES (4, '招商银行','banklist/zhaoshang.jpeg');",
"INSERT INTO `pay_banklist`(`id`, `bank`, `bankimg`) VALUES (5, '中国银行','banklist/zhongguo.jpeg');",
]
conn = pymysql.connect(database='onlybuyp',user='root',port=3306,host='127.0.0.1',password='123456',use_unicode=True,charset='utf8')
cur = conn.cursor()

for i in a:
    cur.execute(i)
    conn.commit()

cur.close()
conn.close()
