extensions = input("Name of file? ").strip()

match extensions:
    case _ if extensions.endswith(".gif"):
        print("image/gif")
    case _ if extensions.endswith(".jpg") or extensions.endswith(".jpeg"):
        print("image/jpeg")
    case _ if extensions.endswith(".png"):
        print("image/png")
    case _ if extensions.endswith(".pdf"):
        print("application/pdf")
    case _ if extensions.endswith(".txt"):
        print("text/plain")  
    case _ if extensions.endswith(".zip"):
        print("application.zip")
    case _:
        print("application/octet-stream")

