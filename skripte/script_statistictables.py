#####

import gpxpy
import gpxpy.gpx

import os

######import list of files

verzeichnis="./"
tracks_verzeichnis=verzeichnis+"tracks/"

l=[]
for file in os.listdir(tracks_verzeichnis):
    endung=os.path.basename(file)[-3:]
    if(endung=="gpx"):
        filename=file
        l+=[file]
l=l[:-1]

#print(l)
#print(os.listdir(verzeichnis))
#l=["2016-09-29_d2.gpx", "2016-09-29_d3.gpx", "2016-09-29_d4.gpx", "2016-09-29_d5.gpx"]

##### create empty lists

table =""
ldist=[]
lmaxkmh=[]
lakmh=[]
lhoch=[]
lrunter=[]
lday=[]
ldate=[]
gesamtdist=0
gesamtday=0


###var für nicht selbstgefahrene km
countgefahr=0

###read info of gpx
for filename in l:
    gefahr=False
    
    ###!change to corresponding folder
    fn = tracks_verzeichnis+filename
    #~/storage/shared/latinamerica.bike/tracks/"+filename
    
    gpx_file = open(fn, 'r')
    gpx = gpxpy.parse(gpx_file)
    print(gpx)

    for track in gpx.tracks:
        ###count for gefahr
        print(track)
        print(track.description[0])
        if(track.description[0]=="*"):
            gefahr=True
            countgefahr+=+1
            track.description=track.description[1:]
        
        ###extract detailed info
        dist = track.length_3d()/1000
        maxkmh = track.get_moving_data()[4]/1000*3600
        akmh =dist/(track.get_moving_data()[0]/3600)
        hoch = track.get_uphill_downhill()[0]
        runter = track.get_uphill_downhill()[1]
        date = track.name[0:10]
        day = track.name[12:]
        
        ###include in list if all km were cycled
        if not gefahr:
            ldist+=[dist]
            lday+=[day]
            lmaxkmh+=[maxkmh]
            lakmh+=[akmh]
        
        ###stats total
        gesamtdist+=dist
        #print(gesamtdist)
        gesamtday+=1
       
    
    ###extract track localities
    
    count=0
    
    while(track.description[count]!="-"):
        count=count+1
    
    start=track.description[:count-1]   
    end=track.description[count+1:] 
    
#######table of cycling days
    head_de="| Tag | von | nach | Distanz | durchschnittliche km/h | max km/h | Höhenmeter hoch | Höhenmeter runter |\n"
    head_en="| day | from | to | distance | average km/h | max km/h | altitude uphill | altitude downhill |\n"
    
    
    row = "|"
    row += "[{:s}".format(day)
    if (gefahr):
       row+="+]"
    else:
       row+="]"    
    row += "(http://www.latinamerica.bike/track/d"+day+"LANG) |"
    
    row += "{:s} |".format(start) 
    row += "{:s} |".format(end) 
    row += "{:.2f} |".format(dist) 
    row += "{:.2f} |".format(akmh) 
    row += "{:.2f} |".format(maxkmh) 
    row += "{:.2f} |".format(hoch)
    row += "{:.2f} |".format(runter) 
    
    table+=row + "\n"

##### 

print(head_de)    
print(table)    
#print("minmax")



###print first infos of cycling days

subtitle_de="\n## Radlertageinfos \n\n"
subtitle_en="\n## information about cycling days \n\n"

includes_verzeichnis=verzeichnis+"_includes/"
fhn_de=includes_verzeichnis+"days_de.md"

f = open(fhn_de, "w")
f.write(subtitle_de)
f.write(head_de)
f.write(table.replace("LANG",""))
f.close()

fhn_en=includes_verzeichnis+"days_en.md"

f = open(fhn_en, "w")
f.write(subtitle_en)
f.write(head_en)
f.write(table.replace("LANG","en"))
f.close()

###### mix/max table

head_de="|  | Max | Tag | Min | Tag |  \n| --- |---:| :---:| ---:| :---:|   \n"

