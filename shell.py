import bracket

# On booting up the shell:
print("\n<<< Bracket Shell >>>\n")
while True:
    text = input("<<>> ")
    result = bracket.run(text)
    print(result)
    
    