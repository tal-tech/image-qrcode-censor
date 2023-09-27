from video_block_qr_zone import *
import os

if __name__ == "__main__":
    '''
    video_block.get_qr(img): detect qrcode of a image
    video_block.cover_img(img, tpl, res[1]): cover an image with logo image
    '''
    video_block = VideoBlock()
    img = cv2.imread('./image.jpeg')
    res = video_block.get_qr(img)
    print('qr position: ',res)
    tpl = cv2.imread('./mask_image.jpeg')
    for i in range(1000):
        _, img = video_block.cover_img(img, tpl, res[1])
    cv2.imwrite('./res.jpg', img)