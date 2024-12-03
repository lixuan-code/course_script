# @Time    : 2024/11/22 00:22
# @Author  : dhixuan
# @File    : python_course_09.py
# @Software: PyCharm
from typing import Union

products: list[list[Union[str, int]]] = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31],
                                         ["Book", 60], ["Nike", 699]]
content: int = int(input('请输入您的预算:'))
cost: int = 0

buyid_lst: list[int] = []
buy_product_lst: list[str] = []
money_lst: list[int] = []

while True:
    print(f"{'商品列表':-^15}")
    for i,item in enumerate(products):
        print(i, item[0], item[1])

    buy: str = input('请选择您要购买的商品编码:')

    if buy.isdigit():
        if products[int(buy)][1] > content:
            print("您的余额不足")
            continue
        else:
            buy_id: int = int(buy)
            buy_product: str = products[buy_id][0]
            cost += products[buy_id][1]
            print("已将{}放入购物车".format(buy_product))

            buyid_lst.append(buy_id)
            buy_product_lst.append(buy_product)
            money_lst.append(products[buy_id][1])
            content -= products[buy_id][1]

    if buy.upper() == 'Q':
        print(f"{'购物清单':-^15}")
        print('编码	   商品名称   单价   数量')
        for each in range(len(buyid_lst)):
            print(f"{buyid_lst[each]}     {buy_product_lst[each]}     {money_lst[each]}     1")
        print(f"-"*20)
        print(f"总计                   {cost}元")
        print(f"余额                   {content}元")
        print('谢谢惠顾')
        break
