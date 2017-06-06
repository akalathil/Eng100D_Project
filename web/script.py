
import pandas as pd
import requests

##################################
#Load in the "cleaned" data #
##################################
df_communicable_diseases = pd.read_csv("../python/communicable_and infectious_diseases_(2011-14).csv")
df_injuries = pd.read_csv("../python/injury_data(2011-14).csv")
df_mental_health = pd.read_csv("../python/Mental_Health_Data(2011-14).csv")
df_nutrition = pd.read_csv("../python/Nutrition_Data(2011-14).csv")
df_oral_eye = pd.read_csv("../python/Oral_Eye_Health_Data(2011-14).csv")
df_tuberculosis = pd.read_csv("../python/Tuberculosis_Health_Data(2012-13).csv")
df_malaria = pd.read_csv("../python/Malaria_Health_Data(2013-14).csv")
df_water = pd.read_csv("../python/Water_Sanitation(2011).csv")
#test=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=Achham&key=AIzaSyAOTrmHFjUxiO8JUs8gqZReTxjFJ1W-9TY")
#print(test.json()['results'][0]['geometry']['location'])

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

del df_oral_eye["Zone"]
del df_oral_eye["Ecological Belt"]
del df_oral_eye["Development Region"]
del df_oral_eye["Year (BS)"]
del df_oral_eye["Indicator"]


del df_tuberculosis["Zone"]
del df_tuberculosis["Ecological Belt"]
del df_tuberculosis["Development Region"]
del df_tuberculosis["Year (BS)"]
del df_tuberculosis["Indicator"]
df_tuberculosis.columns = ["Name", "Year", "Sub-Indicator1", "Sub-Indicator2", "Sub-Indicator3", "Value"]
del df_tuberculosis["Sub-Indicator2"]
del df_tuberculosis["Sub-Indicator3"]

del df_malaria["Zone"]
del df_malaria["Ecological Belt"]
del df_malaria["Development Region"]
del df_malaria["Year (BS)"]
del df_malaria["Indicator"]

del df_water["Zone"]
del df_water["Geographical Region"]
del df_water["Development Region"]


df_communicable_diseases.columns = ["Name", "Year", "Indicator", "Value"]
df_injuries.columns = ["Name", "Year", "Indicator", "Value"]
df_mental_health.columns = ["Name", "Year", "Indicator", "Sub-Indicator", "Value"]
df_nutrition.columns = ["Name", "Year", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]
df_oral_eye.columns = ["Name", "Year", "Indicator", "Value"]
df_malaria.columns = ["Name", "Year", "Sub-Indicator1", "Sub-Indicator2", "Value"]
df_water.columns = ["Name", "Indicator", "Value"]
df_tuberculosis = df_tuberculosis.dropna()
df_mental_health.ix[df_mental_health["Sub-Indicator"] == "Dipression", "Sub-Indicator"] = "Depression"
df_water = df_water[df_water["Indicator"] == "Sanitation Coverage (%"]

region_loc_dict ={}
disease_region_dict = {}
injury_region_dict = {}
oral_eye_disease_dict = {}
def region_lat_long_sort(row):
    loc_data={}
    if row["Name"] not in region_loc_dict.keys():
        req_loc=row["Name"].replace(" ","+")
        req=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+req_loc+"+,+Nepal"+"&key=AIzaSyBRUomBHcNNVN6Zb219Ty1eDkDlNQXzsIE")        
        loc_data=req.json()['results'][0]['geometry']['location']
        region_loc_dict[row["Name"]] = loc_data

def region_sort(row, c_disease_region_dict, file_name):
    info_dict = {}
    region_lat_long_sort(row)
    if row["Indicator"] in c_disease_region_dict.keys(): 
        tempDict = c_disease_region_dict[row["Indicator"]]
        info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
        info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
        info_dict["Value"] = row["Value"]
        info_dict["Year"] = row["Year"]
        info_dict["File Name"] = file_name
        tempDict[row["Name"]] = {"info": info_dict}
        
        c_disease_region_dict[row["Indicator"]] = tempDict
        
    else: 
        info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
        info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
        info_dict["Value"] = row["Value"]
        info_dict["Year"] = row["Year"]
        info_dict["File Name"] = file_name
        t_dict = {"info": file_name}
        c_disease_region_dict[row["Indicator"]] = {row["Name"]: t_dict}
    return c_disease_region_dict

