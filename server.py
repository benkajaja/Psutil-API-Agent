import flask
import psutil

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify(getInfo())

def getInfo():
    res = {}
    res['CPU'] = psutil.cpu_percent()
    res['Memory'] = psutil.virtual_memory()[2]
    res['Network'] = {'bytes_recv': '%s' % psutil.net_io_counters().bytes_recv, # f'{psutil.net_io_counters().bytes_recv}',
                      'bytes_sent': '%s' % psutil.net_io_counters().bytes_sent  # f'{psutil.net_io_counters().bytes_sent}'
                      }
    return res

app.run(host = '0.0.0.0', port = 5000)
