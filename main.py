<<<<<<< HEAD
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        uic.loadUi('ui/main.ui', self)
        self.center_window()
        self.page('dashboard_page')

        # handle button actions
        self.button_handler()

        # handle switch between pages
        self.page_handler()

    # switch between pages
    def page_handler(self):
        # pages navigation
        self.dashboard.clicked.connect(lambda: self.page('dashboard_page'))
        self.degreeplan.clicked.connect(lambda: self.page('degreeplan_page'))
        self.courses.clicked.connect(lambda: self.page('courses_page'))
        self.account.clicked.connect(lambda: self.page('account_page'))

    # handle actions for each button
    def button_handler(self):
        self.closeBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)

    def page(self, name):
        if name == 'dashboard_page':
            self.page_manager.setCurrentWidget(self.dashboard_page)
        elif name == 'degreeplan_page':
            self.page_manager.setCurrentWidget(self.degreeplan_page)
        elif name == 'courses_page':
            self.page_manager.setCurrentWidget(self.courses_page)
        elif name == 'account_page':
            self.page_manager.setCurrentWidget(self.account_page)
        else:
            print('wrong input name or object name')

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    # For Values of Dashboard page
    def dashboardPage(self):
        # show major
        self.user_sum_major.setText()
        # show concentration
        self.user_sum_con.setText()

        # show course category summery
        self.sum_general_com.setText()
        self.sum_general_rem.setText()
        self.sum_general_cre.setText()

        self.sum_core_com.setText()
        self.sum_core_rem.setText()
        self.sum_core_cre.setText()

        self.sum_selective_com.setText()
        self.sum_selective_rem.setText()
        self.sum_selective_cre.setText()

        self.sum_concent_com.setText()
        self.sum_concent_rem.setText()
        self.sum_concent_cre.setText()

        # degree plan summery
        self.sum_year.setText()
        self.sum_TotCredit.setText()

        # CGPA summery
        self.sum_coursesCom.setText()
        self.sum_CGPA.setText()

        # graduation summery
        self.sum_coursesCom.setText()
        self.sum_CGPA.setText()

        # estimate time
        self.sum_remSem2Grad.setText()

    # For Values of Degree Plan page
    def degreePlanPage(self):
        # show current degree plan
        self.dp_major.setText()
        self.dp_year.setText()
        self.dp_courses.setText()
        self.dp_credits.setText()

        # show Total Courses and Credits by Category
        self.dp_gen_courses.setText()
        self.dp_gen_credits.setText()
        self.dp_cor_courses.setText()
        self.dp_cor_credits.setText()
        self.dp_con_courses.setText()
        self.dp_con_credits.setText()

        # Configure Your Degree Plan
        self.config_degreeplan_major.text()
        self.config_degreeplan_year.text()
        self.config_degreeplan_concentration.text()
        self.config_degreeplan_credit.text()
        self.config_degreeplan_general.text()
        self.config_degreeplan_core.text()
        self.config_degreeplan_selective.text()
        self.config_degreeplan_concentration_credit.text()

        # buttons
        self.config_degreeplan_reset.clicked.connect()
        self.config_degreeplan_save.clicked.connect()

    # view data in table
    @staticmethod
    def view(widget_name):
        widget_name.setRowCount(0)

        for row_index, row_data in enumerate(db.cursor.fetchall()):
            widget_name.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                widget_name.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def coursesPage(self):
        # Add Courses
        self.course_input_ID.text()
        self.course_input_name.text()
        self.course_input_category.text()
        self.course_input_grade.text()
        self.course_input_credits.text()
        # buttons
        self.course_input_save.clicked.connect()
        self.course_input_reset.clicked.connect()

        # Edit/Delete Courses
        self.course_modify_search.text()
        # buttons: table ObjectName (course_modify_table)
        self.course_modify_reset.clicked.connect()
        self.course_modify_delete.clicked.connect()
        self.course_modify_save.clicked.connect()

    # For Values of Account page
    def accountPage(self):
        # show name, id, email
        self.account_page_user_title.setText()
        self.account_page_user_id.setText()
        self.accoun_page_user_email.setText()

        # show Credential Information
        self.account_page_credential_reveal.clicked.connect()
        self.account_page_credential_username.setText()
        self.account_page_credential_password.setText()

        # show Advisor Information
        self.account_page_advisor_name.setText()
        self.account_page_advisor_email.setText()

        # Configure Your Account
        self.config_account_name.text()
        self.config_account_lastname.text()
        self.config_account_email.text()
        self.config_account_id.text()
        self.config_account_username.text()
        self.config_account_password.text()
        self.config_account_advisor_name.text()
        self.config_account_advisor_email.text()

        # buttons
        self.config_account_reset.clicked.connect()
        self.config_account_save.clicked.connect()


app = QApplication(sys.argv)
user_interface = UserInterface()
user_interface.show()
app.exec()
=======
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        uic.loadUi('ui/main.ui', self)
        self.center_window()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


app = QApplication(sys.argv)
user_interface = UserInterface()
user_interface.show()
app.exec()
>>>>>>> upstream/main
