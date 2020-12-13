from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1421714631:AAEsZZ3IthCr-zfxOomUEp7uPdL0EebUB34"
    APP_ID =   2802833
    API_HASH = "2b5a05daf024b1e71a1df9975cb4dcb9"
    OWNER_ID =  1072308987
    AUTH_CHANNEL = [-1001475717966]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMCKWJVlEr2sfXpIQmiv1wv3vsIyAT9AszwrwqCqpJKvKpeoy3lZ1R2AGUH3SCrB5kxbxUxSbm_AnABtCXhUyOF7mshFiy5IQGjnIJadgbAeIodkuLuP3uzqVOosZ22HUfQmiMXM_tzptq_65LhEr8_reVmBB0HjGHvyCF4","refresh_token":"1//0dYiWpOwvPC5lCgYIARAAGA0SNwF-L9IrWBSpI-XCR3Kk-brXh95zwOr8IiQO6SyZY3ypZQ0ekXPz7RhQfWst__EqIh8pid8XvRE","scope":"https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata.readonly","token_type":"Bearer","expiry_date":1607798137208}
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
