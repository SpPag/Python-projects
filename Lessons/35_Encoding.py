"""
UTF-8 is one of the most commonly used encoding systems in general. Windows-1253 (or cp1253) is used to support Greek
in Windows.
"""
encoding_systems = ["utf-8", "windows-1253"]
while True:
    filename = input("Please enter file-to-open's name (enter exit to exit): ")
    if filename in ["exit", "EXIT"]:
        break
    for e in encoding_systems:
        try:
            f = open(filename, "r", encoding=e)
            f_contents = f.read()
        except Exception as error:
            print(f"error: {error}")
            print(f"encoding system {e} is incorrect.")
        else:
            print(f"file {filename} is encoded using {e}")
            print(f_contents)
            break