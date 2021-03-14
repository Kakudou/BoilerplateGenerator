from dataclasses\
    import dataclass

from boilerplate_generator.src.utils.singleton\
    import Singleton
from boilerplate_generator.src\
    import SAVE_PATH


@Singleton
@dataclass
class InFilePersist:
    """This class is the in file storage system"""

    __save_path: str = SAVE_PATH

    @property
    def save_path(self) -> str:
        return self.__save_path

    @save_path.setter
    def save_path(self, save_path: str):
        self.__save_path = save_path
