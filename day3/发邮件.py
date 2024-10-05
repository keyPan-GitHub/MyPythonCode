import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(p, text):
    # 初始化发送结果为成功
    ret = True
    try:
        # 创建一个MIMEText对象，设置邮件内容、格式和编码
        msg = MIMEText(text, "plain", "utf-8")

        # 设置邮件的发件人信息
        msg['From'] = formataddr(["潘新友", "13651220389@163.com"])

        # 设置邮件的收件人信息
        msg['To'] = formataddr(["潘新友", "cyjzbmm@outlook.com"])

        # 设置邮件的主题
        msg['Subject'] = "主题"

        # 创建一个SMTP对象，指定SMTP服务器和端口
        server = smtplib.SMTP("smtp.163.com", 25)

        # 登录SMTP服务器
        server.login("13651220389@163.com", "BITLECHVDDSIJIDA")

        # 发送邮件，指定发件人、收件人列表和邮件内容
        server.sendmail("13651220389@163.com", [p, ], msg.as_string())

        # 关闭SMTP连接
        #server.sendmail()
        server.quit()

    except:
        # 如果出现异常，将发送结果设置为失败
        # 如果没有出现错误自动执行except
        ret = False
        print("发送失败")

    return ret

email("cyjzbmm@outlook.com", "測試1")
