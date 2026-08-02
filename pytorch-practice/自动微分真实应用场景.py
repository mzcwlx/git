import torch

torch.manual_seed(99)
x=torch.ones(2,5)
y=torch.zeros(2,3)
w=torch.randn(5,3,requires_grad=True)
b=torch.randn(3,requires_grad=True)
z=torch.matmul(x,w)+b
# z=x@w+b
criterion=torch.nn.MSELoss()
for i in range(100):
    loss=criterion(z,y)
    loss.backward()
    w.data-=0.01*w.grad
    b.data-=0.01*b.grad
    print("第",i+1,"次迭代 权重为:",w,"偏置为:",b,"loss为:",loss)
    if (w.grad is not None) and (b.grad is not None):
        w.grad.zero_()
        b.grad.zero_()
    z=torch.matmul(x,w)+b
print(f"最终结果为 权重：{w}\n偏置:{b}\nloss:{loss}")
