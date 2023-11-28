import arcpy

arcpy.env.workspace = "C:/Users/nrejd/OneDrive/Documents/Fall 2023 Semester/GEOG391/FinalProject/FinalProject/FinalProject.gdb"

arcpy.management.AddField("TIGER_tract", "SamsTest", "FLOAT")

expression = "((incomeClass(!AOQIE001!) * 10) + (eduLevel(!PercentGrads!) * 9) + (countyPop(!Population!) * 8) + (tractPop(!total!) * 7) + (unemploymentClass(!UnemploymentPercent!) * 7) + (demoClass(!WhiteP!) * 5)) / 46"

codeblock = """
#66,856 is median income for Sams
def incomeClass(income):
    if income >= 54000 and income <= 66000:
        return 5
    elif (income >= 43000 and income < 54000) or (income > 66000 and income <= 77000):
        return 3.66
    elif (income >= 32000 and income < 43000) or (income > 77000 and income <= 88000):
        return 2.33
    else:
        return 1

#17.15 percent is the median HS/College Graduation Rate for Sams
def eduLevel(grads):
    if grads >= 14 and grads <= 21:
        return 5
    elif (grads >= 11 and grads < 14) or (grads > 21 and grads <= 24):
        return 3.66
    elif (grads >= 8 and grads < 11) or grads > 24:
        return 2.33
    else:
        return 1

#906,422 is median county population for Sams
def countyPop(pop):
    if pop >= 600000 and pop <= 1200000:
        return 5
    elif (pop >= 300000 and pop < 600000) or (pop > 1200000 and pop <= 1500000):
        return 3.66
    elif (pop >= 150000 and pop < 300000) or (pop > 1500000 and pop <= 1800000):
        return 2.33
    else:
        return 1

#4,313 is median tract population for Sams
def tractPop(pop):
    if pop >= 3600 and pop <= 5000:
        return 5
    elif (pop >= 2900 and pop < 3600) or (pop > 5000 and pop <= 5700):
        return 3.66
    elif (pop >= 2200 and pop < 2900) or (pop > 5700 and pop <= 6400):
        return 2.33
    else:
        return 1

#4.8 is median unemployment rate for Sams
def unemploymentClass(unemp):
    if unemp >= 3.8 and unemp <= 5.8:
        return 5
    elif (unemp > 5.8 and unemp <= 6.8) or (unemp >= 2.8 and unemp < 3.8):
        return 3.66
    elif (unemp > 6.8 and unemp <= 7.8) or (unemp >= 1.8 and unemp < 2.8):
        return 2.33
    else:
        return 1

#33.43 percent is median perecentage of Whites to Non Whites in Sams Tracts
def demoClass(demo):
    if demo >= 25 and demo <= 43:
        return 5
    elif (demo >= 17 and demo < 25) or (demo > 43 and demo <= 53):
        return 3.66
    elif (demo >= 9 and demo < 17) or (demo > 53 and demo <= 63):
        return 2.33
    else:
        return 1
        """

arcpy.management.CalculateField(
    "TIGER_tract", "SamsTest", expression, "PYTHON3", codeblock
)
