def interactive_help():
    while True:
        # Prompt the user to enter a command
        command = input("Enter a command to see the manual (type 'END' to exit): ")

        # Check if the user wants to end the program
        if command.upper() == "END":
            print("Exiting the help system. Goodbye!")
            break

        # Show the help documentation for the entered command
        try:
            help(command)
        except Exception as e:
            print(f"Error retrieving help for '{command}': {e}")


# Run the help system
interactive_help()
