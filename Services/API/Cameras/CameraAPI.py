import pandas.io.json

from Services.API.restplus import api
from flask_restplus import Resource, fields
from flask import request, jsonify,make_response
from datetime import datetime
import logging
import json
from Services.Utilize.ReadConfigurationFile import read_config_from_file as config
import urllib
from sqlalchemy import create_engine
from Services.Handler import CameraHandler
from Services.model import Cameras
import numpy as np

CONN_URI = config.connection["postgres"]
PASSWORD = config.connection["postgres_password"]
DATABASE = config.connection["postgres_database"]
SCHEMA = config.schema["postgres_schema"]
CONN_STR = CONN_URI.format(password=urllib.parse.quote(PASSWORD),database=DATABASE)

ns = api.namespace('cameras/', description='''Cameras Screen ''')

model_edit_camera = ns.model('edit_cameras', {
    "name": fields.String(require=True,example=''),
    "ip": fields.String(require=True,example=''),
    "port": fields.String(require=True,example=''),
    "username": fields.String(require=True,example=''),
    "password": fields.String(require=True,example=''),
})

model_delete_camera = ns.model('delete_cameras', {
    "id": fields.Integer(require=True,example=1),
})

model_get_camera = ns.model('get_users', {
    "name": fields.String(require=True,example=''),
})
nowTime = datetime.utcnow()
model_get_capture = ns.model('get_capture', {
    "id": fields.Integer(require=True,example=1),
    "From": fields.DateTime(require=True,dt_format="iso8601"),
    "To": fields.DateTime(require=True,dt_format="iso8601"),
})
model_update_camera = ns.model('edit_cameras', {
    "id": fields.Integer(require=True,example=1),
    "is_active": fields.Boolean(require=True,example=True),
})
model_get_lastest_capture = ns.model('get_capture', {
    "id": fields.Integer(require=True,example=1),
})
log = logging.getLogger(__name__)

@ns.route('/updateCameras', methods=['POST'])
class UpdateCamera(Resource):
    @ns.expect(model_update_camera, validate=False)
    def post(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            jsonString = request.json
            id = jsonString['id']
            is_active = jsonString['is_active']
            postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
            CameraHandler(postgresql_engine).updateCamera(id,is_active)
            response = {
                "status": 200,
                "message":"Successfully Update Camera"
            }
            return jsonify(response)

        except Exception as e:
            log.error('[{}] [API][CreateUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))

@ns.route('/EditCameras', methods=['POST','DELETE'])
class EditCamera(Resource):
    @ns.expect(model_edit_camera, validate=False)
    def post(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][EditUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            params = request.json
            if params:
               key = params.keys()
               if len(key) < 3:
                   return make_response('User not Input Parameter', 404)
            else:
                return make_response('User not  Input any Parameter', 404)
            try:
                postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
                CameraHandler(postgresql_engine).insertCamera(params)
                response = {
                    "status": 200,
                    "message": 'Create Camera Success!'
                }
                return jsonify(response)
            except Exception as E:
                raise E

        except Exception as e:
            log.error('[{}] [API][CreateUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))

    @ns.expect(model_delete_camera, validate=False)
    def delete(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            jsonString = request.json
            id = jsonString['id']
            postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
            CameraHandler(postgresql_engine).deleteCapture(id)
            CameraHandler(postgresql_engine).deleteEvent(id)
            CameraHandler(postgresql_engine).deleteCamera(id)
            response = {
                "status": 200,
                "message":"Successfully Deleted Camera"
            }
            return jsonify(response)
            # except Exception as E:
            #     raise E

        except Exception as e:
            log.error('[{}] [API][CreateUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))
@ns.route('/GetCamera', methods=['GET','POST'])
class GetCamera(Resource):
    def get(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][GetAllUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            try:
                postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
                data = CameraHandler(postgresql_engine).getCamera()
                frame = []
                if not data.empty:
                    part_data = data.replace({np.nan: None})
                    frame = part_data.to_dict(orient='records')

                total = len(data)
                response = {
                    "status": 200,
                    "result": {
                        "totalRecord": total,
                        "items": frame,

                    }
                }
                return jsonify(response)
            except Exception as E:
                raise E

        except Exception as e:
            log.error('[{}] [API][GetAllUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][GetAllUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))
    @ns.expect(model_get_camera, validate=False)
    def post(self):
        start_time = datetime.utcnow()
        try:
            condition =[]
            log.info(f"[{request.method}] [API][GetUserCondition]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            if request.json:
                name = request.json['name']
                list_camera_name = name.split(',')
                condition.append(Cameras.name.in_(list_camera_name))
            else:
                return make_response('User not Input Parameter', 404)
            try:
                postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
                data = CameraHandler(postgresql_engine).getCamera(condition)
                frame = []
                if not data.empty:
                    part_data = data.replace({np.nan: None})
                    frame = part_data.to_dict(orient='records')

                total = len(data)
                response = {
                    "status": 200,
                    "result": {
                        "totalRecord": total,
                        "items": frame,

                    }
                }
                return jsonify(response)
            except Exception as E:
                raise E

        except Exception as e:
            log.error('[{}] [API][GetUserCondition] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][GetUserCondition]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))



@ns.route('/GetCapture', methods=['POST'])
class CaptureApi(Resource):
    @ns.expect(model_get_capture, validate=False)
    def post(self):
        try:
            jsonString = request.json

            id= jsonString['id']
            fromDate = jsonString['From']
            toDate = jsonString['To']

            postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
            captureDatas = CameraHandler(postgresql_engine).getCapture(id,fromDate,toDate)
            print(captureDatas)
            # _temp = {
            #     "id", "img"
            # }

            result = {"listImages": []}

            for item in captureDatas:
                _temp = {}
                id, img, date = item[0], item[1], item[2]
                _temp["id"] = id
                _temp["img"] = img
                _temp["date"] = date.strftime("%m/%d/%Y, %H:%M:%S")
                result["listImages"].append(_temp)

            # frame = []
            # if not captureDatas.empty:
            #     part_data = captureDatas.replace({np.nan: None})
            #     frame = part_data.to_dict(orient='records')
            return jsonify(result)
        except Exception as e:
            log.error('[{}] [API][GetUserCondition] -> {}: {} '.format(request.method, request.url, str(e)))
@ns.route('/GetLastestCapture', methods=['POST'])
class CaptureLatestApi(Resource):
    @ns.expect(model_get_capture, validate=False)
    def post(self):
        try:
            jsonString= request.json
            postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
            captureDatas = CameraHandler(postgresql_engine).getLastCapture(jsonString['id'])
            result ={}
            result["id"] = captureDatas[0]
            result["img"] = captureDatas[1]
            result["date"] = captureDatas[2].strftime("%m/%d/%Y, %H:%M:%S")
            return jsonify(result)
        except Exception as e:
            log.error('[{}] [API][GetUserCondition] -> {}: {} '.format(request.method, request.url, str(e)))
