import time

recent_time = time.time()

passed_days = recent_time // (3600*24)
passed_hours = recent_time % (3600*24) // 3600
passed_minutes = recent_time % 3600 // 60
passed_seconds = recent_time % 60

print('距离纪元已经过去了%d天,%d小时,%d分钟,%f秒'
      % (passed_days, passed_hours,
         passed_minutes, passed_seconds))
