#!/opt/python/bin/python3
import subprocess
import logging

def get_ping_result(url):
    LIST=[]

    try:
         check_stdout=subprocess.run(['ping','-c','20',url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         if check_stdout.stderr:
             return LIST
    
         else:

             STR=check_stdout.stdout.decode('utf-8').strip()
             LIST=STR.split('\n')
    
             return LIST
    
    except Exception as e:
        logging.error("Error while performing ping for site :{}".format(e))            
        return LIST
