keys = ['apple','banana','cherry']
values = [170,150,300]
d = {}

for k,v in zip(keys,values):
  d.update({k:v})
print(f'作成したリスト:{d}')