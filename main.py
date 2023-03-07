import Downloader
import Uploader
import Email

# channel_name = '@xiaodaodalang'
path = '/host/Youtube'
# pathname = '小岛大浪吹'

list_ = [{'@xiaodaodalang':'小岛大浪吹'},
         {'@wangzhian':'王局拍案'},
         {'@stone_ji':'Stone记'}]
text_ = []
for i in list_:
    channel_name = list(i.keys())[0]
    pathname = list(i.values())[0]
    # print(channel_name,pathname)
    download,filename = Downloader.Youtube_Downloader(channel_name,path).run()
    upload = Uploader.main(path,pathname)
    text_.append(Email.TextBody(download,filename,upload))

Email.send(text_)
