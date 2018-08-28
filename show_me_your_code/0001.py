# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
code_list =[]
choice = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
i = 1
while i < 201:
   code = ''
   code_sample = random.sample(choice, 10)
   for j in code_sample:
      code += j
   code_list.append(code)   # 感谢<strong>a</strong>童鞋的提醒
   if code in code_list:
      print('code 已存在')