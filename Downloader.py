import subprocess
import json
import os

class Youtube_Downloader():
    def __init__(self,channel_name,path):
        # 请将 CHANNEL_NAME 替换为您要下载视频的博主的用户名
        self.channel_name = channel_name#"@wangzhian"
        self.path = path
        self.flag = 0   #0原始状态，1下载成功，2没有更新，-1下载失败
        self.filename = ['']

    def getId(self):
        # 运行 yt-dlp 命令获取最新视频列表
        command = f'yt-dlp --dateafter now-7days "https://www.youtube.com/{self.channel_name}/videos" --flat-playlist -j'
        output = subprocess.check_output(command, shell=True)

        # 解析 JSON 输出以获取最新视频 URL
        self.videos = []
        for line in output.decode().strip().split("\n"):
            video = json.loads(line)
            self.videos.append(video)
        print(self.videos)
        # print(videos)
        # with open('videos.json', 'w') as f:
        #     json.dump(self.videos, f)

        self.video_id = [i['id'] for i in self.videos]


    # 下载最新视频
    def download(self,video_to_download):
        for i in video_to_download:
            video_url = "https://www.youtube.com/watch?v="+i
            command = f'yt-dlp -o "{self.path}/%(title)s.%(ext)s" -f best {video_url}'
            subprocess.run(command, shell=True)
            self.filename = [j['filename'][:-3] for j in self.videos if i == j['id']]


    def main(self):
        json_name = self.channel_name+'-Playlist.json'
        if os.path.exists(json_name) == True:       #判断video_id_former是否存在
            with open(self.path+'/'+json_name, 'r') as fr:
                video_id_former = json.load(fr)
            # print(video_id_former)
            video_to_download = [i for i in self.video_id if i not in video_id_former]

            if len(video_to_download) == 0:
                self.flag = 2 #没有更新
            else:
                with open(self.path+'/'+json_name, 'w') as fw:
                    json.dump(self.video_id, fw)
                self.download(video_to_download)
                self.flag = 1
        else:
            with open(self.path+'/'+json_name, 'w') as fw:
                json.dump(self.video_id, fw)
            video_to_download = [self.video_id[0]]
            self.download(video_to_download)
            self.flag = 1

    def run(self):
        self.getId()
        try:
            self.main()
        except:
            self.flag = -1
        return self.flag,self.filename

# print(Youtube_Downloader('@xiaodaodalang','D://Desktop').run())
