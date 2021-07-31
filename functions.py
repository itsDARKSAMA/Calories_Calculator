## This Application was Designed and Coded by : Abdulrahman Almajayda
## Since : 13/7/2021
## GitHub : GitHub.com/itsDaRKSAMA

## To Do check input values , 
## The height must be 100cm at least,
## The weight must be 30kg at least,
## The age must be 13 years at least.


# a.almajayda : The calories calculation functions class
class CaloriesCalculator:

    # a.almajayda : Generate Activity
    def __generateActivity(self,activity):
        if activity == "/no": return float(1.2)
        elif activity == "1-2": return float(1.4)
        elif activity == "2-3": return float(1.6)
        elif activity == "4-5": return float(1.75)
        elif activity == "6-7": return float(2.0)
        else: return float(2.3)

    # a.almajayda : Men Calories Calculate 
    def menCalc(self,height,weight,age,activity):
        # a.almajayda : BMR Calculate by using Mifflin - St Jeor equation
        bmr = (10 * weight / 1 + 6.25 * height / 1 - 5 * age / 1 + 5)
        return round(self.__generateActivity(activity) * bmr)

    # a.almajayda : Women Calories Calculate
    def womenCalc(self,height,weight,age,activity):
        # a.almajayda : BMR Calculate by using Mifflin - St Jeor equation
        bmr = (10 * weight / 1 + 6.25 * height / 1 - 5 * age / 1  - 161)
        return round(self.__generateActivity(activity) * bmr)

    # a.almajayda : To Gain and To Lose Calories Calculate
    def get_ToGain(self,calories): return(calories + 500)
    def get_ToLose(self,calories): return(calories - 500)

    
    def get_BMI(self,height_m,weight):
        # a.almajayda : BMI Calculate by using Adolphe Quetelet equation
        result = round(weight / (height_m ** 2),1)
        if result <= 16          : return f"Your BMI : {result}\nSevere Thinness","Severe"
        elif 16 < result <= 17   : return f"Your BMI : {result}\nModerate Thinness","Moderate"
        elif 17 < result <= 18.5 : return f"Your BMI : {result}\nMild Thinness","Mild"
        elif 18.5 < result <= 25 : return f"Your BMI : {result}\nNormal","Normal"
        elif 25 < result <= 30   : return f"Your BMI : {result}\nOverweight","Overweight"
        elif 30 < result <= 35   : return f"Your BMI : {result}\nObese Class I","ObeseI"
        elif 35 < result <= 40   : return f"Your BMI : {result}\nObese Class II", "ObeseII"
        else                     : return f"Your BMI : {result}\nObese Class III" , "ObeseIII"