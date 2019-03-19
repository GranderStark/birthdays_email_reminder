import datetime
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

import schedule

import models
from app import App
from templates import FIRST_REMINDER_SUBJECT, FIRST_REMINDER_TEMPLATE


class ReminderProcesor:
    def get_nearest_birthday_user(self, users, supposed_date):
        result = []
        for u in users:
            day = u.birthday.day
            month = u.birthday.month
            if all(
                    (supposed_date.day == day,
                     supposed_date.month == month)
            ):
                result.append(u)
        return result

    def get_recipients(self, users, b_day_users):
        for index, u in enumerate(users):
            if u in b_day_users:
                users.pop(index)
        return users

    def first_reminder(self, users, today):
        """
        Первое напоминание всем, за исключением именнинника за неделю(7 дней, конфиг)
        и указанием супервайзера
        :param users:
        :param today:
        :return:
        """
        delta = app.config['scheduling']['first_reminder']
        delta_days = datetime.timedelta(days=delta)
        b_date = today + delta_days
        b_day_users = self.get_nearest_birthday_user(users, b_date)

        recipients = self.get_recipients(users, b_day_users)
        supervisor = self.get_first_supervisor(recipients, b_day_users)
        if supervisor and recipients and b_day_users:
            b_day_names = ', '.join([u.fio for u in b_day_users])
            subject = FIRST_REMINDER_SUBJECT.format(b_day_names=b_day_names)
            b_date_str = b_date.strftime('%d.%m')

            body = FIRST_REMINDER_TEMPLATE.format(
                b_date_str=b_date_str,
                b_day_names=b_day_names,
                supervisor_name=supervisor.fio
            )
            self.send(body, recipients, subject)

    def send(self, body, recipients, subject):

        email_user = app.config['email']['login']
        email_password = app.config['email']['password']
        email_address = app.config['email']['address']
        email_port = app.config['email']['port']

        sent_from = email_user
        to = [u.email for u in recipients]

        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sent_from
        msg['To'] = ", ".join(to)

        server = smtplib.SMTP_SSL(email_address, email_port)
        server.ehlo()
        server.login(email_user, email_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()

    def get_first_supervisor(self, queryset, b_day_users):
        res = None
        for u in queryset:
            if u.is_supervisor and u not in b_day_users:
                res = u
                break
        return res


class Run(App):
    def __init__(self):
        super().__init__()
        self.jobs = [
            ReminderProcesor().first_reminder
        ]

    def process(self):
        users = app.db_session.query(models.Users).all()
        today = datetime.date.today()
        for j in self.jobs:
            j(users, today)


if __name__ == '__main__':
    app = Run()
    schedule.every().day.at(app.config['schedule_time']).do(app.process)
    while True:
        schedule.run_pending()
        time.sleep(1)