df_communicable_diseases[["Name", "Year", "Indicator","Value"]].apply(lambda x: region_sort(x, disease_region_dict, "communicable_and infectious_diseases_(2011-14).csv"), axis=1)
df_injuries[["Name", "Year", "Indicator","Value"]].apply(lambda x: region_sort(x, injury_region_dict, "injury_data(2011-14).csv"), axis=1)
df_oral_eye[["Name","Year", "Indicator","Value"]].apply(lambda x: region_sort(x, oral_eye_disease_dict, "Oral_Eye_Health_Data(2011-14).csv"), axis=1)

#Adding Tuberculosis Data to Disease Dict
tDict = {}
def add_tuberculosis(row, file_name):
    info_dict = {}
    if row["Sub-Indicator1"] == "Total":
        info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
        info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
        info_dict["Value"] = row["Value"]
        info_dict["Year"] = row["Year"]
        info_dict["File Name"] = file_name
        tDict[row["Name"]] = {"info": info_dict}
        #tempDict["Data"] = df_tuberculosis.loc(df_tuberculosis["Sub-Indicator1"] == "Total")
        disease_region_dict["Tuberculosis"] = tDict
df_tuberculosis[["Name", "Year", "Sub-Indicator1", "Value"]].apply(lambda x: add_tuberculosis(x, "Tuberculosis_Health_Data(2012-13).csv"), axis=1)
dft = df_tuberculosis.loc[df_tuberculosis["Sub-Indicator1"] == "Total"]
disease_region_dict["Tuberculosis"]["Data"] = {"cols": list(dft.columns.values)}
disease_region_dict["Tuberculosis"]["Data"]["rows"] = dft.to_json(orient="records")
#Adding Malaria Data to Disease Dict
mDict = {}
def add_malaria(row, file_name):
    info_dict = {}
    total = 0
    if (row["Sub-Indicator1"] == "Total"):
        if (row["Sub-Indicator2"] == "Female"):
            total = row["Value"]
        else:
            total = total + row["Value"]
            info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
            info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
            info_dict["Value"] = total
            info_dict["Year"] = row["Year"]
            info_dict["File Name"] = file_name
            mDict[row["Name"]] = {"info": info_dict}
            disease_region_dict['Malaria'] = mDict
df_malaria[["Name", "Year", "Sub-Indicator1", "Sub-Indicator2", "Value"]].apply(lambda x: add_malaria(x, "Malaria_Health_Data(2013-14).csv"), axis=1)
dfma = df_tuberculosis.loc[df_malaria["Sub-Indicator1"] == "Total"]
disease_region_dict["Malaria"]["Data"] = {"cols": list(dfma.columns.values)}
disease_region_dict["Malaria"]["Data"]["rows"] = dfma.to_json(orient="records")
#Adding Mental Health Data
mental_health_region_dict = {}
def mental_region_sort(row, file_name):
    info_dict = {}
    region_lat_long_sort(row)
    if (row["Indicator"] == "Mental Health related problems"):
        if row["Sub-Indicator"] in mental_health_region_dict.keys(): 
            tempDict = mental_health_region_dict[row["Sub-Indicator"]]
            info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
            info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
            info_dict["Value"] = row["Value"]
            info_dict["Year"] = row["Year"]
            info_dict["File Name"] = file_name
            tempDict[row["Name"]] = {"info": info_dict}
            mental_health_region_dict[row["Sub-Indicator"]] = tempDict
        
        else:
            info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
            info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
            info_dict["Value"] = row["Value"]
            info_dict["Year"] = row["Year"]
            info_dict["File Name"] = file_name
            t_dict = {"info": info_dict}
            mental_health_region_dict[row["Sub-Indicator"]] = {row["Name"]: t_dict}
        return mental_health_region_dict

df_mental_health[["Name", "Year", "Indicator", "Sub-Indicator", "Value"]].apply(lambda x: mental_region_sort(x, "Mental_Health_Data(2011-14).csv"), axis=1) 
df = df_mental_health.loc[df_mental_health["Indicator"] == "Mental Health related problems"]

