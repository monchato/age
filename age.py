alcohol = input('你有買過酒嗎:')
if alcohol != '有' and alcohol != '沒有':
	print('只能輸入有或沒有哦~')
	raise SystemExit

age = input('你今年幾歲:')
if alcohol == '有':

		if int(age) < 18:
			print('未成年請勿喝酒')
		elif int(age) >= 18:
			print('別喝太多餒~')
	

if alcohol == '沒有':
	if int(age) < 18:
		print('你很乖')
	elif int(age) >= 18:
		print('開喝了阿在等什麼?')
	
