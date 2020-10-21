from pyngrok import ngrok
from pyngrok.exception import PyngrokNgrokHTTPError
from urllib.request import HTTPError
import json
from google.colab import drive
import os

EXTENSIONS = ["ms-python.python", "jithurjacob.nbpreviewer"]


class kagColabServer:
    def __init__(self, port, password=None, drive=True, kaggle=False, folder_tree=None):
        self.port = port
        self.drive = drive
        self.kaggle = kaggle
        self.password = password
        self.folder_tree = folder_tree
        self._install_and_start_code_server()
        self._start_ngrok_tunnel()
        self._connect_drive()

    def _connect_drive(self):
        if self.drive == True:
            drive.mount("/content/drive")

    def import_kaggle_data(self, username, kag_api_key, kag_data_api):
        if self.kaggle == True:
            self._connect_drive()
            folder_space_query_string = (
                f"?folder=/content/drive/My%20Drive/{self.folder_tree}"
            )
            try:
                user_workspace_path = f"/content/drive/My Drive/{self.folder_tree}"
                try:
                    os.mkdir(user_workspace_path)
                except Exception as e:
                    print("The same folder name exists already!")
                os.chdir(user_workspace_path)
                os.environ["KAGGLE_CONFIG_DIR"] = user_workspace_path
                kaggle_auth_file = {
                    "username": f"{username}", "key": f"{kag_api_key}"}
                with open("kaggle.json", "w") as outfile:
                    json.dump(kaggle_auth_file, outfile)
                os.system(f"{kag_data_api}" + " --force")
            except Exception as e:
                print(e)

            self._install_and_start_code_server()
            try:
                url = ngrok.connect(port=self.port)
                print(url)
            except (HTTPError, PyngrokNgrokHTTPError):
                ngrok.kill()
                url = ngrok.connect(port=self.port)
                print(
                    f"Your newly generated url: {url + folder_space_query_string}")

    def _install_and_start_code_server(self):
        if self.kaggle == False:
            os.system("curl -fsSL https://code-server.dev/install.sh | sh")
            for extension in EXTENSIONS:
                os.system(f"code-server --install-extension {extension}")
            if self.password:
                os.system(
                    f"PASSWORD={self.password} code-server --port {self.port} --disable telemetry")
            else:
                os.system(
                    f"nohup code-server --port {self.port} --auth none &")

    def _start_ngrok_tunnel(self):
        if self.kaggle == False:
            try:
                if self.folder_tree == None:
                    url = ngrok.connect(port=self.port)
                    print(url)
                else:
                    ngrok.kill()
                    url = ngrok.connect(port=self.port)
                    print(
                        f"Your newly generated url: {url}" + f"?folder=/content/drive/My%20Drive/{self.folder_tree}")
            except (HTTPError, PyngrokNgrokHTTPError):
                if self.folder_tree is None:
                    ngrok.kill()
                    url = ngrok.connect(port=self.port)
                    print(f"Your newly generated url: {url}")
                else:
                    ngrok.kill()
                    url = ngrok.connect(port=self.port)
                    print(
                        f"Your newly generated url: {url}" + f"?folder=/content/drive/My%20Drive/{self.folder_tree}")