head_en="|  | max | day | min | day |  \n| --- |---:| :---:| ---:| :---:|   \n"    
###calculate max

#print(lday)    
rdist_de = "| Distanz | " 
rdist_en = "| distance | " 
rdist= "{:.2f}".format(max(ldist))
#    print(rdist)

###get day for max    
count=0
var=int()
		#		ldist[2]
		#		print(ldist[0])
for i in ldist:
    count+=+1
   
    while( i > var):
        inum=count-1
        var=i
    
#print(inum)
#print(countgefahr)

    
rdist+=" | [" + str( lday[inum]) + "]"
        
maxi=max(ldist)
		#		print(maxi)
rdist+="(http://www.latinamerica.bike/track/d"+str(lday[inum])+"LANG) |"
#    print(row)
    
    
###calculate min
#print("min")    

rdist+= "{:.2f}|".format(min(ldist))
    
count=0
var=100000000000
		#		ldist[2]
    #print(ldist[0])
for i in ldist:
    count+=+1
    while( i < var):    
        inum=count-1
        var=i
    
    
rdist+="[" + str(lday[inum]) + "]"
        
rdist+="(http://www.latinamerica.bike/track/d"+str(lday[inum])+"LANG) |"
	#			print(row)
######

###akmh
###calculate max
   
rakmh_de = "| durchschnittliche km/h  | " 
rakmh_en = "| average km/h | "
rakmh= "{:.2f}|".format(max(lakmh))
#    print(rakmh)
    
count=0
var=int()
inum=int()
		#		ldist[2]
		#		print(ldist[0])
for i in lakmh:
    count+=+1
    
    while( i > var):
        inum=count-1
        var=i
    
rakmh+="[" + str(lday[inum]) + "]"
print("lakmh")
print(lakmh)        
maxi=max(lakmh)
		#		print(maxi)
rakmh+="(http://www.latinamerica.bike/track/d"+str(lday[inum])+"LANG) |"
#    print(row)
    
####calculate min
#print("min")    

rakmh+= "{:.2f}|".format(min(lakmh))
#rakmh+=  str(min(lakmh)) + "|" 
#    print(rakmh)
       
count=0
var=100000000
		#		ldist[2]
    #print(ldist[0])
for i in lakmh:
    count+=+1
    while( i < var):
        inum=count-1
        var=i
    
rakmh+="[" + str(lday[inum]) + "]"
        
rakmh+="(http://www.latinamerica.bike/track/d"+str(lday[inum])+"LANG) |"
	#			print(row)
    
###maxkmh
###calculate max
    
rmaxkmh = "| max km/h  | "  
rmaxkmh+= "{:.2f}|".format(max(lmaxkmh))
    
count=0
var=0
inum=int()
		#		ldist[2]
		#		print(ldist[0])
for i in lmaxkmh:
    count+=+1
	#			inum=int()
    while( i > var):
        inum=count-1
        var=i
    
rmaxkmh+="[" + str(lday[inum]) + "]"
        
maxi=max(lmaxkmh)
		#		print(maxi)
rmaxkmh+="(http://www.latinamerica.bike/track/d"+ str(lday[inum])+"LANG) |"
#    print(row)
    
####calculate min
#print("min")    

rmaxkmh+= "{:.2f}|".format(min(lmaxkmh))
#    print(rmaxkmh)
    
    
count=0
var=100000000000
		#		ldist[2]
    #print(ldist[0])
for i in lmaxkmh:
    count+=+1
    while( i < var):
        inum=count-1
        var=i
    
rmaxkmh+="[" + str(lday[inum]) + "]"
        
rmaxkmh+="(http://www.latinamerica.bike/track/d"+str(lday[inum])+"LANG) |"
	#			print(row)
    
#####
table_de=rdist_de + rdist + "\n" +rakmh_de + rakmh + "\n" +rmaxkmh + "\n" 
table_en=rdist_en + rdist + "\n" +rakmh_en + rakmh + "\n" +rmaxkmh + "\n" 


