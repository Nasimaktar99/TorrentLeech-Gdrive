from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1421714631:AAEsZZ3IthCr-zfxOomUEp7uPdL0EebUB34"
    APP_ID = 2802833
    API_HASH = "2b5a05daf024b1e71a1df9975cb4dcb9"
    OWNER_ID =   1072308987
    AUTH_CHANNEL = [-1001475717966]
    DESTINATION_FOLDER = "Torrent leech" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken ={"access_token":"ya29.a0AfH6SMDftf3OMtOYrj1clYjMmpdh_oQ_4N-U7m4eSAXHSe5RzsIlKExMq5HE4IFsoxIHuInjIzyKfxejMfuhD_mdpyN5lXT6mkZsWGO5Xeg2gkYvczLP-QwBPMr5pCU8ncgj7C7Hsn41QOD5_-qbmiE0pXHXgRDPF6gW4n7q-Rw","refresh_token":"1//0dj1mOkxMrMrLCgYIARAAGA0SNwF-L9IrUIV1slXz49fBh_9CopzcoAmoHrRalqtTxow3SklX2DVfyK5HhDvz2pydfod7lJfXqEE","scope":"https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata.readonly","token_type":"Bearer","expiry_date":1607837338990}"""
#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
