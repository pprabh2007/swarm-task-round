from flask import Flask, jsonify, abort, request, make_response, url_for,redirect,send_file
import sys

botPose=[[3,4],[5,7],[8,9]]
obstaclePose=[[0,0],[1,1],[3,3]]
app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/', methods = ['GET'])
def getInfo():
    return redirect('/botPose')
    
@app.route('/map', methods = ['GET'])   #Hosts map at http://127.0.0.1:5000/map
def getMap():
    return send_file('images/map.png', mimetype='image/png',cache_timeout=-1)

@app.route('/botPose', methods = ['GET']) #Hosts botPose at http://127.0.0.1:5000/botPose and so on
def getBotPose():
    global botPose
    listPos=[{'posX': x,'posY': y} for [x,y] in botPose]
    return jsonify(listPos)

@app.route('/obstaclesPose', methods = ['GET'])
def getObstaclePose():
    global obstaclePose
    listPos=[{'posX': x,'posY': y} for [x,y] in obstaclePose]
    return jsonify(listPos)

@app.route('/move', methods = ['GET'])
def move():
    global botPose,obstaclePose
    data=request.json
    if 'botId' not in data or 'moveType' not in data:
        abort(400)
    data['botId']=int(data['botId'])
    data['moveType']=int(data['moveType'])
    if data['botId']<=0 or data['botId']>len(botPose):
        abort(400)
    if data['moveType']<=0 or data['moveType']>8:
        abort(400)
    pass    
    return jsonify({'success': 0})

if __name__ == '__main__':
    app.run(debug = True)