import yagmail
import random
import re
import time
import eventlet


def open_file():
    try:
        with open('mail_address_list.txt', 'r', encoding='utf8') as f:
            txt_contents = f.read()
            mail_address_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",
                                           txt_contents)  # 打开同名文件夹下的mail_address_list.txt文件并读取
        return mail_address_list
    except FileNotFoundError:
        print("目录没有'mail_address_list.txt'文件，请检查。")  # 若没有邮箱地址文件则报错


def mail_setting():
    mail_subject = "Cooperation on Water Pumps / A 25-year Pump Factory from China"  # 定义邮件title

    contents = ["""Dear Manager,
        Taixin Pump Industry Co., Ltd. here, a 25-year water pump factory in China, exporting high-quality pumps at a good and affordable price. 
        We're glad to hear that you're on the market for water pumps I am wondering if I have the opportunity to become your water pump supplier.
    
        There are a variety of types of pump and our main products are:
        1. Submersible pump 
        2. Sewage pump 
        3. Cutting pump 
        4. Jet pump 
        5. Intelligent pump
        6. DC pump
        I hope to be a partner of your company! We're sure your inquiry or requirement will get prompt attention. Come back for detail.
    
        Best regards
    
        name 
        Taixin Pump Industry Manufacture CO., LTD
        Website: www.taixinpump.com
        E-mail: mail_address
        Phone: 13586273052
        WeChat: yyyj0721""", """Dear Sir or Madam,
    
        It is a 25-year water pump factory from China. We would like to introduce our products, hope that we may build business cooperation in the future.
        
        There are a variety of types of pump and our main products are:
        1. Submersible pump 
        2. Sewage pump 
        3. Cutting pump 
        4. Jet pump 
        5. Intelligent pump
        6. DC pump
        I hope to be a partner of your company! We're sure your inquiry or requirement will get prompt attention. Come back for detail.
        
        Best regards
        
        name 
        Taixin Pump Industry Manufacture CO., LTD
        Website: www.taixinpump.com
        E-mail: mail_address
        Phone: 13586273052
        WeChat: yyyj0721
    """, """Hi Sir/Madam,
    
        Glad to hear that you're on the market for pumps, we specialize in this field for 25 years, with the strength of SUBMERSIBLE&SEWAGE&INTELLIGENT PUMP.
        
        Also, we have our own professional products to meet any of your requirements.
        
        Should you have any questions, call me, let's talk details.
        
        Best regards!
        name 
        Taixin Pump Industry Manufacture CO., LTD
        Website: www.taixinpump.com
        E-mail: mail_address
        Phone: 13586273052
        WeChat: yyyj0721""", """Hi, Manager.
    
        Good day!
        
        We are a water pump supplier, and we specialize in this field for more than 25 years. 
        
        The main production submersible, sewage, cutting, and intelligent self-priming pump.
        
        If you are interested in it, I 'll send you our catalog.
        
        Thanks for your valuable time.
        
        Regards.
        
        name 
        Taixin Pump Industry Manufacture CO., LTD
        Website: www.taixinpump.com
        E-mail: mail_address
        Phone: 13586273052
        WeChat: yyyj0721""", """Hi friend,
    
        Hopefully, this email doesn't cause you any inconvenience.
        
        Briefly introduce our strengths:
        
        1. 25 years' water pump factory with a variety of pumps
        
        2. Strong at OEM
        
        3. Sample ready in 2 days, fast delivery time 20 days
        
        4. Strong at submersible&sewage&DC&intelligent self-priming pump
        
        We are confident that our products will make a compliment to your business and improve your values to the biggest. For your sake, why not choose one more support?
        
        Anyway..hope we can get your soonest reply!
        
        Best regards.
        
        name 
        Taixin Pump Industry Manufacture CO., LTD
        Website: www.taixinpump.com
        E-mail: mail_address
        Phone: 13586273052
        WeChat: yyyj0721""", ]

    mail_username_list = ['taixinpump.olivia@gmail.com', 'taixin.aaron@gmail.com', 'taixinpump.lucy@gmail.com',
                          'taixinpump.bob@gmail.com', 'taixinpump.zhong@gmail.com', 'taixinpump.daniel@gmail.com']
    mail_username = random.choice(mail_username_list)  # 随机取邮箱
    mail_password = 'Qaz!@#6388987'
    random_contents = random.choice(contents)  # 随机取contents
    pattern = re.compile('.*?\.(.*?)@.*?', re.S)
    name = " ".join(re.findall(pattern, mail_username))  # 提取congtents中的发件人姓名
    name1 = name.capitalize()
    final_content = random_contents.replace('name', name1).replace('mail_address', mail_username)  # 替换contents中的人名及邮箱地址
    return mail_username, mail_password, mail_subject, final_content


if __name__ == '__main__':
    try:
        mail_address_list = open_file()  # 从txt文件中取出邮箱地址
        print("开始执行程序:"
              "此次邮件共计：" + str(len(mail_address_list)) + "封")
        eventlet.monkey_patch()
        for value, address in enumerate(mail_address_list):
            with eventlet.Timeout(100, False): # 设置100秒的超时继续
                mail_setting()  # 每发一封邮件执行一次random，重置username，contents
                mail_username = mail_setting()[0]
                mail_password = mail_setting()[1]
                subject = mail_setting()[2]
                final_content = mail_setting()[3]
                yag = yagmail.SMTP(user=mail_username, password=mail_password)  # 将邮箱参数传入yagmail
                yag.send(to=address, subject=subject, contents=final_content)
                print("%s，已由%s发给%s。 正在发送第下一条。。" % (value + 1, mail_username, address))
            continue
        print("发送完毕。")
    except TypeError:
        print("没有返回邮箱地址参数，请检查。")  # 若没有邮箱地址传入则报错
