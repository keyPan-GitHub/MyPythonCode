import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr\


def send_email(subject, content, to_address):
    try:
        # 创建一个MIMEText对象，用于封装邮件内容
        msg = MIMEText(content)
        # 设置邮件的主题
        msg['Subject'] = subject
        # 设置邮件的发件人信息
        msg['From'] = formataddr(['测试1', '13651220389@163.com'])
        # 设置邮件的收件人信息
        msg['To'] = formataddr(['测试2', to_address])

        # 创建一个SMTP对象，指定SMTP服务器和端口
        server = smtplib.SMTP('smtp.163.com', 25)
        # 启动TLS加密连接
        server.starttls()
        # 登录SMTP服务器
        server.login("13651220389@163.com", "BITLECHVDDSIJIDA")
        # 发送邮件
        server.sendmail("13651220389@163.com", [to_address], msg.as_string())
        # 关闭SMTP连接
        server.quit()
        # 返回成功标志
        return True
    except Exception as e:
        # 打印异常信息
        print(e)
        # 返回失败标志
        return False


send_email("test", "hello world", "cyjzbmm@outlook.com")
