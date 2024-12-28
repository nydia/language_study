import pymysql
from config.config_api import DashboardConfig
from utils.log_utils import LogUtils

class DbConnection:
    def __init__(self) -> None:
        pass
    def get_connection(self):
        try:
            _config = DashboardConfig().get_config()
            
            _conn = pymysql.connect(
                host=_config['database']['mysql']['host'],
                port=_config['database']['mysql']['port'],
                user=_config['database']['mysql']['username'], 
                passwd=_config['database']['mysql']['password'],
                db=_config['database']['mysql']['db'],
                charset=_config['database']['mysql']['charset'],
                cursorclass=pymysql.cursors.DictCursor
            )
            return _conn
        except:
            LogUtils().info("Error: unable to get connection")
        return None