import torch

w=torch.tensor(10,requires_grad=True,dtype=torch.float32)

loss=w**2+20
print("开始 权重初始值为:",w,"loss初始值为:",loss)

for i in range(100):
    loss=w**2+20
    if w.grad is not None:
        w.grad.zero_()
    loss.backward()
    print("第",i+1,"次迭代 权重为:",w,"loss为:",loss)
    w.data-=0.01*w.grad
    loss=w**2+20

print(f"最终结果为 权重：{w},梯度:{w.grad},loss:{loss}")