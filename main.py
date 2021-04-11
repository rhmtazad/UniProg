from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3
import sys
import ctypes

main_window, _ = loadUiType('ui/main.ui')


# main application class
class MainApp(QMainWindow, main_window):
    def __init__(self):
        # call the parent constructor
        QMainWindow.__init__(self)

        # setup the user interface
        self.setupUi(self)

        # center the window
        self.center_window()

        # handle button actions
        self.button_handler()

        # handle switch between pages
        self.page_handler()

        # make sure the login page is default
        self.logout()

    # position application window in center
    def center_window(self):
        # geometry of the main window
        frame_geometry = self.frameGeometry()

        # center point of screen
        center_point = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        frame_geometry.moveCenter(center_point)

        # top left of rectangle becomes top left of window centering it
        self.move(frame_geometry.topLeft())

    # switch between pages
    def page_handler(self):
        # student portal page
        self.studentPortalBtn.clicked.connect(lambda: self.page('StudentPortal'))
        self.stdPortalDBBtn.clicked.connect(lambda: self.page('stdPortalDashboardView'))
        self.stdPortalAddInfoBtn.clicked.connect(lambda: self.page('stdPortalDashboardModify'))

        # degreePlan portal page
        self.degreePlanPortalBtn.clicked.connect(lambda: self.page('DegreePlanPortal'))
        self.dpPortalDBBtn.clicked.connect(lambda: self.page('dashboardCreditsView'))
        self.dpPortalAddCoursesBtn.clicked.connect(lambda: self.page('AddCourse'))
        self.dpPortalDPViewBtn.clicked.connect(lambda: self.page('DegreePlan'))
        self.dpPortalCoursesViewBtn.clicked.connect(lambda: self.page('ViewCourse'))

        # go to home page
        self.stdPortalHomeBtn.clicked.connect(lambda: self.page('MainPage'))
        self.dpPortalHomeBtn.clicked.connect(lambda: self.page('MainPage'))

        # add student page
        self.rgstrBtn.clicked.connect(lambda: self.page('RegisterPage'))

    # handle actions for each button
    def button_handler(self):
        # login when button is pressed
        self.lgnBtn.clicked.connect(self.login)

        # logout when button is pressed
        self.lgtBtnMainPage.clicked.connect(self.logout)
        self.stdPortalLgtBtn.clicked.connect(self.logout)
        self.dpPortalLgtBtn.clicked.connect(self.logout)

        # back button
        self.backBtnRegisterPage.clicked.connect(self.logout)

    def page(self, name):
        if name == 'MainPage':
            self.mainWindows.setCurrentWidget(self.MainPage)
        elif name == 'LoginPage':
            self.mainWindows.setCurrentWidget(self.LoginPage)
        elif name == 'RegisterPage':
            self.mainWindows.setCurrentWidget(self.RegisterPage)
        elif name == 'StudentPortal':
            self.mainWindows.setCurrentWidget(self.StudentPortal)
            self.studentWindows.setCurrentWidget(self.stdPortalDashboardView)
        elif name == 'stdPortalDashboardModify':
            self.studentWindows.setCurrentWidget(self.stdPortalDashboardModify)
        elif name == 'stdPortalDashboardView':
            self.studentWindows.setCurrentWidget(self.stdPortalDashboardView)
        elif name == 'DegreePlanPortal':
            self.mainWindows.setCurrentWidget(self.DegreePlanPortal)
            self.dPlanWindows.setCurrentWidget(self.dashboardCreditsView)
        elif name == 'dashboardCreditsView':
            self.dPlanWindows.setCurrentWidget(self.dashboardCreditsView)
        elif name == 'AddCourse':
            self.dPlanWindows.setCurrentWidget(self.AddCourse)
        elif name == 'DegreePlan':
            self.dPlanWindows.setCurrentWidget(self.DegreePlan)
        elif name == 'ViewCourse':
            self.dPlanWindows.setCurrentWidget(self.ViewCourse)
        else:
            print('wrong input name or object name')

    def login(self):
        entered_username = self.unameInput.text()
        entered_password = self.passInput.text()

        # get username and password form database

        # evaluate input username and password
        if entered_username == "admin" and entered_password == "admin":
            # set home page as current page
            self.page('MainPage')

            # clear the username and password input fields
            self.unameInput.clear()
            self.passInput.clear()
        else:
            # clear the input fields and say try again
            self.unameInput.clear()
            self.passInput.clear()
            ctypes.windll.user32.MessageBoxW(None, "Incorrect Credentials", "Error!", 0)

    def logout(self):
        # clear the input fields and say try again
        self.unameInput.clear()
        self.passInput.clear()

        # set login page as current page
        self.page('LoginPage')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
