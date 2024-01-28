from Services.API.restplus import api
from flask_restplus import Resource, fields
from flask import request, jsonify,make_response
from datetime import datetime
import logging
import json
from Services.Utilize.ReadConfigurationFile import read_config_from_file as config
import urllib
from sqlalchemy import create_engine
from Services.Handler import UsersHandler
from Services.model import Users
import numpy as np

CONN_URI = config.connection["postgres"]
PASSWORD = config.connection["postgres_password"]
DATABASE = config.connection["postgres_database"]
SCHEMA = config.schema["postgres_schema"]
CONN_STR = CONN_URI.format(password=urllib.parse.quote(PASSWORD),database=DATABASE)

ns = api.namespace('users/', description='''Users Screen ''')

model_edit_user = ns.model('edit_users', {
    "user_name": fields.String(require=True,example=''),
    "password": fields.String(require=True,example=''),
    "full_name": fields.String(require=True,example=''),
})

model_delete_user = ns.model('delete_users', {
    "id": fields.Integer(require=True,example=1),
})

model_get_user = ns.model('get_users', {
    "user_name": fields.String(require=True,example=''),
})

log = logging.getLogger(__name__)
@ns.route('/EditUser', methods=['POST','DELETE'])
class EditUser(Resource):
    @ns.expect(model_edit_user, validate=False)
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
                UsersHandler(postgresql_engine).insertUser(params)
                response = {
                    "status": 200,
                    "message": 'Create User Success!'
                }
                return jsonify(response)
            except Exception as E:
                raise E

        except Exception as e:
            log.error('[{}] [API][CreateUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))

    @ns.expect(model_delete_user, validate=False)
    def delete(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))

            # tenant_id = request.json['tenant_id']
            # language = request.json['language']
            # customer_type_filter = request.json['customer_type_filter']
            # product_categories_filter = request.json["product_categories_filter"]
            # coin_from_filter = request.json["coin_from_filter"]
            # coin_to_filter = request.json["coin_to_filter"]
            # limit = 10
            # offset = 0
            # condition = []
            # # transaction condition
            # condition.append(MemberDW.TenantId == tenant_id)
            # if customer_type_filter is not None and customer_type_filter.strip() != '':
            #     condition.append(MemberDW.MemberTypeCode == customer_type_filter)
            # # if product_categories_filter is not None and product_categories_filter.strip() != '':
            # #     condition.append(MemberDW.RankTypeCode == product_categories_filter)
            # if coin_from_filter is not None:
            #     condition.append(MemberDW.Coin >= coin_from_filter)
            #     if coin_to_filter is not None:
            #         condition.append(MemberDW.Coin <= coin_to_filter)
            #
            # try:
            #     con_str = CONN_URI.format(password=urllib.parse.quote(PASSWORD),
            #                               database=SCHEMA_DEFAULT)
            #     engine = create_engine(con_str)
            #     query = CustomerByLogCoinHandler(engine, tenant_id=tenant_id).generate_query(condition)
            #     data_frames = CommonHandler.get_data_all(con_str, query, "BaselineTimeNum")
            #
            #     # has_next_page = False
            #     frame = []
            #     if not data_frames.empty:
            #         data_frames = data_frames.sort_values(by=['ExpiringDate'], ascending=False, ignore_index=True)
            #         part_data = data_frames[offset:limit + offset]
            #         # if len(part_data) > limit - 1:
            #         #     has_next_page = True
            #         #     part_data = part_data.drop(part_data.index[-1])
            #         if not part_data.empty:
            #             part_data = part_data.replace({np.nan: None})
            #         frame = part_data.to_dict(orient='records')
            #
            #     total = len(data_frames)
            response = {
                "status": 200,
                "result": {
                    # "hasNextPage": has_next_page,
                    "totalRecord": 1,
                    "items": 1,

                }
            }
            return jsonify(response)
            # except Exception as E:
            #     raise E

        except Exception as e:
            log.error('[{}] [API][CreateUser] -> {}: {} '.format(request.method, request.url, str(e)))

        finally:
            log.info(f"[{request.method}] [API][CreateUser]::: \n %s ___End Time: {datetime.now()}",
                     json.dumps(request.json))
@ns.route('/GetUser', methods=['GET','POST'])
class GetUser(Resource):
    def get(self):
        start_time = datetime.utcnow()
        try:
            log.info(f"[{request.method}] [API][GetAllUser]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            try:
                postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
                data = UsersHandler(postgresql_engine).getUser()
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
    @ns.expect(model_get_user, validate=False)
    def post(self):
        start_time = datetime.utcnow()
        try:
            condition =[]
            log.info(f"[{request.method}] [API][GetUserCondition]::: \n %s ___Start Time: {start_time}",
                     json.dumps(request.json))
            if request.json:
                user_name = request.json['user_name']
                list_user_name = user_name.split(',')
                condition.append(Users.username.in_(list_user_name))
            else:
                return make_response('User not Input Parameter', 404)
            try:
                postgresql_engine = create_engine(CONN_STR, connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
                data = UsersHandler(postgresql_engine).getUser(condition)
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

