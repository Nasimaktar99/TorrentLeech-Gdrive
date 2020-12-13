from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1413573058:AAGjU8CwLLuIr6nV_vaw7z3_A7SmdlvmCzs"
    APP_ID = 1373938
    API_HASH = "cbb279159c065dbb3ab1e3160b004518"
    OWNER_ID = 12537936
    AUTH_CHANNEL = [-10082786282972]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMCKWJVlEr2sfXpIQmiv1wv3vsIyAT9AszwrwqCqpJKvKpeoy3lZ1R2AGUH3SCrB5kxbxUxSbm_AnABtCXhUyOF7mshFiy5IQGjnIJadgbAeIodkuLuP3uzqVOosZ22HUfQmiMXM_tzptq_65LhEr8_reVmBB0HjGHvyCF4","refresh_token":"1//0dYiWpOwvPC5lCgYIARAAGA0SNwF-L9IrWBSpI-XCR3Kk-brXh95zwOr8IiQO6SyZY3ypZQ0ekXPz7RhQfWst__EqIh8pid8XvRE","scope":"https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata.readonly","token_type":"Bearer","expiry_date":1607798137208}
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