#Adding Nutrition Data
nutrition_region_dict = {}
def nutrition_region_sort(row, file_name): 
    info_dict = {}
    region_lat_long_sort(row)
    if (row["Indicator"] == "Weighing Status according to age group (Repeated Visit)"):
        if (row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"]) in nutrition_region_dict.keys(): 
            tempDict = nutrition_region_dict[row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"]]
            info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
            info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
            info_dict["Value"] = row["Value"]
            info_dict["Year"] = row["Year"]
            info_dict["File Name"] = file_name
            tempDict[row["Name"]] = {"info": info_dict}
            nutrition_region_dict[row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"]] = tempDict
        
        else: 
            info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
            info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
            info_dict["Value"] = row["Value"]
            info_dict["Year"] = row["Year"]
            info_dict["File Name"] = file_name
            t_dict = {"info": info_dict}
            nutrition_region_dict[row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"]] = {row["Name"]: t_dict}
        return nutrition_region_dict

df_nutrition[["Name", "Year", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]].apply(lambda x: nutrition_region_sort(x, "Nutrition_Data(2011-14).csv"), axis=1)
dfn = df_nutrition.loc[df_nutrition["Indicator"] == "Weighing Status according to age group (Repeated Visit)"]

#Adding Water Sanitation Data
water_dict = {}
def water_region_sort(row, file_name): 
    info_dict ={}
    region_lat_long_sort(row)
    info_dict["Latitude"] = (region_loc_dict.get(row['Name'])).get('lat')
    info_dict["Longitude"] = (region_loc_dict.get(row['Name'])).get('lng')
    info_dict["Value"] = row["Value"]
    info_dict["Year"] = "2011"
    info_dict["File Name"] = file_name
    t_dict = {"info": info_dict}
    water_dict[row["Name"]] = {row["Name"]: t_dict}
df_water[["Name", "Value"]].apply(lambda x: water_region_sort(x, "Water_Sanitation(2011).csv"), axis=1)

#Inserting Data Json Value
def add_data_disease(indicator):
    tempDict = disease_region_dict[indicator]
    df = (df_communicable_diseases.loc[df_communicable_diseases['Indicator'] == indicator])
    tempDict["Data"] = {"cols": list(df_communicable_diseases.columns.values)}
    tempDict["Data"]["rows"] = df.to_json(orient="records")
df_communicable_diseases["Indicator"].apply(lambda x: add_data_disease(x))

def add_data_injury(indicator):
    tempDict = injury_region_dict[indicator]
    df = (df_injuries.loc[df_injuries['Indicator'] == indicator])
    tempDict["Data"] = {"cols": list(df_injuries.columns.values)}
    tempDict["Data"]["rows"] = df.to_json(orient="records")
df_injuries["Indicator"].apply(lambda x: add_data_injury(x))

def add_data_oral_eye(indicator):
    tempDict = oral_eye_disease_dict[indicator]
    df = (df_oral_eye.loc[df_oral_eye['Indicator'] == indicator])
    tempDict["Data"] = {"cols": list(df_oral_eye.columns.values)}
    tempDict["Data"]["rows"] = df.to_json(orient="records")
df_oral_eye["Indicator"].apply(lambda x: add_data_oral_eye(x))

def add_data_mental_health(indicator):
    tempDict = mental_health_region_dict[indicator]
    dfm = (df.loc[df['Sub-Indicator'] == indicator])
    tempDict["Data"] = {"cols": list(df.columns.values)}
    tempDict["Data"]["rows"] = dfm.to_json(orient="records")
df["Sub-Indicator"].apply(lambda x: add_data_mental_health(x))

def add_data_nutrition(row):
    iD = (row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"])
    tempDict = nutrition_region_dict[iD]
    df = (dfn.loc[(dfn['Sub-Indicator1'] + ", " + dfn['Sub-Indicator2'])  == (row["Sub-Indicator1"] + ", " + row["Sub-Indicator2"])])
    tempDict["Data"] = {"cols": list(dfn.columns.values)}
    tempDict["Data"]["rows"] = df.to_json(orient="records")
dfn[["Sub-Indicator1", "Sub-Indicator2"]].apply(lambda x: add_data_nutrition(x), axis=1)

def add_water_data(name):
    tempDict = water_dict[name]
    df = (df_water.loc[df_water['Name'] == name])
    tempDict["Data"] = {"cols": list(df_water.columns.values)}
    tempDict["Data"]["rows"] = df.to_json(orient="records")
df_water["Name"].apply(lambda x: add_water_data(x))

disease_region_dict

injury_region_dict

mental_health_region_dict

nutrition_region_dict

region_loc_dict

oral_eye_disease_dict

water_dict


# =================================================== NODE JS SETUP ====================================================================
import json

web_dict = {
   "disease"         : disease_region_dict,
   "injury"          : injury_region_dict,
   "mental_health"   : mental_health_region_dict,
   "nutrition"       : nutrition_region_dict, 
   "oral_eye_health" : oral_eye_disease_dict, 
   "water"           : water_dict
}


with open('data.json', 'w') as fp:
    json.dump(web_dict, fp)
