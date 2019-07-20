import requests
import json

# contain this city
def containTheCity( city_json, city_name ):
    for city in city_json:
        if city["locationName"] == city_name:
            return city
    raise NameError

def printInfo( city_info ):
    infomation = ""
    # POP
    infomation += "下雨機率: \n"
    infomation += city_info["weatherElement"][1]["time"][0]["parameter"]["parameterName"]
    infomation += "\n"
    # date ( start )
    infomation += "日期時間: \n"
    infomation += city_info["weatherElement"][2]["time"][0]["startTime"]
    infomation += " ~ "
    # date ( end )
    infomation += city_info["weatherElement"][2]["time"][0]["endTime"]
    infomation += "\n"
    # temperature min
    infomation += "溫度: \n"
    infomation += city_info["weatherElement"][2]["time"][0]["parameter"]["parameterName"]
    infomation += "°C ~ "
    # temperature max
    infomation += city_info["weatherElement"][4]["time"][0]["parameter"]["parameterName"]
    infomation += "°C"

    return infomation

# call weather api
def weather( city_name ):

    r1 = requests.get( "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-75773CF6-8ADD-46F3-B04F-690EE0A930DA" )
    r1.encoding='utf8'

    j = json.loads( r1.text )

    try:
        city_info = containTheCity( j["records"]["location"], city_name )
        print( "Yes" )
        return printInfo( city_info )
    except NameError:
        print( "無此城市" )
        return "無此城市"


if __name__ == "__main__":
    weather( "新北市" )