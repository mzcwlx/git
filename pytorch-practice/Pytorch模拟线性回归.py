import torch
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def create_dataset():
    x,y,coef=make_regression(n_samples=100, n_features=1, noise=10, coef=True, bias=14.5,random_state=99)
    x=torch.tensor(x)
    y=torch.tensor(y)
    print('真实的回归系数为：',coef)
    return x,y,coef

def show(x,y,coef,epochs,epoch_loss,model_weight):
    plt.scatter(x,y)
    x=torch.linspace(x.min(),x.max(),1000)
    y1=torch.tensor([v*coef+14.5 for v in x])
    plt.plot(x,y1,label='real',color='red')
    y2=torch.tensor([v*model_weight+14.5 for v in x])
    plt.plot(x,y2,label='pred',color='blue')
    plt.grid()
    plt.legend()
    plt.show()

    plt.plot(range(epochs),epoch_loss)
    plt.title('训练误差变化曲线')
    plt.grid()
    plt.show()

def train(x,y,coef):
    dataset=TensorDataset(x,y)
    dataloader=DataLoader(dataset,batch_size=16,shuffle=True)
    model=nn.Linear(in_features=1,out_features=1)
    criterion=nn.MSELoss()
    optimizer=optim.SGD(model.parameters(),lr=0.01)
    print('训练前模型的回归系数为：',model.weight.item())
    epochs=100
    epoch_loss=[]
    total_loss=0.0
    train_sample=0.0
    for epoch in range(epochs):
        for train_x,train_y in dataloader:
            y_pred=model(train_x.type(torch.float32))
            loss=criterion(y_pred,train_y.reshape(-1,1).type(torch.float32))
            total_loss+=loss.item()
            train_sample+=1
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        epoch_loss.append(total_loss/train_sample)
        print("第{}轮训练的平均误差为：{}".format(epoch+1,total_loss/train_sample))
    print('训练结束，模型的回归系数为：',model.weight.item())
    return epochs,epoch_loss,model.weight.item()


if __name__ == '__main__':
    x,y,coef = create_dataset()
    epochs, epoch_loss,model_weight = train(x,y,coef)
    show(x,y,coef,epochs,epoch_loss,model_weight)
