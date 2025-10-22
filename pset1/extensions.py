def main():
    _, file_type = input("File name: ").strip().split(".")

    if file_type == "gif" :
        print("image/gif")
    elif file_type == "jpg" or file_type == "jpeg":
        print("image/jpg")
    elif file_type == "png" :
        print("image/png")
    elif file_type == "pdf":
        print("application/pdf")
    elif file_type == "txt":
        print("txt")
    elif file_type == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()