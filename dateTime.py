import time
from datetime import datetime
import pytz


class TimeAPI():
    def __init__( self ):
        pass

    def getTime( self ):
        tw = pytz.timezone( "Asia/Taipei" )
        print( datetime.now( tw ).strftime( "%Y-%m-%d %H:%M:%S" ) )
        return datetime.now( tw ).strftime( "%Y-%m-%d %H:%M:%S" )
        

if __name__ == "__main__":
    my_time = TimeAPI()
    TimeAPI.getTime( my_time )