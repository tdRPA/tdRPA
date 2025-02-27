'''
tdworker的命令参数,如:
    searchDelay: int = 10000,
    delayAfter: int = 100,
    delayBefore: int = 100,
都是通过time.sleep()实现的，所以可以通过重载time.sleep函数，让流程整体放慢速度，就像开启了慢镜头一样。
本人(有闲王员外)录制演示视频的时候，常常用这个功能，以便大家能看清每个操作步骤，还能一边演示一边讲解。
'''

import time

_sleep=time.sleep

def sleep(i):
    _sleep(i*2) #调慢一半的速度

time.sleep=sleep