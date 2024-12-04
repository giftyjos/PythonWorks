# string representation of a object

# __str__(self)

# class Editor (name,vendor)

# editor_instance print=>nameclass Editor:


class Editor:
    name:str
    vendor:str
    def __init__(self, name, vendor):
        self.name = name
        self.version = vendor
        

    def __str__(self):
        return self.name

# Create an instance of Editor
editor_instance1=Editor("pycharm", "jebranis")

# Use the editor
editor_instance2=Editor("intellij","jetbrains")

editor_instance3=Editor("vscode","microsoft")
print(editor_instance2)
