class RequestForServiceMessage:

    def __init__(self, user_id, service_id, path_to_image, attr):
        self.user_id = user_id
        self.service_id = service_id
        self.path_to_image = path_to_image
        self.attr = attr
