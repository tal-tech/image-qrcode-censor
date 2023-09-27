# 问题背景
视频中二维码突破需要进行遮蔽


# 解决方案
1.使用pyzbar检测当前帧是否有二维码
2.一个视频全部二维码信息用l_detect_qr_zone存放，存放位置和灰度图区域矩阵
3.1每间隔10帧进行检测是否有二维码
3.2每间隔150帧，进行一次批处理
  对150中每一帧np_frame_tocheck，遍历l_detect_qr_zone中 [x0:x1,y0:y1], np_frame_qr
  计算np_frame_tocheck[x0:x1,y0:y1] 和 np_frame_qr 结构体相似度ssim
  ssim>=0.95, 若是则认为当前帧对应区域有二维码


# 环境
详细见requirements.txt
ffmpeg-linux64-v4.1

# 训练命令
无

# 测试命令
将一个视频中二维码遮蔽
```
python test.py
```


# 是否有模型
无


# 目前精度
尚不能100%遮蔽，部分视频某些片段出现未遮挡情况


# 回流数据
未上线, 未作数据回流

# 日志说明
未上线, 未作日志

# 线上相关机器
未上线, 未分配线上机器