#!/opt/python/bin/python3
import subprocess

def get_traceroute_result(url):
    LIST=[]

    try:
         check_stdout=subprocess.run(['/usr/sbin/traceroute','-T', url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         if check_stdout.stderr:
             return LIST
    
         else:

             STR=check_stdout.stdout.decode('utf-8').strip()
             LIST=STR.split('\n')
    
             return LIST
    
    except Exception as e:
        print(e)            
        return LIST
