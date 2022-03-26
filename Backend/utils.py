'''
Created on 
Course work: Cancer prognosis
@author: 
Source:
    
'''
# Import necessary modules
import json
import random







#constants


#getting data from json file



with open('questions.json') as f:
   questions = json.load(f)



round_1q = (questions['Round_1'])
round_2q = (questions['Round_2'])
round_3q = (questions['Round_3'])
round_2q_Liver = (round_2q['Liver'])
round_2q_Pancreas = (round_2q['Pancreas'])
round_2q_Lungs = (round_2q['Lungs'])
round_2q_Skin = (round_2q['Skin'])
round_2q_Leukemia = (round_2q['Leukemia'])
round_3q_Liver = (round_3q['Liver'])
round_3q_Pancreas = (round_3q['Pancreas'])
round_3q_Lungs = (round_3q['Lungs'])
round_3q_Skin = (round_3q['Skin'])
round_3q_Leukemia = (round_3q['Leukemia'])    


class Util():
     
         def __init__(self):
             
             self.count = 0 
             self.round = 0
             self.round_count = 0
             self.choices = ["yes",
             "no"]
             self.correct_choice = ["yes"]
      
             

         def round_1(self,inp):  

           for i in range(0,10): 
            inp = inp.casefold()
            round_count = 0 
            correct = False 
            if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               correct = True

           if (self.count>=3):
               liver(self,inp_1)

           else:
              # return correct
              print(self.count)

         def liver(self,inp):
            for i in range(0,4): 
             inp = inp.casefold()
             self.count = 0 
             self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               self.correct = True


            if(self.count>=2):
               round_3_liver()

            else:
              lungs(self,inp)
            

         def lungs(self,inp):
            for i in range(0,3): 
             inp = inp.casefold()
             self.count = 0 
             self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True


            if(self.count>=2):
               round_3_lungs()

            else:
              pancreas(self,inp)

         def pancreas(self,inp):
            for i in range(0,3): 
             inp = inp.casefold()
             self.count = 0 
             self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True


            if(self.count>=2):
               round_3_pancreas()

            else:
              skin(self,inp)

        

         def skin(self,inp):
            for i in range(0,4): 
             inp = inp.casefold()
             self.count = 0 
             self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

            if(self.count>=2):
               round_3_skin()

            else:
              blood(self,inp)


         def blood(self,inp):
            for i in range(0,3): 
             inp = inp.casefold()
             self.count = 0 
             self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

            if(self.count>=2):
               round_3_blood()

            else:
              return self.correct

         def round_3_liver(self,inp):
             for i in range(0,10): 
              inp = inp.casefold()
              self.count = 0 
              self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

             return self.count

         def round_3_lungs(self,inp):
             for i in range(0,10): 
               inp = inp.casefold()
               self.count = 0 
               self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

             return self.count

         def round_3_skin(self,inp):
             for i in range(0,10): 
               inp = inp.casefold()
               self.count = 0 
               self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

             return self.count

         def round_3_pancreas(self,inp):
             for i in range(0,10): 
               inp = inp.casefold()
               self.count = 0 
               self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

             return self.count

         def round_3_blood(self,inp):
             for i in range(0,10): 
               inp = inp.casefold()
               self.count = 0 
               self.correct = False 
             if (inp == self.correct_choice.casefold()):
               self.count += 1
               round_count += 1
               self.correct = True

             return self.count
   
         def update_round1(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

               self.round_1q = random.choice(questions['Round_1'])
              #  self.round_2q = (questions['Round_2'])
              #  self.round_3q = (questions['Round_3'])
              #  self.round_2q_Liver = (round_2q['Liver'])
              #  self.round_2q_Pancreas = (round_2q['Pancreas'])
              #  self.round_2q_Lungs = (round_2q['Lungs'])
              #  self.round_2q_Skin = (round_2q['Skin'])
              #  self.round_2q_Leukemia = (round_2q['Leukemia'])
              #  self.round_3q_Liver = (round_3q['Liver'])
              #  self.round_3q_Pancreas = (round_3q['Pancreas'])
              #  self.round_3q_Lungs = (round_3q['Lungs'])
              #  self.round_3q_Skin = (round_3q['Skin'])
              #  self.round_3q_Leukemia = (round_3q['Leukemia'])    

              #  self.choices = random.choice(self.choices)

               return self.round_1q ,self.choices

         def update_round2_liver(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

          
               self.round_2q_Liver = random.choice(round_2q['Liver'])
               return self.round_2q_Liver ,self.choices
           
         def update_round2_Lungs(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

          
               self.round_2q_Lungs = random.choice(round_2q['Lungs'])
               return self.round_2q_Lungs ,self.choices

         def update_round2_Pancreas(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

          
               self.round_2q_Skin = random.choice(round_2q['Pancreas'])
               return self.round_2q_Liver ,self.choices

         def update_round2_Skin(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

          
               self.round_2q_Skin = random.choice(round_2q['Skin'])
               return self.round_2q_Liver ,self.choices

         def update_round2_Blood(self):

               self.choices = [
                 "yes",
                 "no"
                 ]

          
               self.round_2q_Blood = random.choice(round_2q['Blood'])
               return self.round_2q_Blood ,self.choices
           

     
    
            




              

         
             

            
             
             



  