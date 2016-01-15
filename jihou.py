#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,datetime,sys

youbi = ["月","火","水","木","金","土","日"]

exe_yukkuri = '/opt/aquestalkpi/AquesTalkPi'

d = datetime.datetime.today()

#sound = '/var/tmp/myraspi/sound/ハクション大魔王の歌.mp3'

if d.hour < 12 :
    hour = "午前" + str(d.hour) + "時"
elif d.hour == 12 : 
    hour = "正午" 
else :
    hour = "午後" + str(d.hour - 12) + "時" 

if d.minute == 0 :
    min = 'ちょうど'
elif d.minute == 30 :
    min = '半'
else :
    min = '%s分' % (d.minute)

jihou_str = 'ゆっくりが %s月%s日%s曜日 %s%sをおしらせします' % (d.month, d.day, youbi[d.weekday()], hour, min)

cmd_now = '%s \"%s\" | aplay' % (exe_yukkuri, jihou_str)
cmd_wakeup = '%s \"ポーーーーーン\" | aplay' % (exe_yukkuri)

print cmd_now
print cmd_wakeup

os.system(cmd_now)
os.system(cmd_wakeup)

sys.exit(0)
