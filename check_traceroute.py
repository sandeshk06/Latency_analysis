#!/opt/python/bin/python3
import subprocess

def get_traceroute_result(url):
    LIST=[]

    try:
         check_stdout=subprocess.run(['traceroute','-T', url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         if check_stdout.stderr:
             retrun LIST
    
         else:

             STR=check_stdout.stdout.decode('utf-8').strip()
             LIST=STR.split('\n')
    
             retrun LIST
    
    except Exception as e:
        return LIST
