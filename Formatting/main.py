#This is Lizzy Saldana's 'What are these numbers'? assignment

prompt = int(input("Pick a number: "))

txt = "{:.4f}"
print(txt.format(prompt))

txt = "{:.0%}"
print(txt.format(prompt))

txt = "{:,}"
print(txt.format(prompt))

txt = "{:.2f}"
print("$", txt.format(prompt))