# GET REQUESTS #

List out types of affliction
https://eng100d-project.herokuapp.com/list
  >>
  ```
  [
    "disease", 
    "injury", 
    "mental_health", 
    "nutrition"
    ...
  ]
  ```
List all afflictions
https://eng100d-project.herokuapp.com/list/all
  >>
  ```
  [
    {
      "type": "disease",
      "affliction": "ARI/Lower respiratory tract Infection",
      "name": "ARI/Lower respiratory tract Infection",
      "date": 1497093051529,
      "views": 0,
      "description": "ARI/Lower respiratory tract Infection",
      "source": "OpenNepal",
      "uploader": "Original"
    },
    {
      "type": "disease",
      "affliction": "Asthama",
      "name": "Asthama",
      "date": 1497093051529,
      "views": 0,
      "description": "Asthama",
      "source": "Original"
    },...
  ]
```
List out afflictions with underneath type of affliction
https://eng100d-project.herokuapp.com/list/{type of affliction}

  ex. https://eng100d-project.herokuapp.com/list/disease
  >>
  ```
  [
    "ARI/Lower respiratory tract Infection",
    "Asthama",
    "Bronchitis",
    "Confirmed Meningitis",
    "HIV/AIDS",
    "Leprosy",
    "Pneumonia",
    ...
  ]
  ```
See Full Affliction Profile
https://eng100d-project.herokuapp.com/list/{type of affliction}/{affliction}
```
NOTE: Replace "/" with %2F
```
  ex. https://eng100d-project.herokuapp.com/list/disease/HIV%2FAIDS
  >>
  ```
{
    "Data": {
      "cols": [
        "Name",
        "Year",
        "Value",
        "Latitude",
        "Longtitude"
      ],
      "rows": "[ {\"0\":\"Taplejung\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.6257485,\"Longitude\":87.7763333},                
                {\"0\":\"Panchthar\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.2036401,\"Longitude\":87.8156715},
               ...]"
    },
    "info": {
    "name": "HIV/AIDS",
    "date": 1497093051529,
    "views": 0,
    "description": "HIV/AIDS",
    "source": "OpenNepal",
    "uploader": "Uploader"
    }
}
```
Get info of affliction
https://eng100d-project.herokuapp.com/info/{type of affliction}/{affliction}

  ex.  https://eng100d-project.herokuapp.com/info/disease/HIV%2FAIDS
>>
```
{
    "name": "HIV/AIDS",
    "date": 1497503262232,
    "views": 0,
    "description": "HIV/AIDS",
    "source": "OpenNepal",
    "uploader": "Original"
}
```

Get both rows and cols of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}

  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS
>>
```
{
  "cols": [
    "Name",
    "Year",
    "Value",
    "Latitude",
    "Longtitude"
  ],
  "rows": "[
            {\"0\":\"Taplejung\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.6257485,\"Longitude\":87.7763333},
            {\"0\":\"Panchthar\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.2036401,\"Longitude\":87.8156715}
            ...]"
}
```

Get cols of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}/cols

  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS/cols
  >>
  ```
  [
    "Name",
    "Year",
    "Value",
    "Latitude",
    "Longtitude"
  ]
  ```

Get rows of affliction
https://eng100d-project.herokuapp.com/data/{type of affliction}/{affliction}/rows
  
  ex. https://eng100d-project.herokuapp.com/data/disease/HIV%2FAIDS/rows
  >>
```
  "[
    {\"0\":\"Taplejung\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.6257485,\"Longitude\":87.7763333},
    {\"0\":\"Panchthar\",\"1\":\"2013\\/14\",\"2\":0,\"Latitude\":27.2036401,\"Longitude\":87.8156715},
    {\"0\":\"Ilam\",\"1\":\"2013\\/14\",\"2\":6,\"Latitude\":26.9111769,\"Longitude\":87.9236747},
    ...
  ]"
```

# POST REQUEST #
Edit Column Labels
https://eng100d-project.herokuapp.com/edit/cols/{type of affliction}/{affliction}
>> Send JSON in this format:
```
[
  "COLUMN_1_NAME",
  "COLUMN_2_NAME",
  "COLUMN_3_NAME",
  ...
]
```

Edit Rows of an Affliction
https://eng100d-project.herokuapp.com/edit/rows/{type of affliction}/{affliction}
>> Send JSON in this format:
```
{			
  "0": "NAME"
  "1": "YEAR"
  "2": "VALUE"
  "index": "INDEX_IN_ROW_ARRAY"
}
```

Edit Info of Affliction
https://eng100d-project.herokuapp.com/edit/info/{type of affliction}/{affliction}
>> Send JSON in this format:
```
NOTE date is calculated with 
var d=new Date();
var n=d.getTime();
```
```
{
  "name":"NAME",
  "date":"DATE",
  "views":"NUMBER_OF_VIEWS",
  "description":"SOME_DESCRIPTION",
  "source": "SOME_SOURCE",
  "uploader":"SOME_UPLOADER"
}
```

Edit the type of an Affliction
https://eng100d-project.herokuapp.com/edit/type/{type of affliction}/{affliction}
>> Send JSON in this format:
```
{
  "type": "NEW_TYPE"
}
```

Add Row to the Table of an Affliction
https://eng100d-project.herokuapp.com/add/row/{type of affliction}/{affliction}
>> Send JSON in this format:
```
{
  "0":"NAME_OF_DISTRICT",
  "1":"YEAR_OF_DATASET",
  "2":"VALUE",
  "Latitude":"LATITUDE_OF_DISTRICT",
  "Longitude":"LONGITUDE_OF_DISTRICT"
}
```
edit Data field
https://eng100d-project.herokuapp.com/edit/data{type of affliction}/{affliction}
>> Send JSON in this format:
```
{
  info:{
    "name":"X",
    "date":Y,
    "views":Z,
    "description":"new description",
    "source":"source",
    "uploader":"SOME_UPLOADER"
  },
  Data:{
    cols:[col1,col2,col3...],
    rows:[
      {
        "0":Name,
        "1":Year,
        "2":Value,
        "Latitude":Lat,
        "Longitude":Long
      },
      {
        "0":Name,
        "1":Year,
        "2":Value,
        "Latitude":Lat,
        "Longitude":Long
      },
      ...
    ]
  }
}
```
Add a new affliction
https://eng100d-project.herokuapp.com/add/affliction/{type of affliction}
>> Send JSON in this format:

```
{
    "name":"NAME_OF_AFFLICTION",
    "description": "DESCRIPTION_OF_AFFLICTION"
}
```
Delete Aflliction
https://eng100d-project.herokuapp.com/delete/affliction/{type of affliction}
>> Send JSON in this format:
```
{}
```
