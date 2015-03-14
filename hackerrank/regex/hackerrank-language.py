languages = ["C", "CPP", "JAVA", "PYTHON", "PERL", "PHP", "RUBY", "CSHARP",
             "HASKELL", "CLOJURE", "BASH", "SCALA", "ERLANG", "CLISP", "LUA",
             "BRAINFUCK", "JAVASCRIPT", "GO", "D", "OCAML", "R", "PASCAL",
             "SBCL", "DART", "GROOVY", "OBJECTIVEC"]

t = int(raw_input())

for case in range(t):
    n, l = (x for x in raw_input().split())
    if l in languages:
        print "VALID"
    else:
        print "INVALID"
