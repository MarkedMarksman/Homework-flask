from flask import Flask, request, jsonify
from flask.views import MethodView
from db import Advertisement, Session
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from schema import CreateAdvertisement, PatchAdvertisement, VALIDATION_CLASS

app = Flask('ad_server')

class HttpError(Exception):

    def __init__(self, status_code: int, message: dict | list | str):
        self.status_code = status_code
        self.message = message

@app.errorhandler(HttpError)
def http_error_handler(error: HttpError):

    error_message = {"status": "error", "description": error.message}
    response = jsonify(error_message)
    response.status_code = error.status_code
    return response

def validate_json(json_data: dict, validation_model: VALIDATION_CLASS):

    try:
        model_object = validation_model(**json_data)
        model_object_dict = model_object.dict(exclude_none=True)
    except ValidationError as err:
        raise HttpError(400, message=err.errors())
    
    return model_object_dict


def get_ad(ad_id: int, session: Session):
    ad = session.query(Advertisement).get(ad_id)
    if ad is None:
        print('None of this exists')
    return ad

class AdvertisementView(MethodView):

    def get(self, ad_id):
        with Session() as session:
            ad = get_ad(ad_id, session)
            return jsonify(
                {
                    'id': ad.id,
                    'title': ad.title,
                    'user': ad.user,
                    'creation_date': ad.creation_date,
                }
            )


    def post(self):
        json_data = request.json
        with Session() as session:
            new_ad = Advertisement(**json_data)
            session.add(new_ad)
            session.commit()
            return jsonify(
                {
                    'id': new_ad.id,
                    'title': new_ad.title,
                    'user': new_ad.user,
                    'creation_date': new_ad.creation_date,
                }
            )

    def delete(self, ad_id):
        with Session() as session:
            ad = get_ad(ad_id, session)
            session.delete(ad)
            session.commit()
            return jsonify({'status': 'success'})

app.add_url_rule('/ads', view_func=AdvertisementView.as_view('post_ad'), methods=['POST'])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdvertisementView.as_view('ad'), methods=['GET', 'DELETE'])


if __name__ == '__main__':

    app.run(port=5000,debug=True)