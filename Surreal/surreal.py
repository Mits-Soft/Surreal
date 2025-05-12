import sys
from pathlib import Path

# ruta_base = Path(__file__).resolve().parent.parent
# mrwalk_path = ruta_base / 'MrWalk'

# if mrwalk_path not in sys.path:
#     sys.path.append(str(mrwalk_path))

from MrWalk import MrWalk

from SurrealPythonDocs import SurrealPythonDocs


# class Surreal:
#     def __init__(self):
#         """
#         Inicializa el sistema de consola interactivo.
#         """
#         print("Welcome to Surreal Console!")
#         print("Type 'help' for a list of commands.")
#         print("Type 'exit' or 'quit' to leave the console.")
#         try:
#             self.api = SurrealPythonDocs()
#         except Exception as e:
#             print(f"No se pudo inicializar SurrealPythonDocs: {e}")

#     def run(self):
#         """
#         Inicia el bucle interactivo de la consola.
#         """
#         while True:
#             command = input("Surreal> ").strip()

#             if command in ["exit", "quit"]:
#                 print("Surreal: Exiting Surreal Console...")
#                 break
#             elif command == "help":
#                 self.show_help()
#             elif command.startswith("init"):
#                 self.init_api(command)
#             elif command == "walk":
#                 self.execute_walk()
#             elif command == "tree":
#                 self.execute_tree()
#             elif command.startswith("prune"):
#                 self.execute_prune(command)
#             else:
#                 print(f"Surreal: Unknown command: {command}")

#     def show_help(self):
#         """
#         Muestra la lista de comandos disponibles.
#         """
#         print("""
#             Available commands:
#             init <path>       - Initialize the API with the given root path (default: current directory).
#             walk              - Perform a directory walk and display the structure.
#             tree              - Display the directory structure as a tree.
#             prune <dirs>      - Prune the specified directories from the structure.
#             help              - Show this help message.
#             exit, quit        - Exit the console.
#         """)

#     def init_api(self, command):
#         """
#         Inicializa la API con un directorio base.
#         """
#         try:
#             _, path = command.split(" ", 1)
#         except ValueError:
#             path = "."  # Directorio actual por defecto

#         try:
#             self.api = SurrealPythonDocs(path)
#         except Exception as e:
#             print(f"Surreal: No se pudo inicializar SurrealPythonDocs: {e}")
#         print(f"Surreal: API initialized with root_path: {self.api.root_path}")

#     def execute_walk(self):
#         """
#         Ejecuta el método walk de la API con listas de extensiones y exclusiones.
#         Permite mantener y modificar las extensiones usadas previamente.
#         """
#         if not self.api:
#             print("Surreal: Error: API not initialized. Use 'init <path>' first.")
#             return

#         # Mantener extensiones y exclusiones previas
#         if not hasattr(self, 'extensions'):
#             self.extensions = []
#         if not hasattr(self, 'exclude'):
#             self.exclude = []

#         print(f"Current extensions: {', '.join(self.extensions) if self.extensions else 'None'}")
#         print(f"Current exclusions: {', '.join(self.exclude) if self.exclude else 'None'}")

#         # Modificar extensiones
#         new_extensions = input("Enter file extensions to add/remove (comma-separated, e.g., .py,.txt), or press Enter to keep: ").strip()
#         if new_extensions:
#             for ext in new_extensions.split(","):
#                 ext = ext.strip()
#                 if ext in self.extensions:
#                     self.extensions.remove(ext)
#                     print(f"Removed extension: {ext}")
#                 else:
#                     self.extensions.append(ext)
#                     print(f"Added extension: {ext}")

#         # Modificar exclusiones
#         new_exclude = input("Enter directories to add/remove from exclusions (comma-separated, e.g., .git,__pycache__), or press Enter to keep: ").strip()
#         if new_exclude:
#             for excl in new_exclude.split(","):
#                 excl = excl.strip()
#                 if excl in self.exclude:
#                     self.exclude.remove(excl)
#                     print(f"Removed exclusion: {excl}")
#                 else:
#                     self.exclude.append(excl)
#                     print(f"Added exclusion: {excl}")

#         # Ejecutar walk con las listas actualizadas
#         self.api.walk(self.extensions, self.exclude)

#     def execute_tree(self):
#         """
#         Ejecuta el método tree de la API.
#         """
#         if not self.api:
#             print("Surreal: Error: API not initialized. Use 'init <path>' first.")
#             return

#         self.api.show_tree()

#     def execute_prune(self, command):
#         """
#         Ejecuta el método prune de la API.
#         """
#         if not self.api:
#             print("Surreal: Error: API not initialized. Use 'init <path>' first.")
#             return

#         try:
#             _, dirs = command.split(" ", 1)
#             exclude_dirs = dirs.split(",")
#         except ValueError:
#             print("Surreal: Error: No directories specified for pruning.")
#             return

#         self.api.prune(exclude_dirs)
        
# if __name__ == "__main__":
#     Surreal().run()

class Surreal:
    def __init__(self):
        
        self.ann = SurrealPythonDocs()

        # self.charles = MrWalk(' "." / "SurrealPythonDocs" ')
        self.ann.set_root_path("./SurrealPythonDocs")

        print("Ann is charged")

        self.structure = self.ann.walk([".py"], [".git", ".vscode", "__init__.py", "__pycache__", "dist", "SurrealPythonDocs.egg-info"])

        print(f"The structure is: {self.structure}")

        print(self.ann.show_tree())

        self.structure = self.ann.prune(["SurrealPythonDocs", "trash"])

        print(f"The structure after pruning example is: {self.structure}")

        print(self.ann.show_tree())
        
        self.docstrings_data = self.ann.extract_docstrings()
        
        pass


if __name__ == "__main__":
    Surreal()

# class SurrealAPI:
#     def get_menu(self):
#         raise NotImplementedError("API must implement get_menu method.")

#     def execute_command(self, command):
#         raise NotImplementedError("API must implement execute_command method.")


# class Surreal:
#     def __init__(self):
#         self.apis = {"docs": SurrealPythonDocs, "walk": MrWalk}
#         self.active_api = None
#         print("Welcome to Surreal Console!")
#         print("Type 'config' to configure APIs.")
#         print("Type 'exit' or 'quit' to leave the console.")

#     def run(self):
#         while True:
#             command = input("Surreal> ").strip()
#             if command in ["exit", "quit"]:
#                 print("Exiting Surreal Console...")
#                 break
#             elif command == "config":
#                 self.configure_api()
#             elif self.active_api:
#                 self.active_api.execute_command(command)
#             else:
#                 print("No API selected. Use 'config' to select an API.")

#     def configure_api(self):
#         print("Available APIs:")
#         for key in self.apis:
#             print(f"- {key}")
#         choice = input("Select an API: ").strip()
#         if choice in self.apis:
#             self.active_api = self.apis[choice]()
#             print(f"Switched to API: {choice}")
#         else:
#             print("Invalid API choice.")