# -*- coding:utf-8 -*-
"输入身高体重，返回国内国外标准的体制"
"BMI = 体重（kg） / 身高（m*m）"

weight = eval(input("请输入您的体重"))
height = eval(input("请输入您的身高"))
print("您的体重为",weight,"kg，您的身高为",height,"cm")

'''
'国内的标准'
"偏廋":18.5,"正常":24,"偏胖":28
"偏廋":18.5,"正常":25,"偏胖":30
'''

'获取 MBI 值'
BMI = weight / pow(height,2)
print(BMI)
'与标准进行比较'
if BMI < 18.5:
    who,nat = "偏廋","偏廋"
elif 18.5 < BMI < 24:
    who,nat = "正常","正常"
elif 24 < BMI < 25:
    who,nat = "偏胖","正常"
elif 25 < BMI < 28:
    who, nat = "偏胖", "偏胖"
elif 28 < BMI < 30:
    who, nat = "偏胖", "肥胖"
else:
    who,nat = "肥胖","肥胖"
print("您的 BMI 在中国标准下为{0},在非中国标准下为{1}".format(who,nat))