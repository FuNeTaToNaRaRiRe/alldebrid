import requests

class Alldebrid:
    def __init__(self):
        self.base = 'https://api.alldebrid.com/v4'
        self.agent = ''
        self.key = ''

    def user_infos(self):
        return requests.get(f'{self.base}/user?agent={self.agent}&apikey={self.key}').json()

    def link_infos(self, link, password=None):
        if password != None:
            return requests.get(f'{self.base}/link/infos?agent={self.agent}&apikey={self.key}&link[]={link}&password={password}').json()
        else:
            return requests.get(f'{self.base}/link/infos?agent={self.agent}&apikey={self.key}&link[]={link}').json()

    def download_link(self, link):
        return requests.get(f'{self.base}/link/unlock?agent={self.agent}&apikey={self.key}&link={link}').json()

    def streaming_link(self, linkid, streamid):
        return requests.get(f'{self.base}/link/streaming?agent={self.agent}&apikey={self.key}&id={linkid}&stream={streamid}').json()

    def upload_magnet(self, magnet):
        return requests.get(f'{self.base}/magnet/upload?agent={self.agent}&apikey={self.key}&magnets[]={magnet}').json()

    def upload_file(self, path):
        files = {
            'files[]': open(path, 'rb')
        }
        return requests.post(f'{self.base}/magnet/upload/file?agent={self.agent}&apikey={self.key}', files=files).json()

    def magnet_status(self, magnetid):
        return requests.post(f'{self.base}/magnet/status?agent={self.agent}&apikey={self.key}&id={magnetid}').json()

    def delete_magnet(self, magnetid):
        return requests.post(f'{self.base}/magnet/delete?agent={self.agent}&apikey={self.key}&id={magnetid}').json()

    def restart_magnet(self, magnetid):
        return requests.post(f'{self.base}/magnet/restart?agent={self.agent}&apikey={self.key}&id={magnetid}').json()
