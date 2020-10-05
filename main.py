
while True:
    options = input("\nConvert to [A]SCII or [T]ext: ").lower()
    if options == "a":
        word = input("Enter the text: ")
        converted_ascii = [ord(i) for i in word]
        print(f"Value of '{word}':", end=" ")
        for i in converted_ascii:
            if converted_ascii.index(i) != len(converted_ascii)-1:
                print(i, end=", ")
            else:
                print(i)

    elif options == "t":
        try:
            ascii = input("Enter the ASCII Value [seperated by (,)]: ")
            separate_ascii = ascii.split(",")
            converted_text = [chr(int(i)) for i in separate_ascii]
            for i in converted_text:
                print(i,end="")
        except ValueError:
            print("error!")
    else:
        print("Exiting the program")
        quit()