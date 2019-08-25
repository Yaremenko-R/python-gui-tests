from pywinauto.application import Application as WinApplication
from fixture.group import GroupHelper


class Application:

    def __init__(self, target, testdata):
        self.application = WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")
        self.group = GroupHelper(self)
        self.testdata = testdata

    def destroy(self):
        self.main_window.close()