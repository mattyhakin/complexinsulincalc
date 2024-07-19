#Creating a calculator in python to work out the amount of insulin to dose with
#currently my ratio's differ during different times of the day so want to make a 
#programme to do the maths for me. This version includes working out the
#correctional dose - if required based upon the current blood sugar readings
#and if any insulin was taken in the last 90 minutes

BLOOD_SUGAR_MIN = 4
BLOOD_SUGAR_MIN_CORRECTION = -1
BLOOD_SUGAR_MAX = 7
BLOOD_SUGAR_MAX_CORRECTION = 1

DOSAGE_RATIO = {
'breakfast': 2,
'lunch': 1.5,
'dinner': 1.5,
'snack': 1.5,
}

def main():
prompt = f"What type of dose is it ({'/'.join(DOSAGE_RATIO.keys())}): "

while (dose_type := input(prompt).strip().lower()) not in DOSAGE_RATIO:
print("Try again")

ratio = DOSAGE_RATIO[dose_type]

carbs = float(input("How Many Carbs are you eating: "))

dose = ratio * carbs / 10

ninety_mins = input("Have you had a dose of insulin in the last 90 minutes?").strip().lower()
if ninety_mins == "yes":
print(f"You need {dose} units of insulin")
raise SystemExit

blood_sugar_level = float(input("What is your current blood sugar reading? "))

multiplier = 0
limit = 0

if BLOOD_SUGAR_MAX < blood_sugar_level:
    multiplier = BLOOD_SUGAR_MAX_CORRECTION
    limit = BLOOD_SUGAR_MAX
elif blood_sugar_level < BLOOD_SUGAR_MIN:
    multiplier = BLOOD_SUGAR_MIN_CORRECT
    limit = BLOOD_SUGAR_MIN
    
cordiff = blood_sugar_level - limit
correction = cordiff * multiplier
total_dose = round(dose + correction)

print(f"You need {total_dose} units of insulin")

if __name__ == '__main__':
main()
