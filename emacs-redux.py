from dvc import *

emacs_commands = List(
    "emacs-commands",

    "doxymacs find next func",
    "doxymacs font lock",
    "doxymacs insert blank multiline comment",
    "doxymacs insert blank singleline comment",
    "doxymacs insert file comment",
    "doxymacs insert function comment",
    "doxymacs insert grouping comments",
    "doxymacs insert member comment",
    "doxymacs lookup",
    "doxymacs mode",
    "doxymacs rescan tags",
    "doxymacs version",

    "hippie expand",
    "join line",
    "open line",

    "eval buffer",
    "eval expression",
    "load library",

    "recover this file",

    "replace buffer in windows",
    "replace rectangle",
    "replace regexp",
    "replace string",
    "server edit",
    "shell command",
    "shell command on region",
    "shell script mode",
    "scroll up",
    "scroll down",
    "linum mode",
    "snippet mode",
    )

dvc = DVC(

    "terminal-emacs.dvc",

    List("say-list", "yes", "no"),
    Script("say <say-list>", '_arg1 + "{Enter}"'),

    List("last", "last", "previous", "back"),
    List("next", "next", "forward", "jump", "right"),
    List("down", "next", "forward", "jump", "down"),
    List("back", "back", "previous", "left"),
    List("up",   "back", "previous", "up"),

    Keys("save", "{Ctrl+x}{Ctrl+s}"),
    Keys("kill emacs", "{Ctrl+x}{Ctrl+c}"),
    Keys("save and quit", "{Ctrl+x}{Ctrl+s}", "{Ctrl+x}{Ctrl+c}"),
    Keys("compile", MetaX("compile")),
    Keys("save compile", "{Ctrl+x}{Ctrl+s}", MetaX("recompile")),
    Keys("suspend emacs", "{Ctrl+x}{Ctrl+z}"),
    Keys("find file", "{Ctrl+x}{Ctrl+f}"),

    Keys("search", "{Ctrl+s}"),
    Keys("search again", "{Ctrl+s}{Ctrl+s}"),
    Keys("back search", "{Ctrl+r}"),
    Keys("back search again", "{Ctrl+r}{Ctrl+r}"),
    Keys("jump error", "{Ctrl+x}`"),
    Keys("next error", "{Ctrl+x}`"),

    Keys("other window", "{Ctrl+x}o"),
    Keys("scroll other", MetaX("scroll-other-window")),
    Keys("scroll up other", MetaX("scroll-other-window-down")),
    Keys("other end", MetaX("end-of-buffer-other-window")),

    Keys("repeat", "{Ctrl+x}z"),
    Keys("next line", "{Ctrl+n}"),
    Keys("kill this line", MetaX("kill-whole-line")),
    Keys("cancel", "{Ctrl+g}"),
    Keys("recenter", "{Ctrl+l}"),

    Keys("control slash", "{Ctrl+/}"),
    Keys("meta space", "{Esc}{Space}"),

    Keys("transpose words", MetaX("transpose words")), 
    Keys("transpose lines", MetaX("transpose lines")),
    Keys("line start", "{Ctrl+a}"),
    Keys("line end", "{Ctrl+e}"),
    Keys("end of line", "{Ctrl+e}"),
    Keys("yank", "{Ctrl+y}"),
    Keys("pop yank", MetaX("yank-pop")),
    Keys("yank pop", MetaX("yank-pop")),
    Keys("set mark", "{Ctrl+Space}"),

	Keys("copy to register", MetaX("copy-to-register")),
	Keys("insert register", MetaX("insert-register")),

	Script("copy to register <1to20>", '"{Esc}xcopy-to-register{Enter}" + _arg1 + "{Enter}"'),
	Script("insert register <1to20>", '"{Esc}xinsert-register{Enter}" + _arg1 + "{Enter}"'),
	
    Keys("<next> word", "{Alt+f}"),
    Keys("<back> word", "{Alt+b}"),
    Keys("<down> line", "{Ctrl+n}"),
    Keys("<up> line", "{Ctrl+p}"),    
    Script("<next> <1to20> words", '"{Ctrl+u}" + _arg2 + "{Alt+f}"'),
    Script("<back> <1to20> words", '"{Ctrl+u}" + _arg2 + "{Alt+b}"'),
    Script("<down> <1to20> lines", '"{Ctrl+u}" + _arg2 + "{Ctrl+n}"'),
    Script("<up> <1to20> lines", '"{Ctrl+u}" + _arg2 + "{Ctrl+p}"'),

    List("kill-list",
	 "buffer",
	 "this buffer",
	 "some buffers",
	 "compilation",
	 "whole line",
	 "grep"),
    Script("kill <kill-list>",
	   '"{Esc}xkill " + _arg1 + "{Enter}"'),

    List("mark-list",
	 "buffer",
	 "line",
	 "sentence",
	 "paragraph",
	 "word"),
    Script("mark <mark-list>",
	   '"{Esc}xmark " + _arg1 + "{Enter}"'),

    List("region-list", "region", "that"),
    List("region-command-list",
	 "kill",
	 "indent",
	 "comment",
	 "downcase",
	 "upcase"),
    Script("<region-command-list> <region-list>",
	   '"{Esc}x" + _arg1 + " region" + "{Enter}"'),
    Script("<region-command-list> <mark-list>",
	   '"{Esc}xmark " + _arg2 + "{Enter}" + ' +
	   '"{Esc}x" + _arg1 + " region" + "{Enter}"'),
    Script("replace <mark-list>",
	   '"{Esc}xmark " + _arg1 + "{Enter}" + ' +
	   '"{Esc}xreplace-string{Enter}"'),
    Script("copy <mark-list>",
	   '"{Esc}xmark " + _arg1 + "{Enter}" + ' +
	   '"{Alt+w}"'),
	   
    emacs_commands,
    Script("<emacs-commands>",
	   '"{Esc}x" + _arg1 + "{Enter}"'),

    List("undo-that", "undo", "undo that"),
    Keys("<undo-that>", "{Ctrl+/}"),
    Script("<undo-that> <1to20>",
		  '"{Ctrl+u}" + _arg2 + "{Ctrl+/}"'),

    Script("<next> tab", '"{Esc}xtabbar-forward{Enter}"'),
    Script("<back> tab", '"{Esc}xtabbar-backward{Enter}"'),

    List("go-to-line", "go to line", "line", "jump line"),
    Keys("<go-to-line>", "{Alt+g}"),
    Script(
	"<go-to-line> <1to20>",
	'"{Ctrl+u}" + _arg2 + "{Alt+g}"'
	),
    Script(
	"<go-to-line> <1to20> <0to9>",
	'"{Ctrl+u}" + _arg2 + _arg3 + "{Alt+g}"'
	),
    Script(
	"<go-to-line> <1to20> <0to9> <0to9>",
	'"{Ctrl+u}" + _arg2 + _arg3 + _arg4 + "{Alt+g}"'
	),

    Script(
	"repeat <1to20>",
	'"{Ctrl+u}" + _arg1 + "{Ctrl+x}z"'
	),

    Script(
	"kill <1to20>", 
	'"{Ctrl+u}" + Str$(_arg1) + "{Ctrl+d}"'
	),

    Keys("kill word", "{Alt+d}"),
    Script(
    	"kill <1to20> words", 
    	'"{Ctrl+u}" + Str$(_arg1) + "{Alt+d}"'
    	),
    
    Keys("kill <last> word", "{Esc}{Backspace}"),
    Script(
    	"kill <last> <1to20> words", 
    	'"{Ctrl+u}" + Str$(_arg2) + "{Esc}{Backspace}"'
    	),

    Script("kill <1to20> lines",
	   '"{Ctrl+u}" + Str$(_arg1) + "{Esc}xkill-whole-line{Enter}"'),

    Keys("<next> buffer", MetaX("next-buffer")),
    List("buffer-list", "compilation", "shell", "scratch"),
    Script("switch to <buffer-list>", '"{Ctrl+x}b*" + _arg1 + "*{Enter}"'),

    List(
	"1to20",
	*[i for i in range(1,21)]
	),

    List(
	"0to9",
	*[i for i in range(0,10)]
	),

    )

print dvc
