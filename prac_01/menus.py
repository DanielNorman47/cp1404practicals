name = input("Enter your name: ")
choice = input("""(H)ello
(G)oodbye
(Q)uit
""")
while choice != 'Q':
   if choice == 'H':
       print(f"hello {name}")
   elif choice == 'G':
       print(f"Goodbye {name}")
   else:
        print("invalid choice")
   choice = input("""(H)ello
(G)oodbye
(Q)uit
""")
print("Finished.")