from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork


class UnitOfWorkMongo(AbstractUnitOfWork):
    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def collect_new_events(self):
        pass
