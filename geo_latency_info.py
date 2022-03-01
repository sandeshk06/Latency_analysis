#!/usr/bin/python3
from scapy.all import *
import requests
import ipaddress
import logging

class GeoTrace:
    

    def __init__(self,site):
        
        self.site=site
          


    def find_source_public_ip(self,):
        try:
        
            SOURCE_IP=()
            resp=requests.get('https://api.ipify.org')
            if resp.status_code==200:
                IP=resp.text
                response=requests.get('http://ip-api.com/json/'+str(IP))
                if response.status_code == 200:
                    data=response.json()
                    latitude=data['lat']
                    longitude=data['lon']
                    SOURCE_IP=(latitude,longitude)

            return SOURCE_IP
        except Exception as e:

            SOURCE_IP=()
            return SOURCE_IP


    def find_geo_location(self,HOP_WISE_RESULT):
        try:
            GEO_LOCATION={} 
            for hop,ip in sorted(HOP_WISE_RESULT.items()):
        
                if ipaddress.ip_address(ip).is_private:
                    #print("Private:{}".format(ip))
                    pass
                else:
                    IP=ip
                    response=requests.get('http://ip-api.com/json/'+str(IP))
                    if response.status_code == 200:
                        data=response.json()
                        TEMP=[]
                        latitude=data['lat']
                        longitude=data['lon']
                        TEMP.append(latitude)
                        TEMP.append(longitude)
                        GEO_LOCATION[hop]=TEMP
                        #print("IP:{},lat:{},long:{}".format(IP,latitude,longitude))
            
            return GEO_LOCATION


        except Exception as e:
            print(e)
            #GEO_LOCATION={}
            return GEO_LOCATION


    def get_geo_traceroute_data(self,):
        GEO_LOCATION={}
        SOURCE_IP=()
        HOP_WISE_RESULT={}
        try:
        
            SOURCE_IP=self.find_source_public_ip()        
            ans,unans=traceroute(target=[self.site],maxttl=30,verbose=0)

             
            if ans.get_trace():
                for key,value in ans.get_trace().items():
                    for hop,ip in value.items():
                        #print(hop,ip[0])
                        HOP_WISE_RESULT[hop]=ip[0]

                if HOP_WISE_RESULT:
            
                    GEO_LOCATION=self.find_geo_location(HOP_WISE_RESULT)
            

            return SOURCE_IP,GEO_LOCATION
   
        except Exception as e:
            logging.error("error while performing geo trace:{}".format(e))
            return SOURCE_IP,GEO_LOCATION

    
