import glob
import cv2
import os
import subprocess

failed = 0

for extension in ['png', 'jpg', 'jpeg']:
    for filename in glob.glob('/Applications/XAMPP/xamppfiles/htdocs/vio/wp-content/uploads/**/*.' + extension, recursive=True):
        try:
            filename_without_extension = filename.split('/')[-1].split('.')[0]
            img = cv2.imread(filename, cv2.IMREAD_COLOR)
            cv2.imwrite(filename, img)
            
            quality = 80
            command = 'cwebp -metadata all -exact -q {} {} -o {}.webp'.format(
            quality, filename, filename_without_extension)
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

            folders_full = filename[len('/Applications/XAMPP/xamppfiles/htdocs/vio/wp-content/uploads/'):]
            folders = folders_full.split("/")
            folder_path = 'Poze_webp'

            for folder in folders[0: len(folders) - 1]:
                folder_path += "/" + folder
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

            new_path = 'Poze_webp/' + folders[0] + '/' + folders[1] + '/' + filename_without_extension + '.webp'
            
            os.rename(filename_without_extension + '.webp', new_path)
        except:
            failed += 1
            continue

print("Finished!\n")
print("Failed = " + str(failed))