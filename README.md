# Altair | McMaster GDC 2025 🎉

# Installation
In order to use Altair, you must first have a valid installation of [Latex](https://www.latex-project.org/get/).
Once you have installed Latex, download the latest release of Altair and run the executable!

# Usage
Simply drag any file you want to remix into the Altair window. After some time, your remixed paper should appear floating around. Click in it to preview it in your default browser!

# Compiling
Install PyInstaller
```shell
pip install PyInstaller
```

Navigate to the project directory and run the following command. The output executable can be doung in the dist folder
```shell
pyinstaller --onefile --add-data "src/backend/index.html;backend" --add-data "assets/file-icon.png;assets" src/main.py
```