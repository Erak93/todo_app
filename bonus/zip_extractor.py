import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)



if __name__ == "__main__":
    extract_archive("output.zip",r"C:\Users\giann\PycharmProjects\todo_app\todo_app\bonus\dest")
