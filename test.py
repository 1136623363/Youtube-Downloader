import json

with open('videos.json','r') as fp:
    json_ = json.load(fp)

list_ = [i['filename'][:-3] for i in json_ if i['id'] == 'FMapyhp1qUY']
print(json_)
print(list_)