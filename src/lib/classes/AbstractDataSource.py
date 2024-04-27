from abc import ABC, abstractmethod # A biblioteca ABC garante que a nossas funções tenham todos os requerimentos que classes abstratas precisam ter.

class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod # Aqui estamos usando um decorator que marque que esse é um metodo abstrato
    def start(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")

    def hello_world(self):
        print('Hello World')