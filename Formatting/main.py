#This is Lizzy Saldana's 'What are these numbers'? assignment

prompt = float(input("Pick a number between 1200-1400: "))

if prompt >=1200.00 and prompt<=1400.00:
    txt = "{:.4f}"
    print("Your number is also", txt.format(prompt))

    txt = "{:.0%}"
    print("You number is also", txt.format(prompt),)

    txt = "{:,}"
    print("You number is also", txt.format(prompt), "thousand")

    txt = "{:.2f}"
    print("Your number is also $", txt.format(prompt))
    prompt
else:
    print("Invalid, choose again.")