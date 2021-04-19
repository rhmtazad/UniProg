import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from entities.student import Student
from entities.degreeplan import DegreePlan
from entities.courses import Courses


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        # setup a frameless window
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.verification_status = False

        uic.loadUi('ui/main.ui', self)

        self.center_window()

        self.button_handler()
        self.page_handler()
        self.oldPos = self.pos()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def user_is_verified(self):
        return self.verification_status

    def page_handler(self):
        self.show_login_page()
        self.signup_button.clicked.connect(self.show_signup_page)

        self.dashboard.clicked.connect(self.show_dashboard_page)
        self.degreeplan.clicked.connect(self.show_dp_page)
        self.courses.clicked.connect(self.show_course_page)
        self.account.clicked.connect(self.show_account_page)

        self.logout.clicked.connect(self.show_login_page)

    def button_handler(self):
        self.closeBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)
        self.config_account_save.clicked.connect(self.save_account)
        self.account_page_credential_reveal.clicked.connect(self.reveal_password)
        self.config_degreeplan_save.clicked.connect(self.save_dp)
        self.course_input_save.clicked.connect(self.save_new_course)
        self.course_modify_reset.clicked.connect(self.update_courses_page)
        self.course_modify_delete.clicked.connect(self.remove_course)
        self.course_modify_save.clicked.connect(self.update_course)
        self.course_search_button.clicked.connect(self.search_courses)
        self.login_button.clicked.connect(self.verify_user)
        self.signup_create_account.clicked.connect(self.create_account)

    def verify_user(self):
        user_login_id = self.user_id_input.text()
        user_login_password = self.password_input.text()

        try:
            if user_login_password == student.file.get(user_login_id, 'password'):
                self.show_dashboard_page()
                self.verification_status = True
                global user_id
                user_id = user_login_id
            else:
                self.show_verification_failed_message()

        except KeyError:
            self.show_verification_failed_message()

    @staticmethod
    def show_verification_failed_message():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Wrong User ID or Password")
        msg.setWindowTitle("Verification Failed!")
        msg.exec()

    def show_login_page(self):
        self.verification_status = False
        self.page_manager.setCurrentWidget(self.login_page)

    def show_signup_page(self):
        self.page_manager.setCurrentWidget(self.signup_page)

    def create_account(self):
        name = self.signup_name.text()
        lastname = self.signup_lastname.text()
        email = self.signup_lastname.text()
        global user_id
        user_id = self.signup_id.text()
        username = self.signup_username.text()
        password = self.signup_password.text()
        advisor = self.signup_advisor_name.text()
        advisor_email = self.signup_advisor_email.text()

        student.file.insert(
            user_id,
            [
                user_id,
                name,
                lastname,
                email,
                username,
                password,
                advisor,
                advisor_email
            ]

        )
        self.verification_status = True
        self.show_dashboard_page()

    def show_dashboard_page(self):
        if self.user_is_verified():
            self.page_manager.setCurrentWidget(self.dashboard_page)
            self.update_dashboard()

    def show_dp_page(self):
        if self.user_is_verified():
            self.page_manager.setCurrentWidget(self.degreeplan_page)
            self.update_dp_page()

    def show_course_page(self):
        if self.user_is_verified():
            self.page_manager.setCurrentWidget(self.courses_page)
            self.update_courses_page()

    def show_account_page(self):
        if self.user_is_verified():
            self.page_manager.setCurrentWidget(self.account_page)
            self.update_account_page()

    def update_dashboard(self):
        # user fullname, major and concentration
        self.user_sum_fullname.setText(student.full_name)
        self.user_sum_major.setText(dp.major)
        self.user_sum_con.setText(dp.conc)

        # degree plan summery
        self.sum_year.setText(dp.year)
        self.sum_TotCredit.setText(f'{dp.credits} Credits, {dp.courses} Courses')

        # general category summary
        taken_gen = courses.gen_status['True']
        remaining_gen = courses.gen_status['False']
        self.sum_general_com.setText(str(taken_gen))
        self.sum_general_rem.setText(str(remaining_gen))
        self.sum_general_cre.setText(str(taken_gen * 3))

        # core category summary
        taken_core = courses.core_status['True']
        remaining_core = courses.core_status['False']
        self.sum_core_com.setText(str(taken_core))
        self.sum_core_rem.setText(str(remaining_core))
        self.sum_core_cre.setText(str(taken_core * 3))

        # concentration category summary
        taken_conc = courses.conc_status['True']
        remaining_conc = courses.conc_status['False']
        self.sum_concent_com.setText(str(taken_conc))
        self.sum_concent_rem.setText(str(remaining_conc))
        self.sum_concent_cre.setText(str(taken_conc * 3))

        # CGPA summary
        self.sum_coursesCom.setText(str(courses.taken_status['True']))

        # estimated graduation time
        self.sum_remSem2Grad.setText(str(courses.remaining_semesters))
        self.sum_CGPA.setText(courses.gpa)

    def update_account_page(self):
        # show name, id, email
        self.account_page_user_title.setText(student.full_name)
        self.account_page_user_id.setText(student.user_id)
        self.accoun_page_user_email.setText(student.email)

        # show credential information
        self.account_page_credential_username.setText(student.username)
        self.account_page_credential_password.setText("##############")

        # show advisor information
        self.account_page_advisor_name.setText(student.advisor)
        self.account_page_advisor_email.setText(student.advisor_email)

    def reveal_password(self):
        self.account_page_credential_password.setText(student.password)

    def save_account(self):
        student.name = self.config_account_name.text()
        student.lastname = self.config_account_lastname.text()
        student.email = self.config_account_email.text()
        student.user_id = str(self.config_account_id.text())
        student.username = self.config_account_username.text()
        student.password = self.config_account_password.text()
        student.advisor = self.config_account_advisor_name.text()
        student.advisor_email = self.config_account_advisor_email.text()

        student.save()
        self.update_account_page()

    def update_dp_page(self):
        # show current degree plan
        self.dp_major.setText(dp.major)
        self.dp_conc.setText(dp.conc)
        self.dp_year.setText(dp.year)
        self.dp_courses.setText(dp.courses)
        self.dp_credits.setText(dp.credits)

        # show total courses and credits by category
        self.dp_gen_courses.setText(str(dp.gen_courses))
        self.dp_gen_credits.setText(str(dp.gen_credits))
        self.dp_cor_courses.setText(str(dp.core_courses))
        self.dp_cor_credits.setText(str(dp.core_credits))
        self.dp_con_courses.setText(str(dp.conc_courses))
        self.dp_con_credits.setText(str(dp.conc_credits))

    def save_dp(self):
        dp.major = self.config_degreeplan_major.text()
        dp.year = self.config_degreeplan_year.text()
        dp.conc = self.config_degreeplan_concentration.text()
        dp.credits = self.config_degreeplan_credit.text()
        dp.gen_credits = self.config_degreeplan_general.text()
        dp.core_credits = self.config_degreeplan_core.text()
        dp.conc_credits = self.config_degreeplan_concentration_credit.text()

        dp.save()
        self.update_dp_page()

    def update_courses_page(self):
        table = self.course_modify_table
        table.setRowCount(0)

        for row_index, row_data in enumerate(courses.read()):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def search_courses(self):
        search_term = str(self.course_modify_search.text())
        self.updated_course_table(search_term, 'id')

    def updated_course_table(self, search_term, column):
        table = self.course_modify_table
        table.setRowCount(0)

        for row_index, row_data in enumerate(courses.search(search_term, column)):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

    def save_new_course(self):
        course_id = self.course_input_ID.text()
        name = self.course_input_name.text()
        category = self.course_input_category.text()
        credit = self.course_input_credits.text()
        grade = self.course_input_grade.text()
        taken = self.course_input_taken_status.text()

        courses.save(
            [
                course_id,
                name,
                category,
                credit,
                taken,
                grade
            ]
        )
        self.update_courses_page()

    def selected_row(self):
        table = self.course_modify_table
        selected_item = table.currentRow()
        column_count = table.columnCount()
        return [table.item(selected_item, column).text() for column in range(0, column_count)]

    def remove_course(self):
        courses.delete(self.selected_row()[0])
        self.update_courses_page()

    def update_course(self):
        courses.update(
            self.selected_row(),
            self.selected_row()[0]
        )
        self.update_courses_page()


user_id = '#38786'
major = 'Information Technology'

student = Student(user_id)
dp = DegreePlan(major)
courses = Courses()

app = QApplication(sys.argv)
user_interface = UserInterface()
user_interface.show()
app.exec()
