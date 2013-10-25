import urllib, csv , operator
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
    total = sum(out.values())
    print total
    for  key, val in out.items():
        out[key]= (out[key] /total)*100
    out = sorted(out.iteritems(), key=operator.itemgetter(1))[-5:]
    js_data = "var catalogLabels  = ["  +  ",".join(
                    ["\"%s\"" % str(x) for x, y in out]
    ) + "],\
    catalogDatas   = ["  +  ",".join(
                    [  str(y) for x, y in out]
    )   +   "]"
    
    open("js/catalog.js", "wb").write(js_data)
if __name__== "__main__":
  run()
  



    
    
  
