import os
import shutil


class FolderClassifier:

    def __init__(self):
        # customized dictionary for type mapping
        self.folder_to_files = {'Audio': ['wav', 'mp3', 'raw', 'wma'],
                                'Video': ['mp4', 'm4a', 'm4v', 'f4v', 'f4a', 'm4b',
                                          'm4r', 'f4b', 'mov', 'avi', 'wmv', 'flv'],
                                'Image': ['jpeg', 'jpg', 'gif', 'bmp', 'svg', 'png'],
                                'Data': ['txt', 'xlsx', 'xls', 'zip'],
                                'Document': ['pdf', 'doc', 'docx', 'odt', 'html',
                                             'ppt', 'pptx', 'epub']}

        # name of the folder for other type of files
        self.other_folder = 'Others'
        self.folders = list(self.folder_to_files.keys()) + [self.other_folder]

    def create_folders(self, input_folder):
        """Help make directories based on mappings"""
        for folder in self.folders:
            folder = os.path.join(input_folder, folder)
            if not os.path.exists(folder):
                os.mkdir(folder)
                print(f'{folder} created')
            else:
                print(f'{folder} already exists')

    def classify(self, input_folder):
        """Classify and move files to the new filesystem"""

        print('Input directory is ', input_folder)

        self.create_folders(input_folder)

        for file in os.listdir(input_folder):

            # Do not touch unseen files (e.g. .DS_STORE)
            if file.startswith('.'):
                continue

            original_file_path = os.path.join(input_folder, file)

            # Do not touch existing directories
            if os.path.isdir(original_file_path) or file in self.folders:
                continue

            extension = file.split('.')[-1]

            moved_ind = 0
            for folder, ext_list in self.folder_to_files.items():
                folder = os.path.join(input_folder, folder)
                if extension in ext_list:
                    shutil.move(original_file_path, folder)
                    print(f'{file} MOVED TO {folder}.')
                    moved_ind = 1
                    break

            if not moved_ind:
                folder = os.path.join(input_folder, self.other_folder)
                shutil.move(original_file_path, folder)
                print(f'{file} MOVED TO {folder}')


if __name__ == '__main__':
    folder_path = '/Users/LinXIAO/Downloads'
    fc = FolderClassifier()
    fc.classify(folder_path)
    print('Done.')
