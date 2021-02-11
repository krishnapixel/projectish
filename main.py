import bottle

@bottle.route("/")
def any_name():
  return bottle.static_file("index.html", root="")

'''@bottle.route("/plots.js")
def second():
 return bottle.static_file("plots.js", root="")'''

@bottle.route("/permitsByMonth")
def barGraph():
    return permitsByMonth()

'''@bottle.route("/permitsByYear")
def linegraph():
    return bottle.linegraph("appcode.py", root="")

@bottle.route("/permitsScatter")
def scatterGraph():
    return data.scatterGraph()'''

bottle.run(host="0.0.0.0", port=8080, debug=True)