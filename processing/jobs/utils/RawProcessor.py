from abc import ABCMeta, abstractmethod
from .writeToJSON import writeToJSONFile
import os

class RawProcessor(metaclass=ABCMeta):

    @property
    @abstractmethod
    def toChart(self):
        pass

    def run(self):
        json = self.toChart()
        print(os.path.abspath()+'../../../../charts/i.json')
        writeToJSONFile({},os.path.abspath()+'../../../../charts/i.json')
    

    if __name__ == "__main__":
        run()
