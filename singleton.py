"""
Creational Pattern - Singleton 單例模式
保證一個類別僅有一個實體，並提供一個存取他的全域存取點，而且自行實例化並向整個系統提供這個實例。
"""


class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)  # False

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)  # True
print(appState2.isLoggedIn)  # True
