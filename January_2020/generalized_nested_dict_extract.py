"""
Output:
{
  'Washington, DC, USA': ('227 mi', '3 hours 54 mins'), 'Philadelphia, PA, USA': ('94.6 mi', '1 hour 44 mins'), 
  'Santa Barbara, CA, USA': ('2,878 mi', '1 day 18 hours'), 'Miami, FL, USA': ('1,286 mi', '18 hours 43 mins'), 
  'Austin, TX, USA': ('1,742 mi', '1 day 2 hours'), 'Napa County, CA, USA': ('2,871 mi', '1 day 18 hours')
}
"""
inp = {
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",
    "Miami, FL, USA",
    "Austin, TX, USA",
    "Napa County, CA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,286 mi",
          "value": 2069031
        },
        "duration": {
          "text": "18 hours 43 mins",
          "value": 67405
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,742 mi",
          "value": 2802972
        },
        "duration": {
          "text": "1 day 2 hours",
          "value": 93070
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,871 mi",
          "value": 4620514
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 152913
        },
        "status": "OK"
      }
    ]
  }],
  "status": "OK"
}

def extract_outer(dict_obj,key):
    lis = []

    def extract_inner_rec(dict_obj,lis,key):
        if isinstance(dict_obj,dict):
            for k,v in dict_obj.items():
                if isinstance(v,(dict,list)):
                    extract_inner_rec(v,lis,key)
                elif k == key:
                    lis.append(v)
        elif isinstance(dict_obj,list):
            for item in dict_obj:
                extract_inner_rec(item,lis,key)
        return lis
    results = extract_inner_rec(dict_obj, lis, key)
    return results

out_lis = extract_outer(inp,"text")
print(dict(zip(inp["destination_addresses"],list(zip(out_lis[::2],out_lis[1::2])))))
