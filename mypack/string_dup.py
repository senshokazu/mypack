#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re

def operation_num():
	
	start_num_list=[]
	step_num_list=[]
	Input_list=[]

	print('ループ処理回数を入力してください')
	ite_num=input()
	print('次に、最初の複製したい文字列を入力してください')
	input_string=input()
	#inputで入力された文字列は改行コードが無視される
	input_string=input_string.replace('\\n','\n')
	Input_list.append(input_string)
	print('開始の値を入力してください')
	start_num_list.append(input())
	print('ステップ値を入力してください')
	step_num_list.append(int(input()))
	print('0埋めフォーマットは有効にしますか?有効にしたい場合は1を入力してください')
	zero_format=input()
	if zero_format=='1':
		print('有効桁数を入力してください')
		effective_digit=input()

	while (True):
		print('文字列を続けて入力してください。終了したい場合は@finish')
		input_string=input()
		if input_string=='@finish':
			break
		else:
			input_string=input_string.replace('\\n','\n')
			Input_list.append(input_string)

		print('開始の値を入力してください。終了したい場合は@finish')
		input_string=input()
		if input_string=='@finish':
			break
		else:
			start_num_list.append(input_string)

		print('ステップ値を入力してください')
		step_num_list.append(int(input()))


	str_list=list(range(int(ite_num)))
	line=''
	if zero_format=='1':
		if len(effective_digit)==1:
			param='{0:0'+effective_digit+'d}'
		else:
			param='{0:'+effective_digit+'d'

		for i in range(0,int(ite_num)):
			try:
				for j in range(len(Input_list)):
					temp=param.format(int(start_num_list[j]))
					line+=Input_list[j]+temp
					start_num_list[j]  =int(start_num_list[j])
					start_num_list[j] +=step_num_list[j]
			except IndexError:
				line+=Input_list[j]

			str_list[i]=line
			line=''
	else:
		for i in range(0,int(ite_num)):
			try:
				for j in range(len(Input_list)):
					line+=Input_list[j]+str(start_num_list[j])
					start_num_list[j]  =int(start_num_list[j])
					start_num_list[j] +=step_num_list[j]
			except IndexError:
				line+=Input_list[j]

			str_list[i]=line
			line=''
			
	str_list=''.join(str_list)
	file=codecs.open('sample.txt','w','utf-8')
	file.writelines(str_list)
	file.close()