
# coding: utf-8

# In[56]:

import pandas as pd

# In[57]:

##################################
#Load in the "cleaned" data #
##################################
df_communicable_diseases = pd.read_csv("communicable_and infectious_diseases_(2011-14).csv")
df_injuries = pd.read_csv("injury_data(2011-14).csv")
df_mental_health = pd.read_csv("Mental_Health_Data(2011-14).csv")
df_nutrition = pd.read_csv("Nutrition_Data(2011-14).csv")


# In[58]:

################################
# Drop unneeded attributes #
################################
del df_communicable_diseases["Zone"]
del df_communicable_diseases["Ecological Belt"]
del df_communicable_diseases["Development Region"]
del df_communicable_diseases["Year (BS)"]
del df_communicable_diseases["Indicator"]

del df_injuries["Zone"]
del df_injuries["Ecological Belt"]
del df_injuries["Development Region"]
del df_injuries["Year (BS)"]

del df_mental_health["Zone"]
del df_mental_health["Ecological Belt"]
del df_mental_health["Development Region"]
del df_mental_health["Year (BS)"]

del df_nutrition["Zone"]
del df_nutrition["Ecological Belt"]
del df_nutrition["Development Region"]
del df_nutrition["Year (BS)"]


df_communicable_diseases.columns = ["Name", "Year", "Indicator", "Value"]
df_injuries.columns = ["Name", "Year", "Indicator", "Value"]
df_mental_health.columns = ["Name", "Year", "Indicator", "Sub-Indicator", "Value"]
df_nutrition.columns = ["Name", "Year", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]


# In[59]:

disease_region_dict = {}
injury_region_dict = {}
def region_sort(row, c_disease_region_dict):
    if row["Name"] in c_disease_region_dict.keys(): 
        tempDict = c_disease_region_dict[row["Name"]]
        tempDict[row["Indicator"]] = row["Value"]
        c_disease_region_dict[row["Name"]] = tempDict
        
    else: 
        c_disease_region_dict[row["Name"]] = {row["Indicator"]: row["Value"]}
    return c_disease_region_dict

df_communicable_diseases[["Name","Indicator","Value"]].apply(lambda x: region_sort(x, disease_region_dict), axis=1)
df_injuries[["Name","Indicator","Value"]].apply(lambda x: region_sort(x, injury_region_dict), axis=1)


# In[60]:

mental_health_region_dict = {}
def mental_region_sort(row): 
    if (row["Indicator"] == "Mental Health related problems"):
        if row["Name"] in mental_health_region_dict.keys(): 
            tempDict = mental_health_region_dict[row["Name"]]
            tempDict[row["Sub-Indicator"]] = row["Value"]
            mental_health_region_dict[row["Name"]] = tempDict
        
        else: 
            mental_health_region_dict[row["Name"]] = {row["Sub-Indicator"]: row["Value"]}
        return mental_health_region_dict

df_mental_health[["Name", "Indicator", "Sub-Indicator", "Value"]].apply(lambda x: mental_region_sort(x), axis=1)        


# In[61]:

nutrition_region_dict = {}
def nutrition_region_sort(row): 
    if (row["Indicator"] == "Weighing Status according to age group (Repeated Visit)"):
        if row["Name"] in nutrition_region_dict.keys(): 
            tempDict = nutrition_region_dict[row["Name"]]
            tempDict[row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"] ] = row["Value"]
            nutrition_region_dict[row["Name"]] = tempDict
        
        else: 
            nutrition_region_dict[row["Name"]] = {(row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"] ): row["Value"]}
        return nutrition_region_dict

df_nutrition[["Name", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]].apply(lambda x: nutrition_region_sort(x), axis=1)


# In[62]:

disease_region_dict


# In[63]:

injury_region_dict


# In[64]:

mental_health_region_dict


# In[65]:

nutrition_region_dict

# =================================================== NODE JS SETUP ====================================================================
import json

web_dict = 
{
    disease   : disease_region_dict,
    injury    : injury_region_dict,
    mental    : mental_health_region_dict,
    nutrition : nutrition_region_dict
}


with open('data.json', 'w') as fp:
    json.dump(web_dict, fp)


