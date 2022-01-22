#!/usr/bin/python3
import logging
import pycurl
import json
from io import BytesIO
import os
import subprocess
import sys

def compute(url):
    try:
        
        buffer = BytesIO()
        url=url
        #payload=str(data[0])
        #payload=json.dumps(data[0])
        
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        #c.setopt(c.HTTPHEADER,header)
        #c.setopt(c.POSTFIELDS,payload)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CONNECTTIMEOUT, 5)
        c.perform()
        
        NAMELOOKUP_TIME=round(float(c.getinfo(c.NAMELOOKUP_TIME)),3)  # :.3f for display  result upto
        CONNECT_TIME=round(float(c.getinfo(c.CONNECT_TIME)),3)
        PRETRANSFER_TIME=round(float(c.getinfo(c.PRETRANSFER_TIME)),3)
        STARTTRANSFER_TIME=round(float(c.getinfo(c.STARTTRANSFER_TIME)),3)
        TOTAL_TIME=round(float(c.getinfo(c.TOTAL_TIME)),3)
        
        c.close()
        
        logging.info("NAME:{},NAMELOOKUP_TIME:{},CONNECT_TIME:{},PRETRANSFER_TIME:{},STARTTRANSFER_TIME:{},TOTAL_TIME:{}".format(url,NAMELOOKUP_TIME,CONNECT_TIME,PRETRANSFER_TIME,STARTTRANSFER_TIME,TOTAL_TIME))
        
        return (NAMELOOKUP_TIME,CONNECT_TIME,PRETRANSFER_TIME,STARTTRANSFER_TIME,TOTAL_TIME)
        
    except Exception as e:
        logging.error("Exception occoured in compute:{}".format(e))
        NAMELOOKUP_TIME=CONNECT_TIME=PRETRANSFER_TIME=STARTTRANSFER_TIME=TOTAL_TIME='null'
        return (NAMELOOKUP_TIME,CONNECT_TIME,PRETRANSFER_TIME,STARTTRANSFER_TIME,TOTAL_TIME)

