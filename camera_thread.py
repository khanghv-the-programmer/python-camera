from flask import Flask, Response
from Services.API import CameraThread
import threading
app = Flask(__name__)
thread = CameraThread()

@app.route('/video/<string:ip>')
def video(ip):
    return Response(thread.generate_frame(ip), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera/active/<string:ip>')
def active_camera(ip):
    thread.active_camera_by_ip(ip)
    return "Done", 200

def start_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


flask_thread = threading.Thread(target=start_flask)
flask_thread.start()
flask_thread.join()

