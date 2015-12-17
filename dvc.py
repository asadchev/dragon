def MetaX(line):
    return "{Esc}x%s{Enter}" % line

def Indent(n = 1):
    return "\n" + "    "*n

class List(list):
    def __init__(self, name, *args):
	self.name = name
	list.__init__(self, args)
    def __str__(self):
	return (
	    "LIST \"%s\" {" % self.name +
	    Indent(1) +
	    Indent(1).join("\"%s\"" % s for s in self) +
	    "\n}"
	    )

class Script(list):
    def __init__(self, name, *args):
	self.name = name
	list.__init__(self, args)
    def __str__(self):
	return (
	    "COMMAND \"%s\" {" % self.name +
	    Indent(1) + "SCRIPT {" + 
	    Indent(2) +
	    Indent(2).join("SendKeys %s" % s for s in self) +
	    Indent(1) + "}" +
	    "\n}"
	    )

class Keys(list):
    def __init__(self, name, *args):
	self.name = name
	list.__init__(self, args)
    def __str__(self):
	return (
	    "COMMAND \"%s\" {" % self.name +
	    Indent(1) + "KEYS {" + 
	    Indent(2) +
	    Indent(2).join(str(s) for s in self) +
	    Indent(1) + "}" +
	    "\n}"
	    )

class DVC(list):
    def __init__(self, menu, *args):
	self.menu = menu
	self.state = ""
	list.__init__(self, args)
    def __str__(self):
	unique = set()
	for e in self:
	    #print e.name
	    if e.name in unique:
		raise Exception("duplicate entry '%s'" % e.name)
	    unique.add(e.name)
	return (
	    "MENU \"%s\" {\n" % self.menu +
	    "STATE \"%s\" {\n" % self.state +
	    "\n" +
	    "\n\n".join(str(s) for s in self) +
	    "\n" +
	    "\n}" +
	    "\n}"
	    )
