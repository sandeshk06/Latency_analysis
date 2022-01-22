from flask import Flask,render_template,request
from check_domain_result import compute 
from check_traceroute import get_traceroute_result 
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

            result=get_traceroute_result(name)
            return render_template('show_traceroute_result.html',url=name,result=result)



    return render_template('traceroute.html')



if __name__=='__main__':
    serve(app,port=5000,threads=100)
