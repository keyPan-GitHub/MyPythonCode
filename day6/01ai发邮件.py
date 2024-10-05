import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(sender_name: str, sender_email: str, password: str,
               recipient_email: str, subject: str, text: str) -> bool:
    """
    发送电子邮件的函数。
    :return:
    :param sender_name: 发件人姓名
    :param sender_email: 发件人邮箱地址
    :param password: 发件人邮箱密码
    :param recipient_email: 收件人邮箱地址
    :param subject: 邮件主题
    :param text: 邮件正文
    :return: 发送是否成功
    """
    ret = True
    try:
        # 创建邮件对象并设置内容
        msg = MIMEText(text, "plain", "utf-8")
        msg['From'] = formataddr([sender_name, sender_email])
        msg['To'] = formataddr(["Recipient", recipient_email])  # 可以根据需要修改收件人姓名
        msg['Subject'] = subject

        # 创建SMTP对象并发送邮件
        server = smtplib.SMTP("smtp.163.com", 25)  # 使用587端口以支持STARTTLS
        server.starttls()  # 加密连接
        server.login(sender_email, password)
        server.sendmail(sender_email, [recipient_email], msg.as_string())
        server.quit()

    except Exception as e:
        ret = False
        print(f"发送失败: {e}")

    return ret


# 使用环境变量来获取敏感信息，如邮箱密码
password = 'BITLECHVDDSIJIDA'  # 默认值为空字符串，生产环境中应配置为实际密码
if not send_email("潘新友", "13651220389@163.com", password,
                  "cyjzbmm@outlook.com", "测试邮件", "这是一封测试邮件"):
    print("邮件发送失败")
else:
    print("邮件发送成功")
