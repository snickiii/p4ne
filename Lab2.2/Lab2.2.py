from flask import Flask, jsonify
from ipaddress import IPv4Interface
import re
import glob

files = glob.glob('config_files/*.log')

app = Flask(__name__)


def return_network(s):
    r = re.search("ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})", s)
    if r is not None:
        return IPv4Interface((r.group(1), r.group(2)))
    else:
        return None


@app.route('/')
def index():
    info = ('Flask - фреймворк для создания веб-приложений на языке программирования Python, '
            'использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2.')
    return info


@app.route('/configs')
def configs():
    hosts = [i.split('config_files\\')[1].split('_')[0] for i in files]
    return jsonify(hosts)


@app.route('/configs/<host>')
def config(host):
    networks = []
    for file in files:
        if host in file:
            with open(file, 'r') as f:
                for line in f:
                    network = return_network(line)
                    if network is not None:
                        networks.append(str(return_network(line)))
    return jsonify(networks)


if __name__ == '__main__':
    app.run(debug=True)
