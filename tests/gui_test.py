# tests/gui_test.py

import source.gui.gui as gui

if __name__ == "__main__":
    gui_app = gui.GUIManager()
    gui_app.main_loop()
