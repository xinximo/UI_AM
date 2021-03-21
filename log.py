# # -*- coding:utf-8 -*- #
# # @time 2021-03-11 20:06
# # author:pengda
# import datetime
# import logging
# import os
#
# project_path = os.path.dirname(__file__)
# # log_base_dir = project_path + r'/log'
# log_base_dir = os.path.join(project_path, 'log')
#
#
# cur = datetime.datetime.now()
# year = cur.year
# month = cur.month
# day = cur.day
# hour = cur.hour
# minute = cur.minute
# second = cur.second
# current_time = "{}{:0>2}{:0>2}{:0>2}{:0>2}{:0>2}".format(year, month, day, hour, minute, second)
# log_file = os.path.join(log_base_dir, current_time + '.log')
# logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
#                     filename=log_file,
#                     filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                                    # a是追加模式，默认如果不写的话，就是追加模式
#                     format='%(asctime)s - %(levelname)s: %(message)s')
