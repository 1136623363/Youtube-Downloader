import requests
import os
from urllib.parse import quote
from requests_toolbelt import MultipartEncoder
import NameCheck

def upload(path, pathname, filename):
    m = MultipartEncoder(
        fields={
            'file': (filename, open(path + '/' + filename, 'rb'))
        }
    )
    new_filename = NameCheck.namecheck(filename)
    file = quote(pathname + '/' + new_filename, 'utf-8')
    # print(file)
    headers = {
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjExMzY2MjMzNjMiLCJleHAiOjE2NzgyODQ0NzQsIm5iZiI6MTY3ODExMTY3NCwiaWF0IjoxNjc4MTExNjc0fQ.IaaDSu-fIUG7RQNUDs_HH6K7VmUu0Lot5Z8OCYMNong',
        'Content-Type': m.content_type,
        # 'Content-Length':'',
        'file-path': f'/Youtube/{file}'
    }

    res = requests.put(url="http://192.168.31.183:5244/api/fs/form", data=m, headers=headers)
    print(res.text)

    return res.status_code


def main(path, pathname):
    filename_list = [i for i in os.listdir(path)]
    filename_list_to_upload = [i for i in filename_list if i[-3:] == 'mp4']

    for i in filename_list_to_upload:
        flag = upload(path, pathname, i)
        if flag == 200:
            os.remove(path + '/' + i)
        return flag

        # try:
        #     upload(path, pathname,i)
        #     return 0
        # except:
        #     return 1

# path = '/host/王志安'
# pathname = '王局'
# main(path,pathname)