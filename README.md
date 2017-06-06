List out types of affliction
https://eng100d-project.herokuapp.com/list
  >>["disease", "injury", "mental_health", "nutrition", "oral_eye_health", "water"]

List out afflictions with underneath type of affliction
https://eng100d-project.herokuapp.com/list/{type of affliction}

  ex. https://eng100d-project.herokuapp.com/list/disease
  >>["STD/STI","HIV/AIDS","Leprosy","Confirmed Meningitis","ARI/Lower respiratory tract Infection","Upper respiratory tract Infection","Pneumonia","Sever Pneumonia","Bronchitis","Asthama","Urinary Track Infections (UTI)","Viral Influnenza","Reproductive Tract Infection (RTI) male","Reproductive Tract Infection (RTI) female","Tuberculosis","Malaria"]
  
List out districts affected by afflection
https://eng100d-project.herokuapp.com/list/{type of affliction}/{affliction}

  ex. https://eng100d-project.herokuapp.com/list/disease/HIV%2FAIDS
  >>["Taplejung","Panchthar","Ilam","Jhapa","Morang","Sunsari","Dhankuta","Teharthum","Sankhuwasabha","Bhojpur","Solukhumbu","Okhaldhunga", "Khotang","Udaypur","Saptari","Siraha","Dhanusha","Mahottari","Sarlahi","Sindhuli","Ramechhap","Dolkha","Sindhupalchowk","Kavre","Lalitpur","Bhaktapur","Kathmandu","Nuwakot","Rasuwa","Dhading","Makawanpur","Rautahat","Bara","Parsa","Chitwan","Gorkha","Lamjung","Tanahu","Syangja","Kaski","Manang","Mustang","Myagdi","Parbat","Baglung","Gulmi","Palpa","Nawalparasi","Rupandehi","Kapilvastu","Arghakhanchi","Pyuthan","Rolpa","Rukum","Salyan","Dang","Banke","Bardiya","Surkhet","Dailekh","Jajarkot","Dolpa","Jumla","Kalikot","Mugu","Humla","Bajura","Bajhang","Achham","Doti","Kailali","Kanchanpur","Dadeldhura","Baitadi","Darchula","Data"]

Get Info about district
https://eng100d-project.herokuapp.com/info/{type of affliction}/{affliction}/{district}

  ex. https://eng100d-project.herokuapp.com/info/disease/HIV%2FAIDS/Panchthar
  >> {"Latitude":27.2036401,"Longitude":87.8156715,"Value":0,"Year":"2013/14","File Name":"communicable_and infectious_diseases_(2011-14).csv"}

Get both rows and cols of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}

  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS
  >>{"cols":["Name","Year","Indicator","Value"],
     "rows":"[{\"Name\":\"Taplejung\",\"Year\":\"2011\\/12\",\"Indicator\":\"HIV\\/AIDS\",\"Value\":0},{\"Name\":\"Panchthar\",\"Year\":\"2011\\/12\",\"Indicator\":\"HIV\\/AIDS\",\"Value\":0}...]}

Get colss of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}/cols

  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS/cols
  >>["Name","Year","Indicator","Value"]

Get rows of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}/rows
  
  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS/rows
  >> [{\"Name\":\"Taplejung\",\"Year\":\"2011\\/12\",\"Indicator\":\"HIV\\/AIDS\",\"Value\":0},{\"Name\":\"Panchthar\",\"Year\":\"2011\\/12\",\"Indicator\":\"HIV\\/AIDS\",\"Value\":0}...]

