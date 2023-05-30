from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import data_required

FAI=Flask(__name__)

class NameForm(Form):
    sname=StringField(validators=([data_required()]))
    submit=SubmitField()

@FAI.route('/webforms',methods=['GET','POST'])
def Webforms():
    NFO=NameForm()

    if request.method=='POST':
        NFD=NameForm(request.form)
        if NFD.validate():
            return NFD.sname.data
    return render_template('webforms.html',NFO=NFO)

if __name__=='__main__':
    FAI.run(debug=True)
