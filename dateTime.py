import time
import datetime


class TimeAPI():
    def __init__( self ):
        pass

    def getTime( self ):
        print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == "__main__":
    my_time = TimeAPI()
    TimeAPI.getTime( my_time )