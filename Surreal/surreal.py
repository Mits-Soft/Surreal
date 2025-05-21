import sys
from pathlib import Path

# ruta_base = Path(__file__).resolve().parent.parent
# mrwalk_path = ruta_base / 'MrWalk'

# if mrwalk_path not in sys.path:
#     sys.path.append(str(mrwalk_path))

from MrWalk import MrWalk
from SurrealPythonDocs import SurrealPythonDocs

class SurrealPythonDocsInterface:
    """
    Interfaz CLI para SurrealPythonDocs, pensada para ser importada y usada desde la CLI Surreal.
    """
    def __init__(self, root_path=None):
        try:
            self.api = SurrealPythonDocs(root_path) if root_path else SurrealPythonDocs()
        except Exception as e:
            print(f"No se pudo inicializar SurrealPythonDocs: {e}")
            self.api = None
        self.extensions = []
        self.exclude = []

    def init(self, path=None):
        try:
            # Si el path es vacío o None, usar el directorio actual
            if not path:
                self.api = SurrealPythonDocs()
            else:
                self.api = SurrealPythonDocs(path)
            print(f"Surreal: API initialized with root_path: {self.api.root_path}")
        except Exception as e:
            print(f"Surreal: No se pudo inicializar SurrealPythonDocs: {e}")

    def walk(self):
        if not self.api:
            print("Surreal: Error: API not initialized. Use 'init <path>' first.")
            return
        print(f"Current extensions: {', '.join(self.extensions) if self.extensions else 'None'}")
        print(f"Current exclusions: {', '.join(self.exclude) if self.exclude else 'None'}")
        new_extensions = input("Enter file extensions to add/remove (comma-separated, e.g., .py,.txt), or press Enter to keep: ").strip()
        if new_extensions:
            for ext in new_extensions.split(","):
                ext = ext.strip()
                if ext in self.extensions:
                    self.extensions.remove(ext)
                    print(f"Removed extension: {ext}")
                else:
                    self.extensions.append(ext)
                    print(f"Added extension: {ext}")
        new_exclude = input("Enter directories to add/remove from exclusions (comma-separated, e.g., .git,__pycache__), or press Enter to keep: ").strip()
        if new_exclude:
            for excl in new_exclude.split(","):
                excl = excl.strip()
                if excl in self.exclude:
                    self.exclude.remove(excl)
                    print(f"Removed exclusion: {excl}")
                else:
                    self.exclude.append(excl)
                    print(f"Added exclusion: {excl}")
        self.api.walk(self.extensions, self.exclude)

    def tree(self):
        if not self.api:
            print("Surreal: Error: API not initialized. Use 'init <path>' first.")
            return
        self.api.show_tree()

    def prune(self, exclude_dirs):
        if not self.api:
            print("Surreal: Error: API not initialized. Use 'init <path>' first.")
            return
        self.api.prune(exclude_dirs)

    def extract_docstrings(self):
        if not self.api:
            print("Surreal: Error: API not initialized. Use 'init <path>' first.")
            return None
        return self.api.extract_docstrings()

    def render_document(self, docstrings_data, *args, **kwargs):
        if not self.api:
            print("Surreal: Error: API not initialized. Use 'init <path>' first.")
            return None
        return self.api.render_document(docstrings_data, *args, **kwargs)

    def show_help(self):
        print("""
            Available commands:
            init <path>       - Initialize the API with the given root path (default: current directory).
            walk              - Perform a directory walk and display the structure.
            tree              - Display the directory structure as a tree.
            prune <dirs>      - Prune the specified directories from the structure.
            extract           - Extract docstrings from the codebase.
            render            - Render documentation from extracted docstrings.
            help              - Show this help message.
            exit, quit        - Exit the console.
        """)

    def execute_command(self, command):
        if command == "help":
            self.show_help()
        elif command.startswith("init"):
            parts = command.split(maxsplit=1)
            path = parts[1] if len(parts) > 1 and parts[1].strip() else None
            self.init(path)
        elif command == "walk":
            self.walk()
        elif command == "tree":
            self.tree()
        elif command.startswith("prune"):
            try:
                _, dirs = command.split(" ", 1)
                exclude_dirs = [d.strip() for d in dirs.split(",")]
            except ValueError:
                print("Surreal: Error: No directories specified for pruning.")
                return
            self.prune(exclude_dirs)
        elif command == "extract":
            docstrings = self.extract_docstrings()
            print(docstrings)
        elif command == "render":
            docstrings = self.extract_docstrings()
            if docstrings:
                doc = self.render_document(docstrings, "JsonDot", "2023", "MitsSoft", "MIT License")
                print(doc)
        else:
            print(f"Surreal: Unknown command: {command}")

# CLI principal
class Surreal:
    def __init__(self):
        # Diccionario de APIs disponibles (puedes registrar más aquí)
        self.apis = {
            'docs': SurrealPythonDocsInterface,
            # 'mrwalk': MrWalkInterface, # Ejemplo para futuras APIs
        }
        self.history = []
        self.active_api = None
        print("Welcome to Surreal Console!")
        print("Type 'help' for a list of commands.")
        print("Type 'exit' or 'quit' to leave the console.")
        print("Type 'apis' to list and activate available APIs.")

    def run(self):
        while True:
            print("\nType 'apis' to list and activate available APIs.")
            try:
                command = input("Surreal> ").strip()
            except EOFError:
                print("\nSurreal: Exiting Surreal Console...")
                break
            if command in ["exit", "quit"]:
                print("Surreal: Exiting Surreal Console...")
                break
            elif command == "" or command == "":
                break
            elif command == "help":
                self.show_help()
            elif command == "apis":
                self.select_api_menu()
            elif self.active_api:
                self.active_api.execute_command(command)
            else:
                print("No API active. Type 'apis' to select one.")

    def show_help(self):
        print("""
Surreal CLI - Main Commands:
  apis         - List and activate available APIs
  help         - Show this help message
  exit, quit   - Exit the Surreal console

When an API is active, you can use its commands directly here or enter its menu with 'apis'.
Use 'back' to return from an API menu to this main prompt.
""")

    def select_api_menu(self):
        print("Available APIs:")
        for key in self.apis:
            print(f"- {key}")
        choice = input("Select an API (or type 'back' to cancel): ").strip()
        if choice == "back":
            print("Returning to main console.")
            return
        if choice in self.apis:
            self.active_api = self.apis[choice]()
            print(f"Activated API: {choice}")
            self.api_menu_loop()
        else:
            print("Invalid API choice.")

    def api_menu_loop(self):
        print("Entering API menu. Type 'back' to return to main console.")
        while True:
            try:
                api_command = input("Surreal[API]> ").strip()
            except EOFError:
                print("\nSurreal: Exiting Surreal Console...")
                exit(0)
            if api_command == "back":
                print("Returning to main console.")
                break
            elif api_command in ["exit", "quit"]:
                print("Surreal: Exiting Surreal Console...")
                exit(0)
            else:
                self.active_api.execute_command(api_command)

if __name__ == "__main__":
    Surreal().run()