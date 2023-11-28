import arcpy

arcpy.env.workspace = "C:/Users/nrejd/OneDrive/Documents/Fall 2023 Semester/GEOG391/FinalProject/FinalProject/FinalProject.gdb"

arcpy.management.AddField("TIGER_tract", "TargetTest", "FLOAT")

expression = "((incomeClass(!AOQIE001!) * 10) + (eduLevel(!PercentGrads!) * 9) + (countyPop(!Population!) * 8) + (tractPop(!total!) * 7) + (unemploymentClass(!UnemploymentPercent!) * 7) + (demoClass(!WhiteP!) * 5)) / 46"

codeblock = """
#75,985 is median income for Target
def incomeClass(income):
    if income >= 65000 and income <= 85000:
        return 5
    elif (income >= 55000 and income < 65000) or (income > 85000 and income <= 95000):
        return 3.66
    elif (income >= 45000 and income < 55000) or (income > 95000 and income <= 105000):
        return 2.33
    else:
        return 1

#19.9 percent is the median HS/College Graduation Rate for Target
def eduLevel(grads):
    if grads >= 17 and grads <= 27:
        return 5
    elif (grads >= 14 and grads < 17) or (grads > 27 and grads <= 34):
        return 3.66
    elif (grads >= 10 and grads < 14) or grads > 34:
        return 2.33
    else:
        return 1

#1,290,188 is median county population for Target
def countyPop(pop):
    if pop >= 1000000 and pop <= 1900000:
        return 5
    elif (pop >= 800000 and pop < 1000000) or (pop > 1900000 and pop <= 2500000):
        return 3.66
    elif (pop >= 500000 and pop < 800000) or (pop > 2500000 and pop <= 3200000):
        return 2.33
    else:
        return 1

#4,528 is median tract population for Target
def tractPop(pop):
    if pop >= 3800 and pop <= 5500:
        return 5
    elif (pop >= 3000 and pop < 3800) or (pop > 5500 and pop <= 6500):
        return 3.66
    elif (pop >= 2200 and pop < 3000) or (pop > 6500 and pop <= 7500):
        return 2.33
    else:
        return 1

#4.8 is median unemployment rate for Target
def unemploymentClass(unemp):
    if unemp >= 3.8 and unemp <= 5.8:
        return 5
    elif (unemp > 5.8 and unemp <= 6.8) or (unemp >= 2.8 and unemp < 3.8):
        return 3.66
    elif (unemp > 6.8 and unemp <= 7.8) or unemp < 2.8:
        return 2.33
    else:
        return 1

#43.98 percent is median perecentage of Whites to Non Whites in Target Tracts
def demoClass(demo):
    if demo >= 34 and demo <= 52:
        return 5
    elif (demo >= 24 and demo < 34) or (demo > 52 and demo <= 60):
        return 3.66
    elif (demo >= 14 and demo < 24) or (demo > 60 and demo <= 68):
        return 2.33
    else:
        return 1
        """

arcpy.management.CalculateField(
    "TIGER_tract", "TargetTest", expression, "PYTHON3", codeblock
)
