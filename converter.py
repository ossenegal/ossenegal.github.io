import urllib, csv
url= "https://raw.github.com/ossenegal/ossenegal.github.io/master/survey/2012.csv"
def run():
    r = urllib.urlopen(url)
    reader = csv.DictReader(r, dialect=csv.excel,
                            delimiter=",")
    out ={}
    for dic in reader:
      print dic
      for key in dic.keys() :
        try:
            x = float(dic[key])
        except (ValueError ,TypeError):
            continue
        if key in out:
            out[key] = float(out[key]) + float(dic[key])
        else:
            out[key] = float(dic[key])
    print out
    """
    {'iPad': 21.850000000000001, 'SymbianOS': 72.699999999999989, 'Windows': 1626.47
    , 'iPod': 16.390000000000001, 'iOS': 157.0, 'Autre': 39.43, 'BlackBerry': 13.110
    000000000001, 'iPhone': 26.57, 'Linux': 317.94999999999993, 'Android': 117.91, '
    Windows Phone': 3.96, 'Macintosh': 186.65999999999997}
    """
    # Format for js
    # create js file like this
    # var DataSet: [
    #    {
    #      "x": "Pepperoni",
    #      "y": 12
    #    },
    #    {
    #      "x": "Cheese",
    #      "y": 8
    #   }
    # ]
    tpl ="""
    {
         "x": "%s",
         "y": %s
    } ,"""
    js_data = "var DataSet=\
            [ \
    "
    for  key, value in out.items():
        js_data  =  js_data + tpl % (key, value)
    import re
    js_data = re.sub(",$", "]", js_data )
    print js_data
    open("js/catalog.js", "wb").write(js_data)
if __name__== "__main__":
  run()
  



    
    
  
