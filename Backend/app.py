
'''
Created on 
Course work: 
@author: 
Source:
    
'''
# Import necessary modules

from flask import Flask, request ,render_template
from utils import round_1q
from utils import Util

app = Flask(__name__)

utils = Util()



@app.route('/round1',methods=["GET","POST"])
def start():
      
    print(utils.update_round1())


    cur_round_1q = utils.update_round1()[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        "choice"    : cur_choices,
        "round_1q"     : cur_round_1q
        
        }

    return result
        # answer1 = request.args.get('answer',default='no')

@app.route('/round2-liver',methods=["GET","POST"])
def Round_2_liver():
      
    print(utils.update_round2_liver())


    cur_round_2q = utils.update_round2_liver()[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        
        "choice"    : cur_choices,
        "round_2q"     : cur_round_2q
        
    }

    return result

@app.route('/round2-lungs',methods=["GET","POST"])
def Round_2_lungs():
      
    print(utils.update_round2_Lungs())


    cur_round_2q = utils.update_round2_Lungs()[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        
        "choice"    : cur_choices,
        "round_2q"     : cur_round_2q
        
    }

    return result

@app.route('/round2-skin',methods=["GET","POST"])
def Round_2_skin():
      
    print(utils.update_round2_Skin())


    cur_round_2q = utils.update_round2_Skin()[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        
        "choice"    : cur_choices,
        "round_2q"     : cur_round_2q
        
    }

    return result

@app.route('/round2-blood',methods=["GET","POST"])
def Round_2_blood():
      
    print(utils.update_round2_Blood())


    cur_round_2q = utils.update_round2_Blood()[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        
        "choice"    : cur_choices,
        "round_2q"     : cur_round_2q
        
    }

    return result

@app.route('/round2-pancreas',methods=["GET","POST"])
def Round_2_pancreas():
      
    print(utils.update_round2_Pancreas())


    cur_round_2q = utils.update_round2_Pancreas[0]
    cur_choices = request.values.get("choice",default ='no')
   


    result = {
        
        "choice"    : cur_choices,
        "round_2q"     : cur_round_2q
        
    }

    return result
    







        





        

    
    


if __name__== "__main__":

    app.run(host="0.0.0.0", debug = True, port = 6003)

