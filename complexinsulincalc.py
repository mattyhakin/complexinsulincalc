#Creating a calculator in python to work out the amount of insulin to dose with
#currently my ratio's differ during different times of the day so want to make a 
#programme to do the maths for me. This version includes working out the
#correctional dose - if required based upon the current blood sugar readings
#and if any insulin was taken in the last 90 minutes

#Blood Sugar range
bs_min = 4
bs_max = 7

#Blood Sugar Correctional units
bs_mincorrect = -1
bs_maxcorrect = 1

#Ratio's for each type of meal/snack
breakfast = 2
lunch = 1.5
dinner = 1.5
snack = 1.5

#Asking for input of the meal time and setting the ratio
dose_type = input("What Type of Dose is it: ")

if dose_type == "Breakfast" or dose_type =="breakfast":
    ratio = breakfast

elif dose_type == "Lunch" or dose_type == "lunch":
    ratio = lunch

elif dose_type == "Dinner" or dose_type == "dinner":
    ratio = dinner

elif dose_type == "Snack" or dose_type == "snack":
    ratio = snack

else:
    print("Try again")

#Asking for input of how manu carbs are being dosed for
carbs = input("How Many Carbs are you eating: ")

#Working out the dose by multiplying the ratio and carbs then diving by 10 
#to get the insulin dose
dose = float(ratio) * float(carbs) / 10

#Asking for input of Blood Sugars to work out any correctional dose
bloodsugars = input("What is your current blood sugar reading? ")

#If Blood Suagrs are great then the max value adds correctional dose to
#the calculation
if float(bloodsugars) > bs_max:
    cordiff = float(bloodsugars) - float(bs_max)
    totalcorrect = float(cordiff) * float(bs_maxcorrect)
    totaldose = float(dose) + float(totalcorrect)

# If Blood Sugars are less than the min removes units of insulin from the dose
elif float(bloodsugars) < bs_min:
    cordiff = float(bs_min) - float(bloodsugars)
    totalcorrect = float(cordiff) * float(bs_mincorrect)
    totaldose = float(dose) + float(totalcorrect)

#If its between the max and min, it just uses the dose calulated eatlier
else:
    totaldose = dose

#Sets the dose to a round number
totaldose = round(totaldose)

#Prints the dose required based on the inputs
print("You Need " + str(totaldose) + " Units of Insulin")





