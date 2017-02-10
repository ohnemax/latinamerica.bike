# -*- coding: utf-8 -*-
#####

import gpxpy
import gpxpy.gpx
import os
import cyclegpx
######import list of files

####filter lists###
#tl=[1,6,7]
#tl2=[True, True, False]

#filtered_list = [i for indx,i in enumerate(tl) if tl2[indx] == True]
#filtered_list = [i for (i, v) in zip(tl, tl2) if v]

#print(filtered_list)
#exit(0)

#####get list of files

verzeichnis="./"
track_verzeichnis=verzeichnis+"tracks/"

l=[]
for file in os.listdir(track_verzeichnis):
    endung=os.path.basename(file)[-3:]
    if(endung=="gpx"):
        
        filename=file
        l+=[file]

l.sort()        
#print(l)        
#l=l[:-1]
print(l)


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

aldist=[]
alakmh=[]
alday=[]
almaxkmh=[]
altime=[]
ezldist=[]

ltf=[]
        

###var für nicht selbstgefahrene km
countgefahr=0

###read info of gpx
for filename in l:
    gefahr=False
    
    ###!change to corresponding folder
    fn = track_verzeichnis+filename
    #~/storage/shared/latinamerica.bike/cg./"+filename
    
    
    cg = cyclegpx.trip(fn)
    print(filename)

    cg.loadandparse()
    cg.calculate()

    descr=cg.trackdescription()
       
    if(descr[0]=="*"):
        gefahr=True
        countgefahr+=+1
        descr=descr[1:]
    
        
    ###extract detailed info
    dist = cg.totaldistance()
    maxkmh = cg.maxspeed()
    time=cg.movingtimeseconds()
    akmh=cg.averagemovingspeed()
    hoch = cg.climbingdistance()
    runter = cg.descendingdistance()
    date = cg.trackname()[:-3]
    day = cg.trackname()[-2:]
        
    #add infos to list
    aldist+=[dist]
    alday+=[day]
    almaxkmh+=[maxkmh]
    alakmh+=[akmh]
    altime+=[time]
        
    
    if gefahr == False:
        ltf.append(True)
    else: 
        ltf.append(False)
                      
    ###stats total
    gesamtdist+=dist
    #print(gesamtdist)
    gesamtday+=1
    
        
    count=0
    
    while(cg.trackdescription()[count]!="-"):
        count=count+1
    
    start=cg.trackdescription()[:count-1]   
    end=cg.trackdescription()[count+1:] 


        
    
    row = u"|"
    row += "[{:s}".format(day)
    if (gefahr):
       row+="+]"
    else:
       row+="]"    
    row += "(http://www.latinamerica.bike/track/d"+day+"LANG) |"
    row += u"{:s} |".format(start)
    row += u"{:s} |".format(end)
    row += "{:.2f} |".format(dist) 
    row += "{:.2f} |".format(akmh) 
    row += "{:.2f} |".format(maxkmh) 
    row += "{:.2f} |".format(hoch*1000)
    row += "{:.2f} |".format(runter*1000) 
    
    table+=row + "\n"

##### 
   
#######table of cycling days
head_de="| Tag | von | nach | Distanz | durchschnittliche km/h | max km/h | Höhenmeter hoch | Höhenmeter runter |\n"
head_en="| day | from | to | distance | average km/h | max km/h | altitude uphill | altitude downhill |\n"

print(head_de)    
print(table)    
#print("minmax")
   
#make list for countable kms
print(ldist)

ldist= [i for (i, v) in zip(aldist, ltf) if v]
lday= [i for (i, v) in zip(alday, ltf) if v]
lmaxkmh= [i for (i, v) in zip(almaxkmh, ltf) if v]
lakmh= [i for (i, v) in zip(alakmh, ltf) if v]
     
      
 ###extract track-localities

############
#####make files
    

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
statistic_de+="Gesamt km (getrackt): {:.2f}  \n".format(gesamtdist)
statistic_de+="Gesamt Tage auf dem Rad: {:.0f}  \n".format(gesamtday)
statistic_de+= "km ohne Platten: bisher alle!  \n"
statistic_de+= "Anzahl angebotener Lifts: 4\n\n"

statistic_en="## overall statistics\n\n"
#statistic+=("%str"), gesamtdist
statistic_en+="total km (tracked): {:.2f}  \n".format(gesamtdist) 
statistic_en+="days spent on the bike: {:.0f}  \n".format(gesamtday)
statistic_en+= "km without punctures: all!  \n"
statistic_en+= "free offered lifts: 4\n\n"

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

########Etappenzielstatiatik
#def variable


