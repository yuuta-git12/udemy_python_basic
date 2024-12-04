# 辞書型のfor文処理

fruits = {'1':'apple','2':'banana','3':'strawberry'}
for k,v in fruits.items():
    print("{}:{}".format(k,v))

# リストのインデックスを取り出す処理
for i, fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)

# zip関数を使ったリスト内の処理
# 要素数が同じ部分まで処理してくれる
days = ['Mon','Tue','Wed','THU']
fruits2 = ['apple','banana','orange','Strawberry']
drinks = ['coffee','tea','beer']

for day,fruit,drink in zip(days,fruits2,drinks):
    print(day,fruit,drink)