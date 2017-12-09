# -*- coding: utf-8 -*-
def register(username, password):
	ret = u"OCCUR ERROR IN REGISTER"
	uname_list = []
	pwd_list = []
	try:
		f = open('user_list.txt', 'r')
		for i in f.read().splitlines():
			uname_list.append(i.split('@')[0])
			pwd_list.append(i.split('@')[1])
		f.close()
	except Exception:
		print(u"读取user_list.txt错误")

	if username in uname_list:
		ret = u"该用户名已被注册"
	else:
		uname_list.append(username)
		pwd_list.append(password)
		try:
			f = open('user_list.txt', 'w+')
			for i in range(len(uname_list)):
				f.write(uname_list[i] + '@' + pwd_list[i] + '\n')
			f.close()
			ret = u"注册成功"
		except Exception, e:
			print(u"user_list.txt写入错误")

	sendData = {"response": ret}
	return sendData

# -*- coding: utf-8 -*-
def login(username, password):
	ret = u"OCCUR ERROR IN LOGIN"
	uname_list = []
	pwd_list = []
	try:
		f = open('user_list.txt', 'r')
		for i in f.read().splitlines():
			uname_list.append(i.split('@')[0])
			pwd_list.append(i.split('@')[1])
		f.close()
	except Exception:
		print(u"读取user_list.txt错误")

	if username not in uname_list:
		ret = u"该用户名不存在"
	else :
		for i in range(len(uname_list)):
			if uname_list[i] == username:
				ret = "登录成功" if pwd_list[i] == password else "登录失败 密码错误"
				break
	sendData = {"response": ret}
	return sendData