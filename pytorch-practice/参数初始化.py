import torch.nn as nn


# 1.均匀分布随机初始化
def dm01():
    linear=nn.Linear(5,3)
    nn.init.uniform_(linear.weight )
    nn.init.uniform_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

#2.固定初始化
def dm02():
    linear=nn.Linear(5,3)
    nn.init.constant_(linear.weight,3)
    nn.init.constant_(linear.bias,3)
    print(linear.weight.data)
    print(linear.bias.data)

#3. 全0初始化
def dm03():
    linear=nn.Linear(5,3)
    nn.init.zeros_(linear.weight)
    nn.init.zeros_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

#4.全1初始化
def dm04():
    linear=nn.Linear(5,3)
    nn.init.ones_(linear.weight,3)
    nn.init.ones_(linear.bias,3)
    print(linear.weight.data)
    print(linear.bias.data)

#5.正态分布随机初始化
def dm05():
    linear=nn.Linear(5,3)
    nn.init.normal_(linear.weight)
    nn.init.normal_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

#6.kaiming初始化
def dm06():
    linear=nn.Linear(5,3)
    # nn.init.kaiming_normal_(linear.weight)
    # nn.init.kaiming_normal_(linear.bias)
    nn.init.kaiming_uniform_(linear.weight)
    nn.init.zeros_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)


#7.xavier初始化
def dm07():
    linear=nn.Linear(5,3)
    # nn.init.xavier_normal_(linear.weight)
    # nn.init.xavier_normal_(linear.bias)
    nn.init.kaiming_uniform_(linear.weight)
    nn.init.zeros_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    # dm04()
    # dm05()
    # dm06()
    dm07()