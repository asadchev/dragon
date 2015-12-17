from dvc import *

# linux.cmd = { "svn " : "S. V. N.",
# 	      "ssh" : "S. S. H.",
# 	      "git " : "",
# 	      "diff " : "",
# 	      "make " : "",
# 	      "emacs" : "",
# 	      "apt-get " : "apt get",
# 	      "apt-cache " : "apt cache",
# 	      "tar xf " : "tar X. F.",
# 	      "cd " : "C. D.",
# 	      "cd -" : "cd minus",
# 	      "grep -r " : "grep R.",
# 	      "fg {Enter}" : "G. F.",
# 	      "sudo " : "",
# 	      "ln -s " : "L. N. S.",
# 	      "tail -f " : "tail F.",
# 	      "rm " : "R. M."
# 	      }

# linux.dir = { "mkdir " : "make",
# 	      "ls " : "list",
# 	      "cd " : "change" }

# linux["make"] = [ "clean", "install", "upload" ]

# linux["svn"] = [  "add", "move", "remove",
# 		  "commit", "checkout", "update", "up"
# 		  "diff", "status", "log"
# 	       ]

# linux.pipe = [ "grep", "less", "head", "xargs", "cat", "tail", "awk" ]

# for (k,v) in linux.cmd.items(): script.append((v or k, k))

# for (k,v) in linux.items():
#     voice = linux.cmd.get(k + " ", None) or linux.cmd.get(k,k) or k
#     script.append(List(k, v))
#     script.append(("%s <%s>" % (voice,k), [k + " ", Argument(0), " "]))

# script.append(List("dir", linux.dir.values()))
# script.append(("<dir> dir",
# 		      Var("cmd", Argument(0)),
# 		      Transform(Var("cmd"), linux.dir), Var("cmd")))

# script.append(List("pipe", linux.pipe))
# script.append(("pipe <pipe>", ["| ", Argument(0)]))

dvc = DVC(
    
    "terminal-linux.dvc",

    Keys("equal quotes", '=""{Left}'),
    Keys("dollar parens", '$(){Left}'),

    List("commands",
	 "ssh",
	 "make",
	 "cmake",
	 "sudo",
	 "grep",
	 "less",
	 "head",
	 "tail",
	 "emacs",
	 "valgrind",
	 "gdb",
	 "tmux"
	 ),
    Script("<commands>", '_arg1 + " "'),

    List("apt-get", "remove", "install", "update", "upgrade"),
    Script("apt-get <apt-get>", '"apt-get " + _arg1 + " "'),
    

)

git = [
    "",
    "fetch",
    "fetch --all",
    "log",
    "clone",
    "branch",
    "commit",
    "commit --amend",
    "commit --all",
    "add",
    "push",
    "push --force",
    "pull",
    "checkout",
    "checkout --force",
    "diff",
    "reset",
    "reset --hard",
    "show",
    "rebase",
    "rebase --continue",
    "rebase --abort",
    "stash",
    "stash apply",
    "stash pop",
    "cherry-pick"
    ]

for cmd in git:
    cmd = "git %s " % cmd
    voice = cmd.replace("--", "")
    dvc.append(Keys(voice, cmd))



print dvc