statistic_de="## Gesamtstatistiken\n\n"
statistic_de+= "Gesamt km (getrackt): "
#statistic+=("%str"), gesamtdist
statistic_de+="{:.2f}  \n".format(gesamtdist) 
statistic_de+="Gesamt Tage auf dem Rad: "
statistic_de+="{:.0f}  \n".format(gesamtday)
statistic_de+= "km ohne Platten: bisher alle!  \n"
statistic_de+= "Anzahl angebotener Lifts: 3\n\n"

statistic_en="## overall statistics\n\n"
statistic_en+= "total km (tracked): "
#statistic+=("%str"), gesamtdist
statistic_en+="{:.2f}  \n".format(gesamtdist) 
statistic_en+="days spent on the bike: "
statistic_en+="{:.0f}  \n".format(gesamtday)
statistic_en+= "km without punctures: all!  \n"
statistic_en+= "free offered lifts: 3\n\n"

##### 
print(statistic_de)
print(head_de)    
print(table_de)    

#######get update date

import time
toda=time.strftime("%d/%m/%Y")

update_de="**letztes Update: " 
update_de+= toda
update_de+="**\n\n"

update_en="**last update: " 
update_en+= toda
update_en+="**\n\n"

#####


fhn_de=includes_verzeichnis+"stats_de.md"
f = open(fhn_de, "w")
f.write(update_de)
f.write(statistic_de)
f.write(head_de)
f.write(table_de.replace("LANG",""))
f.close()

fhn_en=includes_verzeichnis+"stats_en.md"
f = open(fhn_en, "w")
f.write(update_en)
f.write(statistic_en)
f.write(head_en)
f.write(table_en.replace("LANG","en"))
f.close()


#########
skripte_verzeichnis=verzeichnis+"skripte/"
fhn=skripte_verzeichnis+"track-beschreibung"
fn =open(fhn, "r")

#text= fn.read()
days=[]
date=[]
desc_de=[]
desc_en=[]
ident=[]


for line in fn:
   print(line)
   #print("blabla")
   ee = line.split("|")
   ee=ee[1:-1]
   print("ee")
   print(ee)
   
   days+=[ee[0]]
   date+=[ee[1]]
   desc_de+=[ee[2]]
   desc_en+=[ee[3]]
   ident+=[ee[4]]
   #print("days:")
   #print(days)
   
for element in range(1,len(days)):   

    head_layout="---   \nlayout: post \n"
    head_title_de="title: 'Radlertag "
    head_title_de+= "{:s}'  \n".format(days[element].strip())
    
    head_title_en="title: 'Biking day "
    head_title_en+= "{:s}'  \n".format(days[element].strip())
    head_author="author: team \n"
    head_date= "modified: "
    head_date+= "{:s}\n".format(date[element].strip())
    head_category="category: track \n"
    head_lang_de="lang: de \n"
    head_lang_en="lang: en \n"
    head_ref="ref: d"
    head_ref+="{:s}\n".format(days[element].strip())
    head_descr_de=desc_de[element]+"\n\n"
    head_descr_en=desc_en[element]+"\n\n"
    head_end="archive: false \ncomments: true \nfeatured: false \n--- \n\n"
    maps="<iframe width='480' height='360' src='http://track-kit.net/maps_s3/?v=embed&track="
    maps+="{:s}".format(ident[element].strip())
    maps+=".gpx' frameborder='0' allowfullscreen></iframe>"

    posts_verzeichnis=verzeichnis+"_posts/"
    fhn_de=posts_verzeichnis+"{:s}-d{:s}.md".format(date[element].strip(),days[element].strip())
    fhn_en=posts_verzeichnis+"{:s}-d{:s}en.md".format(date[element].strip(),days[element].strip())

    wtf_de=head_layout+head_title_de+head_author+head_date+head_category+head_lang_de+head_ref+head_end+head_descr_de+maps
    f = open(fhn_de, "w")
    f.write(wtf_de)
    f.close()

    wtf_en=head_layout+head_title_en+head_author+head_date+head_category+head_lang_en+head_ref+head_end+head_descr_en+maps
    f = open(fhn_en, "w")
    f.write(wtf_en)
    f.close()
