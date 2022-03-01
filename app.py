from flask import Flask,render_template,request
from check_domain_result import compute
from check_traceroute import get_traceroute_result
from check_mtr import get_mtr_result
from check_ping import get_ping_result
from geo_latency_info import *
import folium
import os
import logging
from waitress import serve
logging.basicConfig(filename="/var/log/latency_app.log",level = logging.INFO,format = '%(levelname)s %(asctime)s %(message)s',datefmt = '%Y-%m-%d %H:%M:%S',filemode = 'a')
logger = logging.getLogger()

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
            result=[ int(res*1000) for res in result ]
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

            return render_template('show_traceroute_result.html',url=name,traceroute_result=traceroute_result,mtr_result=mtr_result,ping_result=ping_result)



    return render_template('traceroute.html')

@app.route('/geo_trace',methods=['GET','POST'])
def geo_trace():

    if request.method=='POST':
        name=request.form['name']
        if name == '':

            return render_template('geo_trace.html')

        else:

            #draw trace on map
            #remove old map

            #os.remove('templates/show_geo_trace.html')
            #logging.info("removed templates/show_geo_trace.html")

            m=folium.Map()
            Cordinate_list=[]
            geo_obj=GeoTrace(name)
            SOURCE_LOCATION,TRACES=geo_obj.get_geo_traceroute_data()

            Cordinate_list.append(list(SOURCE_LOCATION))

            if TRACES:
                for hop,cordinate in sorted(TRACES.items()):
                    Cordinate_list.append(cordinate)

            coordinates =[Cordinate_list]

            logger.info(coordinates)

            m = folium.Map(location=SOURCE_LOCATION, zoom_start=4)
            folium.TileLayer('stamentoner').add_to(m)
            folium.TileLayer('stamenterrain').add_to(m)
            folium.TileLayer('openstreetmap').add_to(m)
            folium.map.LayerControl().add_to(m)
           

            COORDINATE_LIST=coordinates[0]
            #add marker
            count=0
            for i in range(0,len(COORDINATE_LIST)):
                lat=COORDINATE_LIST[i][0]
                lon=COORDINATE_LIST[i][1]
                count+=1
                folium.Marker(location=[lat,lon],popup=('Route {}'.format(count)),icon = folium.Icon(color='green',icon='plus')).add_to(m)


            my_PolyLine=folium.PolyLine(locations=coordinates,weight=5,color='red')
            m.add_child(my_PolyLine)
            f_name=name.split('.')[0]
            file_name='show_geo_trace_'+str(f_name)+'.html'
            saved_file_name=os.path.join('templates/',file_name)
            m.save(saved_file_name)
            logging.info("saved new result to geo_trace.html")

        return render_template(file_name)

    return render_template('geo_trace.html')

if __name__=='__main__':
    serve(app,port=5000,threads=100)