######### Track-Einträge
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
   if line.strip()=="":
       continue
   #print(line)
   #print("blabla")
   ee = line.split("|")
   ee=ee[1:-1]
   #print("ee")
   #print(ee)
   
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
    
    head_title_en="title: 'Biking day {:s}'  \n".format(days[element].strip())
    head_author="author: team \n"
    head_date= "modified: {:s}\n".format(date[element].strip())
    head_category="category: track \n"
    head_lang_de="lang: de \n"
    head_lang_en="lang: en \n"
    head_ref="ref: d{:s}\n".format(days[element].strip())
    head_descr_de=desc_de[element]+"\n\n"
    head_descr_en=desc_en[element]+"\n\n"
    head_end="archive: false \ncomments: true \nfeatured: false \n--- \n\n"
    maps="<iframe width='480' height='360' src='http://track-kit.net/maps_s3/?v=embed&track={:s}".format(ident[element].strip())
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




########Etappenzielstatiatik
#def variable

lez = {}
lez[1] = (1, 11, "Rundreise Uruguay", 230879)
lez[2] = (12, 20, "Bahia Blanca", 230881)
lez[3] = (24, 35, "Puerto Madryn", 232100)
lez[4] = (37, 43, "Ushuaia", 232845)
lez[5] = (44, 53, "El Calten", 234072)
lez[6] = (54, 76, "Puerto Montt/Carretera Austral", 235134)

lrow_ez=[]
lrow_ez_en=[]

for key in lez:
    
    lvar1=lez[key][0]
    
    lvar2=lez[key][1]    

    
    eztime=0       
    ezakmh=0
    ezldist=[] 
    ezltime=[]   
     
    for i in range(lez[key][0]-1,lez[key][1]+1):
    #ez_dist+=
        
        ezdist=0
    
#ezdist+=dist
        #print(aldist)
        ezldist=aldist[lvar1-1:lvar2:]
            
        for element in ezldist:
            ezdist+=element
        #print(ezldist)
        #print("ezdist")
        #print(ezdist)
        
        ezltime=altime[lvar1-1:lvar2:]
        
        for time in ezltime:
            eztime+=time
        
        eztime=eztime/3600
        
        
    ezakmh=ezdist/eztime
    
    #print("dist,time,akmh")
    #print(ezdist)
    #print(eztime)
    #print(ezakmh)    
    
    
    row_ez= "{:.0f}. Etappenziel: ".format(key)
    row_ez+= lez[key][2]
    row_ez+= "\n\n"
    row_ez+= "Reisetage: {:.0f} - {:.0f}  \n".format(lvar1, lvar2)
    row_ez+= "Etappendistanz: {:.2f}  \n".format(ezdist)
    row_ez+= "Etappenzeit: {:.2f}  \n".format(eztime)
    row_ez+= "Etappendurchschnittsgeschwindigkeit: {:.2f}  \n\n".format(ezakmh)
    row_ez+= "<iframe width='480' height='360' src='http://cg.kit.net/maps_s3/?v=embed&cg.{:.0f}.gpx' frameborder='0' allowfullscreen></iframe>\n".format(lez[key][3])
   
    
    #print(row_ez)
     
    lrow_ez+=[row_ez]
    
    ####write row for en

    row_ez_en= "{:.0f}. interim goal: ".format(key)
    row_ez_en+= lez[key][2]
    row_ez_en+= "\n\n"
    row_ez_en+= "travelling days: {:.0f} - {:.0f}  \n".format(lvar1, lvar2)
    row_ez_en+= "distance: {:.2f}  \n".format(ezdist)
    row_ez_en+= "time: {:.2f}  \n".format(eztime)
    row_ez_en+= "average speed: {:.2f}  \n\n".format(ezakmh)
    row_ez_en+= "<iframe width='480' height='360' src='http://cg.kit.net/maps_s3/?v=embed&cg.{:.0f}.gpx' frameborder='0' allowfullscreen></iframe>\n".format(lez[key][3])
   
    
    #print(row_ez_en)
     
    lrow_ez_en+=[row_ez_en]




###write file for etappenziel
includes_verzeichnis=verzeichnis+"_includes/"

ez_de=includes_verzeichnis+"ez_de.md"

print(lrow_ez)
rowlrow=""
for i in lrow_ez:
    rowlrow+=i 
    print(i)
    rowlrow+="\n"
    
    
    
f = open(ez_de, "w")
f.write(rowlrow)
#f.write(head_de)
f.close()


##english file
ez_en=includes_verzeichnis+"ez_en.md"

print(lrow_ez_en)
rowlrow_en=""
for i in lrow_ez_en:
    rowlrow_en+=i 
    print(i)
    rowlrow_en+="\n"
    
    
    
f = open(ez_en, "w")
f.write(rowlrow_en)
#f.write(head_de)
f.close()
