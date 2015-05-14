from flask import Flask, jsonify, make_response

import csv

app = Flask(__name__)

@app.route('/<ip_address>', methods=['GET'])
def get_geolocation(ip_address):
    ip = ''.join(map(str, ip_address.split('.')))
    data = find_ip(ip)
    return jsonify({'location': data})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def find_ip(ip):
    loc_id = None
    with open('GeoLiteCity-Blocks.csv', 'rb') as ip_file:
        read = csv.reader(ip_file)
        next(read)
        ip_reader = csv.DictReader(ip_file)
        for address in ip_reader:
            if address['startIpNum'] == ip:
                loc_id = address['locId']
                break
    with open('GeoLiteCity-Location.csv', 'rb') as location_file:
        read = csv.reader(location_file)
        next(read)
        location_reader = csv.DictReader(location_file)
        for place in location_reader:
            if place['locId'] == loc_id:
                return place

if __name__ == '__main__':
    app.run(debug=True)