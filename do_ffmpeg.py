import os

ini_folder = './tencent_data/'
for i in range(0, 6):
    try:
        foldername = ini_folder + str(i) + '_upload/1_Video/'
        filename = foldername + str(i) + '.mp4'
        save_name = ini_folder + str(i) + '_upload/2_Audio/'
        cmd = 'ffmpeg -i ' + filename + \
            ' -vn -acodec copy ' + save_name + str(i) + '.m4a'
        os.system(cmd)
    except Exception as err:
        print(err)
