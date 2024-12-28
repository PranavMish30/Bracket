import bracket

# On booting up the shell:
print("\n<<< Bracket Shell >>>\n")
while True:
    text = input("<<>> ")
    result = bracket.run(text)
    for obj in result:
        print(obj.type,obj.value)
    
    