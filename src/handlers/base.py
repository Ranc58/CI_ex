import json

from tornado.web import RequestHandler
import http.client as httplib


class BaseAPIHandler(RequestHandler):

    @staticmethod
    def date_handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return obj

    def build_arguments_from_json(self):
        data = self.request.body
        args = json.loads(data.decode('utf-8')) if data else {}
        return args

    def json_response(self, data, status_code=httplib.OK, status_reason=None):
        if status_code >= httplib.BAD_REQUEST:
            self.set_header("Content-Type", 'application/problem+json')
        else:
            self.set_header("Content-Type", 'application/json')
        self.set_status(status_code, status_reason)
        try:
            self.write(json.dumps(data, default=self.date_handler, skipkeys=True))
        except Exception:
            self.write(json.dumps({'status': 'Internal Server Error'}, skipkeys=True))
        self.finish()

    def return_created(self, result, status_code=httplib.CREATED):
        self.json_response(result, status_code)

    def return_not_found(self, message='404 - Page not found'):
        result = dict(status="error", message=message)
        self.json_response(result, httplib.NOT_FOUND)

    def return_no_content(self, status_code=httplib.NO_CONTENT):
        self.set_status(status_code=status_code)
