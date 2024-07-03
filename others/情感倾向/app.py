from flask import Flask, request, render_template
import pandas as pd
import pygwalker as pyg
import io
import base64
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        try:
            # 读取CSV文件
            data = pd.read_csv(file)
            
            # 使用 PyGWalker 生成图表
            walker = pyg.walk(data)
            
            # 将生成的图表保存为HTML字符串
            html_str = walker.to_html()
            
            # 将图表嵌入到结果页面
            return render_template('result.html', chart=html_str)
        except Exception as e:
            print(f"Error processing file: {e}")
            return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)