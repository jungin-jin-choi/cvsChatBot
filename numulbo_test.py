# -*- codiing : utf-8 -*-

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')

def Keyboard():
	dataSend = {
		"type" : "buttons",
		"buttons" : ["편의점 선택하기","도움말"]
	}
	return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']
	if content == u"편의점 선택하기":
		dataSend = {
			"message": {
				"text": "편의점 목록!\n1. CU\n2. GS25\n3. eMart24"
			}
		}
	elif content ==u"도움말":
		dataSend = {
			"text":"도움말"
		}
	elif u"CU" in content:
		dataSend ={
			"message":{
				"text": "찾고자 하는 CU 지점을 선택해주세요"
			}
		}
	elif u"GS25" in content:
		dataSend ={
			"message":{
				"text": "찾고자 하는 GS25 지점을 선택해주세요"
			}
		}
	elif u"eMart24" in content:
		dataSend ={
			"message":{
				"text": "찾고자 하는 eMart24 지점을 선택해주세요"
			}
		}
	return jsonify(dataSend)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
