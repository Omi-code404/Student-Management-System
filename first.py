def success_decorator(func):
    def wrapper():
        print("🔄Process started...")
        func()
        print("✅ Process completed successfully!")
    return wrapper

@success_decorator
def upload_file():
    print("Uploading file to the server...")

upload_file()