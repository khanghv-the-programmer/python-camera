from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Services.model import Users,Captures,Cameras,Events

db_schema = 'streaming_camera'
postgresql_engine = create_engine("postgresql://postgres:cameraip2024@cameraip.cilyqldqbjqk.ap-southeast-1.rds.amazonaws.com:5432/postgres",
                                  connect_args={'options': '-csearch_path={}'.format(db_schema)})
Session = sessionmaker(bind=postgresql_engine)
session = Session()

users = session.query(Users).all()
for user in users:
    print(user.id, user.full_name, user.username, user.password,user.isactive)

cameras = session.query(Cameras).all()
for camera in cameras:
    print(camera.id, camera.name)

captures = session.query(Captures).all()
for capture in captures:
    print(capture.id, capture.image)

events = session.query(Events).all()
for event in events:
    print(event.id, event.camera_id)
