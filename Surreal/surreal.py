import sys
from pathlib import Path

# ruta_base = Path(__file__).resolve().parent.parent
# mrwalk_path = ruta_base / 'MrWalk'

# if mrwalk_path not in sys.path:
#     sys.path.append(str(mrwalk_path))

from MrWalk import MrWalk

from surreal_python_docs import SurrealPythonDocs

class Surreal:
    def __init__(self):
        """
        Inicializa el sistema de consola interactivo.
        """
        print("Welcome to Surreal Console!")
        print("Type 'help' for a list of commands.")
        print("Type 'exit' or 'quit' to leave the console.")
        self.api = None  # Instancia de SurrealPythonDocs

    def run(self):
        """
        Inicia el bucle interactivo de la consola.
        """
        while True:
            command = input("Surreal> ").strip()

            if command in ["exit", "quit"]:
                print("Exiting Surreal Console...")
                break
            elif command == "help":
                self.show_help()
            elif command.startswith("init"):
                self.init_api(command)
            elif command == "walk":
                self.execute_walk()
            elif command == "tree":
                self.execute_tree()
            elif command.startswith("prune"):
                self.execute_prune(command)
            else:
                print(f"Unknown command: {command}")

    def show_help(self):
        """
        Muestra la lista de comandos disponibles.
        """
        print("""
Available commands:
  init <path>       - Initialize the API with the given root path (default: current directory).
  walk              - Perform a directory walk and display the structure.
  tree              - Display the directory structure as a tree.
  prune <dirs>      - Prune the specified directories from the structure.
  help              - Show this help message.
  exit, quit        - Exit the console.
        """)

    def init_api(self, command):
        """
        Inicializa la API con un directorio base.
        """
        try:
            _, path = command.split(" ", 1)
        except ValueError:
            path = "."  # Directorio actual por defecto

        self.api = SurrealPythonDocs(path)
        print(f"API initialized with root_path: {self.api.root_path}")

    def execute_walk(self):
        """
        Ejecuta el método walk de la API.
        """
        if not self.api:
            print("Error: API not initialized. Use 'init <path>' first.")
            return

        self.api.walk()

    def execute_tree(self):
        """
        Ejecuta el método tree de la API.
        """
        if not self.api:
            print("Error: API not initialized. Use 'init <path>' first.")
            return

        self.api.tree()

    def execute_prune(self, command):
        """
        Ejecuta el método prune de la API.
        """
        if not self.api:
            print("Error: API not initialized. Use 'init <path>' first.")
            return

        try:
            _, dirs = command.split(" ", 1)
            exclude_dirs = dirs.split(",")
        except ValueError:
            print("Error: No directories specified for pruning.")
            return

        self.api.prune(exclude_dirs)

# class Surreal:
#     def __init__(self):

#         self.charles = MrWalk(' "." / "SurrealPythonDocs" ')

#         print("Charles Walk is charged")

#         self.structure = self.charles.walk([".py"], [".git", ".vscode"])

#         print(f"The structure is: {self.structure}")

#         print(self.charles.tree())

#         self.structure = self.charles.prune(["SurrealPythonDocs", "trash"])

#         print(f"The structure after pruning example is: {self.structure}")

#         print(self.charles.tree())


# if __name__ == "__main__":
#     Surreal()
