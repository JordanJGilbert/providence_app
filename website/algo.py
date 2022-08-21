def fasting_bg(basal_insulin, blood_glucose):
    if 100 <= blood_glucose <= 140:
        return "Insulin Dosage is still: " + str(basal_insulin)
    elif 141 <= blood_glucose <= 200:
        return "Updated Insulin Dosage: " + str(int(basal_insulin * 1.1))
    elif blood_glucose > 200:
        return "Updated Insulin Dosage: " + str(int(basal_insulin * 1.2))
    elif 80 <= blood_glucose <= 99:
        return "Updated Insulin Dosage: " + str(int(basal_insulin * .9))
    elif blood_glucose < 80:
        return "Updated Insulin Dosage: " + str(int(basal_insulin * .8))

def post_prandial_BG(prandial_insulin, blood_glucose, meal):
    if meal == "lunch":
        changed_meal = "Breakfast"
    elif meal == "dinner":
        changed_meal = "Lunch"
    elif meal == "bedtime":
        changed_meal = "Dinner"
    
    if 100 <= blood_glucose <= 150:
        return changed_meal + " prandial insulin dosage is still: " + str(prandial_insulin)
    elif 151 <= blood_glucose <= 200:
        return changed_meal + " prandial insulin dosage: " + str(max(int(prandial_insulin * 1.1), prandial_insulin + 2))
    elif blood_glucose > 200:
        return changed_meal + " prandial insulin dosage: " + str(max(int(prandial_insulin * 1.2), prandial_insulin + 3))
    elif 80 <= blood_glucose <= 99:
        return changed_meal + " prandial insulin dosage: " + str(min(int(prandial_insulin * .9), prandial_insulin - 2))
    elif blood_glucose < 80:
        return changed_meal + " prandial insulin dosage: " + str(min(int(prandial_insulin * .8), prandial_insulin - 3))