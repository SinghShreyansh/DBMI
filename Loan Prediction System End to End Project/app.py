from logging import debug
from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict/', methods=['GET', 'POST'])

def predict():
    if request.method == 'POST':
        Gender = int(request.form.get('Gender'))
        Married = int(request.form.get('Married'))
        Education =  int(request.form.get('Education'))
        Self_Employed =  int(request.form.get('Self_Employed') )
        ApplicantIncome =  int(request.form.get('ApplicantIncome') )
        CoapplicantIncome =  int(request.form.get('CoapplicantIncome') )
        LoanAmount = float(request.form.get('LoanAmount'))
        Loan_Amount_Term =float( request.form.get('Loan_Amount_Term'))
        Credit_History =  float(request.form.get('Credit_History') )
        Property_Area =  int(request.form.get('Property_Area')  )

    prediction = utils.preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area)

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
