def format_greeting(name, title="Customer"):
    # Remove leading/trailing whitespace
    cleaned_name = name.strip()
    if cleaned_name == "":
        return "Hello, Valued Customer!" # Empty input
    titled_name = cleaned_name.title()
    first_name = titled_name.split()[0] # get first name
    return f"Hello, {first_name} ({title})!" # Greeting message


def main(): 
    full_name = input("Enter your full name: ")
    greeting = format_greeting(full_name)
    print(greeting)

main()