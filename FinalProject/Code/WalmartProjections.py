import arcpy

arcpy.env.workspace = "C:/Users/nrejd/OneDrive/Documents/Fall 2023 Semester/GEOG391/FinalProject/FinalProject/FinalProject.gdb"

arcpy.management.AddField("TIGER_tract", "WalmartTest", "FLOAT")

expression = "((incomeClass(!AOQIE001!) * 10) + (eduLevel(!PercentGrads!) * 9) + (countyPop(!Population!) * 8) + (tractPop(!total!) * 7) + (unemploymentClass(!UnemploymentPercent!) * 7) + (demoClass(!WhiteP!) * 5)) / 46"

codeblock = """
#66,825.5 is median income for Walmart
def incomeClass(income):
    if income >= 60000 and income <= 70000:
        return 10
    elif (income >= 50000 and income < 60000) or (income > 70000 and income <= 85000):
        return 7.32
    elif (income >= 40000 and income < 50000) or (income > 85000 and income <= 100000):
        return 4.66
    else:
        return 1

#14.38 percent is the median HS/College Graduation Rate for Walmart
def eduLevel(grads):
    if grads >= 11 and grads <= 19:
        return 10
    elif (grads >= 8 and grads < 11) or (grads > 19 and grads <= 25):
        return 7.32
    elif (grads >= 4 and grads < 8) or (grads > 25 and grads <= 30):
        return 4.66
    else:
        return 1

#822,779 is median county population for Walmart
def countyPop(pop):
    if pop >= 400000 and pop <= 1200000:
        return 10
    elif pop < 400000 or (pop > 1200000 and pop <= 1600000):
        return 7.32
    elif pop > 2500000 and pop <= 2000000:
        return 4.66
    else:
        return 1

#4,681.5 is median tract population for Walmart
def tractPop(pop):
    if pop >= 3900 and pop <= 5500:
        return 10
    elif (pop >= 3200 and pop < 3900) or (pop > 5500 and pop <= 6400):
        return 7.32
    elif (pop >= 2500 and pop < 3200) or (pop > 6400 and pop <= 7300):
        return 4.66
    else:
        return 1

#4.6 is median unemployment rate for Walmart
def unemploymentClass(unemp):
    if unemp >= 3.8 and unemp <= 6.1:
        return 10
    elif (unemp > 6.1 and unemp <= 7.6) or unemp < 3.8:
        return 7.32
    elif unemp > 7.6 and unemp <= 9.3:
        return 4.66
    else:
        return 1

#43.56 percent is median perecentage of Whites to Non Whites in Walmart Tracts
def demoClass(demo):
    if demo >= 28 and demo <= 56:
        return 10
    elif (demo >= 14 and demo < 28) or (demo > 56 and demo <= 68):
        return 7.32
    elif demo < 14 or (demo > 68 and demo <= 80):
        return 4.66
    else:
        return 1
        """

arcpy.management.CalculateField(
    "TIGER_tract", "WalmartTest", expression, "PYTHON3", codeblock
)
