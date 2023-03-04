from flask import Flask,request,jsonify
from mynn import MyFirst
app=Flask(__name__)
NN=MyFirst()
@app.route('/api/myfirstnn',methods=['GET','POST'])
def mynn():
    if request.method=='GET':
        return jsonify("this is my nn. developed by spoorthi shetty")
    else:
        input_json = request.json
        nn_input=input_json['input']
        output =NN.predict(nn_input)
        return jsonify(output)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8208)
