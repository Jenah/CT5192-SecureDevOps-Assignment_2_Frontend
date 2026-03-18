from zapv2 import ZAPv2

target = 'http://localhost:3000'
zap = ZAPv2()
zap.urlopen(target)
zap.spider.scan(target)
zap.ascan.scan(target)
