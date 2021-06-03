import HTMLTestRunner
import unittest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


class MyUnit(unittest.TestCase):
    mylst=[]

    def setUp(self):
        self.mylst = [1, 2, 3]
        print("333333333")
    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("1111111")
    def test_case_list(self):
        self.assertEqual([1,2,3],self.mylst,"they are not equal")   # assert 断言
        print("2222222")

    def tearDown(self):
        self.mylst = None
        print("44444444")



def mysuite():
    suite=unittest.TestSuite()
    suite.addTest(MyUnit("test_case_num"))
    suite.addTest(MyUnit("test_case_list"))
    return suite

if __name__ == "__main__":
    filename = 'E:\\Testfun\\20181202\\tryunitest\\TestfanResult.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="报告结果",
    description="用例执行情况：")

    runner=unittest.TextTestRunner()
    runner.run(mysuite())

# 只需要改这些即可，开始
smtpserver = 'smtp.163.com'
username = 'xxx@163.com'
password = 'xxx'     # 设置客户端授权码 的 密码
sender = 'xxx@163.com'
# 收件人为多个收件人
receiver = ['xxx@163.com']
subject = "Lee's Report"
mailbody = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.testfan.cn\n\nThanks!"
attachfile = "smail.py"
# 只需要改这些即可，结束


msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'Lee <xxx@163.com>'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)


# 构造文字内容

text_plain = MIMEText(mailbody, 'plain', 'utf-8')
msg.attach(text_plain)


# 构造附件
sendfile = open(attachfile, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=attachfile)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
