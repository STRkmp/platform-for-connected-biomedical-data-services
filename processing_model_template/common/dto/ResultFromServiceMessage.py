class ResultFromServiceMessage:
    def __init__(self, request_id, status, path_to_result=None):
        self.request_id = request_id
        self.status = status
        self.path_to_result = path_to_result
