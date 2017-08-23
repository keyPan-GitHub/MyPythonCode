import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(p, text):
    ret = True
    try:
        msg = MIMEText(text, "plain", "utf-8")
        msg['From'] = formataddr(["潘新友", "13651220389@163.com"])
        msg['To'] = formataddr(["走人", "pxy1010995752@vip.qq.com"])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("13651220389@163.com", "pxy785378521")
        server.sendmail("13651220389@163.com", [p, ], msg.as_string())
        # server.sendmail()
        server.quit()

    except:
        # 如果出现错误自动执行except
        ret = False
        print("发送失败")
    return ret


email("pxy1010995752@vip.qq.com", "ok")
