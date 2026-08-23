from sklearn.datasets import make_regression
import torch.nn as nn
import torch

model=nn.Sequential(
    nn.Linear(3,3),
    nn.LeakyReLU(),
    nn.Linear(3,2),
    nn.LeakyReLU(),
    nn.Linear(2,2),
)

nn.init.kaiming_normal_(model[0].weight)
nn.init.zeros_(model[0].bias)
nn.init.kaiming_normal_(model[2].weight)
nn.init.zeros_(model[2].bias)
nn.init.kaiming_normal_(model[4].weight)
nn.init.zeros_(model[4].bias)

X=torch.randn(100,3)
y1=2*X[:,0]+3*X[:,1]-X[:,2]+1 #2+6-3+1=6
y2=X[:,0]-2*X[:,1]+4*X[:,2]+2 #1-4+12+2=11
Y=torch.stack([y1,y2],dim=1)

criterion=nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(10001):
    prediction=model(X)
    loss=criterion(prediction,Y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch%100==0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")
model.eval()
with torch.no_grad():

    x=[1,2,3]
    pre=model(torch.tensor(x,dtype=torch.float32).reshape(1,3))
    print(pre)
