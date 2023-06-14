from enum import Enum


class Token(Enum):
    TOKEN = "OAuth y0_AgAAAAAwNSVLAAoKrgAAAADlZ8vm1l1GeQ61QjG_5TFSxnGP7Xqtvjo"


class Files(Enum):
    NEW_FOLDER_1 = "new_folder_1"
    FILE_FOR_COPY = "Файл для копирования.txt"
    NAME_COPY_FILE = "result.txt"
    DELETE_FILE = "new_folder_1%2FФайл для копирования.txt"


AUTH = {
    "Authorization": Token.TOKEN.value
}