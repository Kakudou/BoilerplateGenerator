from abc\
    import abstractmethod
from typing\
    import List

from boilerplate_generator.src.boilerplate_generator.gateway.abstract_gateway\
    import AbstractGateway


class EntityGateway(AbstractGateway):

    @abstractmethod
    def find_all_by_project(self, project_name) -> List[str]:
        raise NotImplementedError
