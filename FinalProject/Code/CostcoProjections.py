import arcpy

arcpy.env.workspace = "C:/Users/nrejd/OneDrive/Documents/Fall 2023 Semester/GEOG391/FinalProject/FinalProject/FinalProject.gdb"

arcpy.management.AddField("TIGER_tract", "CostcoTest", "FLOAT")

expression = "((incomeClass(!AOQIE001!) * 10) + (eduLevel(!PercentGrads!) * 9) + (countyPop(!Population!) * 8) + (tractPop(!total!) * 7) + (unemploymentClass(!UnemploymentPercent!) * 7) + (demoClass(!WhiteP!) * 5)) / 46"

codeblock = """
#75,208 is median income for Costco
def incomeClass(income):
    if income >= 65000 and income <= 85000:
        return 5
    elif (income >= 55000 and income < 65000) or income > 85000:
        return 3.66
    elif (income >= 45000 and income < 55000):
        return 2.33
    else:
        return 1

#20.95 percent is the median HS/College Graduation Rate for Costco
def eduLevel(grads):
    if grads >= 15:
        return 5
    elif grads >= 10 and grads < 15:
        return 3.66
    elif grads >= 5 and grads < 10:
        return 2.33
    else:
        return 1

#1,290,188 is median county population for Costco
def countyPop(pop):
    if pop >= 900000 and pop <= 1600000:
        return 5
    elif (pop >= 600000 and pop < 900000) or (pop > 1600000 and pop <= 1900000):
        return 3.66
    elif (pop >= 300000 and pop < 600000) or (pop > 1900000 and pop <= 2200000):
        return 2.33
    else:
        return 1

#5,256 is median tract population for Costco
def tractPop(pop):
    if pop >= 4200 and pop <= 6200:
        return 5
    elif (pop >= 3200 and pop < 4200) or (pop > 6200 and pop <= 7200):
        return 3.66
    elif (pop >= 2200 and pop < 3200) or (pop > 7200 and pop <= 8200):
        return 2.33
    else:
        return 1

#3.8 is median unemployment rate for Costco
def unemploymentClass(unemp):
    if unemp >= 2.8 and unemp <= 4.8:
        return 5
    elif (unemp > 4.8 and unemp <= 5.8) or (unemp >= 1.8 and unemp < 2.8):
        return 3.66
    elif (unemp > 5.8 and unemp <= 6.8) or (unemp >= 0.8 and unemp < 1.8):
        return 2.33
    else:
        return 1

#41.3 percent is median perecentage of Whites to Non Whites in Costco Tracts
def demoClass(demo):
    if demo >= 32 and demo <= 50:
        return 5
    elif (demo >= 23 and demo < 32) or (demo > 50 and demo <= 59):
        return 3.66
    elif (demo >= 14 and demo < 23) or (demo > 59 and demo <= 68):
        return 2.33
    else:
        return 1
        """

arcpy.management.CalculateField(
    "TIGER_tract", "CostcoTest", expression, "PYTHON3", codeblock
)
