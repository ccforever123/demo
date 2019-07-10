import os


def main():
    path = os.path.join(os.getcwd(), 'yellow\\watchface\\res')

    for parents, dirnames, filenames in os.walk(path):
        filenameFront = 'A100_000'
        filenameIndex = 1
        for filename in filenames:
            filePath = os.path.join(parents, filename)
            newfilename = get_filename_index(filenameFront, filenameIndex)[0] + '.png'
            filenameIndex = get_filename_index(filenameFront, filenameIndex)[1]
            newFilename = os.path.join(parents, newfilename)
            os.rename(filePath, newFilename)

def get_filename_index(filenameFront, filenameIndex):
    lenFileIndex = len(str(filenameIndex))
    if lenFileIndex == 1:
        filename = filenameFront[:-1] + str(filenameIndex)
    elif lenFileIndex == 2:
        filename = filenameFront[:-2] + str(filenameIndex)
    else:
        filename = filenameFront[:-3] + str(filenameIndex)
    return filename, filenameIndex + 1

if __name__ == "__main__":
    main()