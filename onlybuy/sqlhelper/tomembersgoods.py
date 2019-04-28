import pymysql

a = [
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (1, '梵地亚（Vantiiear）万向轮拉杆箱耐磨抗摔24英寸旅行箱男女行李箱登机箱 银色', 186.00, '梵地亚（Vantiiear）万向轮拉杆箱耐磨抗摔24英寸旅行箱男女行李箱登机箱 银色', 1, 1, '/goods/1686632');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (2, '小米（MI）90分旅行箱拉杆箱1A 男女万向轮登机行李箱 20英寸 星空灰', 299.00, '小米（MI）90分旅行箱拉杆箱1A 男女万向轮登机行李箱 20英寸 星空灰', 1, 1, '/goods/8811991');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (3, '【京选尚品】地平线8号（LEVEL8）行李箱旅行箱登机箱20英寸德国拜耳PC箱体拉杆箱 黑色（锤科出品）', 299.00, '【京选尚品】地平线8号（LEVEL8）行李箱旅行箱登机箱20英寸德国拜耳PC箱体拉杆箱 黑色（锤科出品）', 1, 1, '/goods/100001009067');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (4, '梵地亚（Vantiiear）拉杆箱万向轮耐磨抗摔行李箱20英寸旅行箱男女登机箱 黑色升级版', 169.00, '梵地亚（Vantiiear）拉杆箱万向轮耐磨抗摔行李箱20英寸旅行箱男女登机箱 黑色升级版', 1, 1, '/goods/1686651');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (5, '博兿（BOYI）行李箱24英寸万向轮拉杆箱 男女防刮耐磨密码静音旅行箱子 BY-72002银白色', 186.00, '博兿（BOYI）行李箱24英寸万向轮拉杆箱 男女防刮耐磨密码静音旅行箱子 BY-72002银白色', 1, 1, '/goods/5140554');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (6, '【京选尚品】（锤科出品）地平线8号（LEVEL8）行李箱旅行箱托运箱24英寸德国拜耳PC箱体拉杆箱黑色', 399.00, '【京选尚品】（锤科出品）地平线8号（LEVEL8）行李箱旅行箱托运箱24英寸德国拜耳PC箱体拉杆箱黑色', 1, 1, '/goods/100001826395');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (7, '小米（MI）米家90分轻商务旅行箱拉杆箱 男女万向轮登机行李箱 钛金灰 20英寸 前开盖 双密码锁', 399.00, '小米（MI）米家90分轻商务旅行箱拉杆箱 男女万向轮登机行李箱 钛金灰 20英寸 前开盖 双密码锁', 1, 1, '/goods/5717123');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (8, '【防盗合金铝框】意酷拉杆箱万向轮行李箱男女小登机箱大号旅行箱20寸24寸26寸28寸密码箱学生皮箱子 海关锁款-银色（热卖款 男女士都适合） 20英寸-登机箱-商务手提上飞机手拉箱 领劵立减', 238.00, '【防盗合金铝框】意酷拉杆箱万向轮行李箱男女小登机箱大号旅行箱20寸24寸26寸28寸密码箱学生皮箱子 海关锁款-银色（热卖款 男女士都适合） 20英寸-登机箱-商务手提上飞机手拉箱 领劵立减', 1, 1, '/goods/1496483833833');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (9, '斯高高尔夫（SCOGOLF）拉杆箱20英寸行李箱女 旅行箱登机箱万向轮6689玫瑰金', 152.00, '斯高高尔夫（SCOGOLF）拉杆箱20英寸行李箱女 旅行箱登机箱万向轮6689玫瑰金', 1, 1, '/goods/5068358');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (10, '拉杆箱铝框行李箱男女旅行箱新品20寸登机箱万向轮密码箱 古典灰 24寸/需托运', 549.00, '拉杆箱铝框行李箱男女旅行箱新品20寸登机箱万向轮密码箱 古典灰 24寸/需托运', 1, 1, '/goods/41148557411');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (11, '瑞动（SWISSMOBILITY）拉杆箱24英寸旅行箱 大容量行李箱轻盈静音万向轮男女 5555黑色', 299.00, '瑞动（SWISSMOBILITY）拉杆箱24英寸旅行箱 大容量行李箱轻盈静音万向轮男女 5555黑色', 1, 1, '/goods/980431');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (12, '【防刮型】吉鲁宾528拉杆箱 旅行箱行李箱男士女士登机箱20/24/26/29英寸箱包万向轮 玫瑰金 20英寸 登机箱', 208.00, '【防刮型】吉鲁宾528拉杆箱 旅行箱行李箱男士女士登机箱20/24/26/29英寸箱包万向轮 玫瑰金 20英寸 登机箱', 1, 1, '/goods/10536190598');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (13, '爱华仕（OIWAS）飞机轮密码锁拉杆箱6182 商务出差旅行箱 行李箱男女登机箱20英寸灰色', 369.00, '爱华仕（OIWAS）飞机轮密码锁拉杆箱6182 商务出差旅行箱 行李箱男女登机箱20英寸灰色', 1, 1, '/goods/2001495');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (14, 'ALLANT拉杆箱万向轮 24英寸行李箱男旅行箱 ABS时尚轻盈 AL-8503 黑色', 186.00, 'ALLANT拉杆箱万向轮 24英寸行李箱男旅行箱 ABS时尚轻盈 AL-8503 黑色', 1, 1, '/goods/5037172');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (15, '小米（MI）90分旅行箱拉杆箱1A 男女万向轮行李箱 26英寸 星空灰', 449.00, '小米（MI）90分旅行箱拉杆箱1A 男女万向轮行李箱 26英寸 星空灰', 1, 1, '/goods/8811995');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (16, '瑞士军刀威戈（Wenger）拉杆箱 男女商务休闲ABS22英寸万向轮行李箱旅行箱 黑色 SAX631115109058', 199.00, '瑞士军刀威戈（Wenger）拉杆箱 男女商务休闲ABS22英寸万向轮行李箱旅行箱 黑色 SAX631115109058', 1, 1, '/goods/1964546');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (17, '90分拉杆箱24英寸 德国拜尔PC材质静音万向轮行李箱 商旅两用旅行箱 钛金灰', 449.00, '90分拉杆箱24英寸 德国拜尔PC材质静音万向轮行李箱 商旅两用旅行箱 钛金灰', 1, 1, '/goods/6708133');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (18, '迪士尼（Disney）儿童拉杆箱18英寸小学生行李箱 公主登机箱万向轮旅行箱 TFD0003-B18冰雪蓝色', 398.00, '迪士尼（Disney）儿童拉杆箱18英寸小学生行李箱 公主登机箱万向轮旅行箱 TFD0003-B18冰雪蓝色', 1, 1, '/goods/100000972598');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (19, '卡帝乐鳄鱼(CARTELO) 耐磨防刮24英寸拉杆箱万向轮旅行李箱男女学生密码箱时尚轻盈商务休闲行李箱包 炫酷黑', 159.00, '卡帝乐鳄鱼(CARTELO) 耐磨防刮24英寸拉杆箱万向轮旅行李箱男女学生密码箱时尚轻盈商务休闲行李箱包 炫酷黑', 1, 1, '/goods/8484527');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (20, '瑞动（SWISSMOBILITY）拉杆箱30英寸差旅大容量行李箱 防泼水静音万向轮旅行箱男女 5560黑色', 329.00, '瑞动（SWISSMOBILITY）拉杆箱30英寸差旅大容量行李箱 防泼水静音万向轮旅行箱男女 5560黑色', 1, 1, '/goods/1000632');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (21, '【防刮伤】【高品质】 铝框拉杆箱万向轮行李箱男士女士旅行箱20/24/26/29英寸登机箱 高端 铝框+银色 20英寸 登机箱', 258.00, '【防刮伤】【高品质】 铝框拉杆箱万向轮行李箱男士女士旅行箱20/24/26/29英寸登机箱 高端 铝框+银色 20英寸 登机箱', 1, 1, '/goods/11251605629');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (22, '蒙特布朗 铝框拉杆箱防刮旅行箱20/24/28英寸行李箱 黑色 20英寸可登机', 368.00, '蒙特布朗 铝框拉杆箱防刮旅行箱20/24/28英寸行李箱 黑色 20英寸可登机', 1, 1, '/goods/1187770724');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (23, '旅行大师 新品18英寸拉杆箱女万向轮登机箱轻便小型行李箱男纯PC迷你旅行箱包韩版飞机密码箱子 经典黑 18英寸', 469.00, '旅行大师 新品18英寸拉杆箱女万向轮登机箱轻便小型行李箱男纯PC迷你旅行箱包韩版飞机密码箱子 经典黑 18英寸', 1, 1, '/goods/41709333859');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (24, '七匹狼行李箱男拉杆箱旅行箱万向轮女24寸密码箱20寸登机箱箱子潮 蓝色 20英寸【官方直营·收藏加购优先发货】', 229.00, '七匹狼行李箱男拉杆箱旅行箱万向轮女24寸密码箱20寸登机箱箱子潮 蓝色 20英寸【官方直营·收藏加购优先发货】', 1, 1, '/goods/42889099222');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (25, '维多利亚旅行者（VICTORIATOURIST）拉杆箱PC+ABS商务旅行箱行李箱男 24英寸万向轮海关锁5518银色', 248.00, '维多利亚旅行者（VICTORIATOURIST）拉杆箱PC+ABS商务旅行箱行李箱男 24英寸万向轮海关锁5518银色', 1, 1, '/goods/4442235');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (26, '小米（MI）90分旅行箱拉杆箱 男女万向托运旅行皮箱24英寸轻巧便利出差旅游行李箱 星空灰-24英寸', 349.00, '小米（MI）90分旅行箱拉杆箱 男女万向托运旅行皮箱24英寸轻巧便利出差旅游行李箱 星空灰-24英寸', 1, 1, '/goods/30394948309');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (27, '卡帝乐鳄鱼(CARTELO) 拉杆箱 万向轮旅行箱 20英寸登机箱行李箱密码箱子 幻影黑', 169.00, '卡帝乐鳄鱼(CARTELO) 拉杆箱 万向轮旅行箱 20英寸登机箱行李箱密码箱子 幻影黑', 1, 1, '/goods/8484501');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (28, '稻草人(MEXICAN)行李箱男女 24英寸大容量拉杆箱 德国拜耳PC材质万向轮静音海关密码锁旅行箱 商务黑', 359.00, '稻草人(MEXICAN)行李箱男女 24英寸大容量拉杆箱 德国拜耳PC材质万向轮静音海关密码锁旅行箱 商务黑', 1, 1, '/goods/7410797');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (29, '瑞动（SWISSMOBILITY）铝框拉杆箱24英寸密码锁行李箱 复古旅行箱静音万向飞机轮男女 5083奢华银', 499.00, '瑞动（SWISSMOBILITY）铝框拉杆箱24英寸密码锁行李箱 复古旅行箱静音万向飞机轮男女 5083奢华银', 1, 1, '/goods/3526440');",
"INSERT INTO `memberapp_goods`(`id`, `title`, `price`, `desc`, `isDelete`, `type_id`, `listimg`) VALUES (30, '【铝框防刮款】纯奢行李箱拉杆箱男铝框万向轮旅行箱学生密码箱女20/24/26/29英寸 经典黑 20英寸-登机箱', 238.00, '【铝框防刮款】纯奢行李箱拉杆箱男铝框万向轮旅行箱学生密码箱女20/24/26/29英寸 经典黑 20英寸-登机箱', 1, 1, '/goods/10634306339');",
]
conn = pymysql.connect(database='onlybuyp',user='root',password='123456',port=3306,host='localhost',use_unicode=True,charset='utf8')
cur = conn.cursor()
for i in a:
    cur.execute(i)
conn.commit()

cur.close()
conn.close()
