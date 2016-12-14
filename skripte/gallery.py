import os
import numpy as np
import PIL.Image

# Folder for images
imagefolder = "images/"

# Thumbnail folder
thfolder = "thumb/"

# Thumbnail size
thsize = 320, 240

# Filename for file with descriptions for images
dfn = "_data/galeriebeschreibung.csv"

# Table order
tablelist = ['filename','thfilename','folder','date','fav','show','de','en','es']

# Filename for file with categories and titles
cfn = "_data/galeriekategorien.csv"


##############################

EXIF_DATE = 36867
extensions = [".jpg", ".JPG", ".jpeg", ".JPEG"]
dl = []
cl = []

# Load cfn
if os.path.exists(cfn):
    cf = open(cfn, 'r')
    for line in cf:
        row = line.split(",")
        row = [ e.strip() for e in row ]
        cl += [row]
else:
    print("Could not find file with directory descriptions ('{:s}')".format(cfn))
    print("I will stop here")
    exit(-1)

if(len(cl) > 1):
    cl = cl[1:]
else:
    cl = 0
ncl = np.array(cl)

print ncl

# Load dfn or create empty list
if os.path.exists(dfn):
    df = open(dfn, 'r')
    for line in df:
        if(line.strip() != ""):
            rowlist = line.strip().split(",")
            rowdict = {tablelist[i]:rowlist[i] for i in range(len(tablelist))}
            dl += [rowdict]
    df.close()



# go through image folders - each subfolder will be one page
for folder in os.listdir(imagefolder):
    data = ncl[(ncl[:,0] == folder)]
    if data.size != 0:
        print("Found folder with description: {:s}".format(folder))
        if not os.path.exists(os.path.join(imagefolder, folder, thfolder)):
            os.mkdir(os.path.join(imagefolder, folder, thfolder))
        # go through subfolder
        imglist = []
        for fn in os.listdir(os.path.join(imagefolder, folder)):
            if any(fn.endswith(ext) for ext in extensions):
                ffn = os.path.join(imagefolder, folder, fn)
                #print(ffn)
                img = PIL.Image.open(ffn)
                if 'exif' in img.info:
                    imgdate = img._getexif()[EXIF_DATE]
                else:
                    imgdate = ""
                    print("File without correct image tag found. Will stop now")
                    print("Add with exiftool -DateTimeOriginal='YYYY:MM:DD hh:mm:ss' {:s}".format(ffn))
                    exit(-1)
                # check if file already in list
                if fn not in [d['filename'] for d in dl]:
                    #dl[folder][fn] = {'filename': fn,
                    if "small" in fn:
                        outfn = fn.replace("small", "thumb")
                    else:
                        outfn = fn.replace(".", "thumb.")
                    dl += [{'filename': fn,
                            'thfilename': outfn,
                            'folder': folder,
                            'date': imgdate,
                            'fav': "",
                            'show': "x",
                            'de': "",
                            'en': "",
                            'es': ""}]
                    print("Creating thumbnail for {:s} named {:s}".format(fn, outfn))
                    img.thumbnail(thsize, PIL.Image.ANTIALIAS)
                    img.save(os.path.join(imagefolder, folder, thfolder, outfn), "JPEG")

                # else?
        #imglist.sort(key = lambda item:item['date'])

f = open(dfn, 'w')
dl.sort(key = lambda item:item['date'])
f.write(','.join(tablelist) + "\n")
for item in dl:
    line = ','.join("{:s}".format(item[a]) for a in tablelist)
    f.write(line + "\n")
f.close()
    
