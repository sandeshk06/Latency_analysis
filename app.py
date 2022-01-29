from flask import Flask,render_template,request
from check_domain_result import compute 
from check_traceroute import get_traceroute_result 
from check_mtr import get_mtr_result 
from check_ping import get_ping_result 
from geo_latency_info import *
from waitress import serve

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/latency',methods=['GET','POST'])
def latency():
    if request.method=='POST':
        name=request.form['name']
        if name == '':
             
            return render_template('latency.html')
        else:
            
            result=compute(name)
            return render_template('show_latency_result.html',url=name,result=result)



    return render_template('latency.html')

@app.route('/traceroute',methods=['GET','POST'])
def traceroute():
    if request.method=='POST':
        name=request.form['name']
        if name == '':

            return render_template('traceroute.html')
        else:

            traceroute_result=get_traceroute_result(name)
            mtr_result=get_mtr_result(name)
            ping_result=get_ping_result(name)
            
            #draw trace on map
            Cordinate_list=[]
            geo_obj=GeoTrace(name)
            SOURCE_LOCATION,TRACES=geo_obj.get_geo_traceroute_data()
            
            Cordinate_list.append(list(SOURCE_LOCATION))

            if TRACES:
                for hop,cordinate in sorted(TRACES.items()):
                    Cordinate_list.append(cordinate)

            


            return render_template('show_traceroute_result.html',url=name,traceroute_result=traceroute_result,mtr_result=mtr_result,ping_result=ping_result)



    return render_template('traceroute.html')



if __name__=='__main__':
    serve(app,port=5000,threads=100)
