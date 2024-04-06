class ResultFromServiceMessage:
    def __init__(self, request_id, result_file, status):
        self.request_id = request_id
        self.status = status
        self.result_file = result_file
