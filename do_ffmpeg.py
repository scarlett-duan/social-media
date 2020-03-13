import os

ini_folder = './weibo_data/data_1/'
for i in range(1, 6):
    try:
        foldername = ini_folder + str(i) + '_upload/1_video/'
        filename = foldername + str(i)  # + '.mp4'
        save_name = ini_folder + str(i) + '_upload/2_audio/'
        cmd = 'ffmpeg -vn -y -acodec copy ' + \
            save_name + ' -i ' + filename + str(i) + '.m4a'
        os.system(cmd)
    except Exception as err:
        print(err)
