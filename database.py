


class DataBase:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db:
            self.db.close()

    def save_db(self):
        pass

    def get_db(self):
        pass

