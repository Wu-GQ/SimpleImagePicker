from urllib import request
import time
import random
import os

# 在线图片前缀
IMG_PREFIX_URL = 'http://analyse.kiiik.com:80/images/index/banner'
# 在线图片后缀
IMG_SUFFIX_URL = '.jpg'
# 图片开始序号
IMG_START_INDEX = 2
# 图片结束序号
IMG_END_INDEX = 2
# 图片序号最少长度
IMG_INDEX_MIN_LENGTH = 1

# 本地保存路径（相对路径）
SAVE_FOLDER_PATH = 'Secret/'
# 本地保存的图片名前缀
IMG_PREFIX_FILENAME = time.strftime("%Y%m%d%H%M%S_", time.localtime())


def confirm_save_folder():
    """ 确认文件夹路径 """
    if os.path.exists(SAVE_FOLDER_PATH):
        # 文件夹存在时，确认是否直接覆盖
        a = input(SAVE_FOLDER_PATH + ' 文件夹已存在，是否覆盖该文件夹内容(Y/N):')

        if a != 'Y' and a != 'y':
            print('已停止覆盖文件夹，请确认文件夹路径。')
            return bool(False)

        return bool(True)
    else:
        # 文件夹不存在时，确认是否创建
        a = input(SAVE_FOLDER_PATH + ' 文件夹不存在，是否需要创建该文件夹(Y/N):')

        if a == 'N' or a == 'n':
            print('新建文件夹失败，退出程序。')
            return bool(False)
        else:
            try:
                os.mkdir(SAVE_FOLDER_PATH)
                print('新建文件夹 ' + SAVE_FOLDER_PATH + ' 成功。')
            except Exception as e:
                print('新建文件夹失败，退出程序。')
                print(e)
                return bool(False)

        return bool(True)


def download_by_urlretrieve():
    """ 通过request.urlretrieve方式下载图片 """
    for i in range(IMG_START_INDEX, IMG_END_INDEX + 1):
        img_online_path = IMG_PREFIX_URL + str(i).zfill(IMG_INDEX_MIN_LENGTH) + IMG_SUFFIX_URL
        img_local_path = SAVE_FOLDER_PATH + IMG_PREFIX_FILENAME + str(i).zfill(IMG_INDEX_MIN_LENGTH) + IMG_SUFFIX_URL

        print(img_online_path + ' 开始下载……', end='\n\t')
        try:
            request.urlretrieve(img_online_path, img_local_path)
            print('下载完毕，保存位置: ' + img_local_path)
        except Exception as e:
            print('下载出错 ********')
            print(e)
        finally:
            time.sleep(random.uniform(2, 5))

    print('全部下载任务已完成.')


def download_by_urlopen():
    """ 通过request.urlopen方式下载图片 """
    for i in range(IMG_START_INDEX, IMG_END_INDEX + 1):
        img_online_path = IMG_PREFIX_URL + str(i).zfill(IMG_INDEX_MIN_LENGTH) + IMG_SUFFIX_URL
        img_local_path = SAVE_FOLDER_PATH + IMG_PREFIX_FILENAME + str(i).zfill(IMG_INDEX_MIN_LENGTH) + IMG_SUFFIX_URL

        print(img_online_path + ' 开始下载……', end='\n\t')
        with request.urlopen(img_online_path, timeout=30) as response, open(img_local_path, 'wb') as file_save:
            file_save.write(response.read())
            file_save.flush()
            file_save.close()
            print('下载完毕，保存位置: ' + img_local_path)
            time.sleep(random.uniform(2, 5))


if __name__ == '__main__':
    if confirm_save_folder():
        # download_by_urlretrieve()
        download_by_urlopen()
