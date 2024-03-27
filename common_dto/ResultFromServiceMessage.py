class ResultFromServiceMessage:
    def __init__(self, user_id, service_id, path_to_origin_image, answer):
        self.user_id = user_id
        self.service_id = service_id
        self.path_to_origin_image = path_to_origin_image
        self.answer = answer
