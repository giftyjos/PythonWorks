from abc import  ABC,abstractmethod

class Editor(ABC):

    
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def excute(self):
        pass
class vscode(Editor):

    def write(self):
        print("vscode write mmethod")
    def debug(self):
        print("vscode debug method")

    def excecute(self):
        print("vscode excute")

vscode_instance=Vscode()
vscode_instance.open()
    