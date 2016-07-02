#!/usr/lib/python

from __future__ import division
import math
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='notiskon', api_key='tb196pluzj')
# declare the saving in percentage for different combination of patterns during weekdays
#this allocation is based in 50/50 wavelength resource sharing. However it can be another scenario with unequal sharing
table_transport_weekdays = [5,100,50,80,50,40]
table_resident_weekdays = [20,50,65,90,100,100]
table_office_weekdays = [5,50,100,75,75,45]

table_transport_weekend = [0,50,50,40,40,30]
table_resident_weekend = [25,50,75,75,85,100]
table_office_weekend = [5,25,50,40,40,35]

table_transport_office_weekdays = [10,75,75,75,50,40]
table_transport_resident_weekdays = [25,75,60,90,75,50]
table_office_resident_weekdays = [25,88,75,75,75,50]
table_office_resident_transport_weekdays = [25,67,80,80,65,60]

table_transport_office_weekend = [5,50,50,50,50,40]
table_transport_resident_weekend = [12,70,70,70,70,70]
table_office_resident_weekend = [15,70,70,70,70,70]
table_office_resident_transport_weekend = [20,60,60,60,60,60]

#select combination of traffic area

pattern_combo = int(raw_input( " Please select combination of traffic: \n 1. Transport - Office \n 2. Transport - Resident \n 3. Office - Resident \n 4. Office-Transport-Resident \n"))
if pattern_combo == 1:
	n_sc_transport = int(raw_input("Give number of Small Cells in transport area: "))
	n_sc_office = int(raw_input("Give number of Small Cells in office area: "))
	#get the number of resources that share the network
	shared = int(2)
	table_weekday = table_transport_office_weekdays
	table_weekend = table_transport_office_weekend
	not_shared_1_weekday = table_transport_weekdays
	not_shared_2_weekday = table_office_weekdays
	not_shared_1_weekend = table_transport_weekend
	not_shared_2_weekend = table_office_weekend
	#print table_weekday
elif pattern_combo == 2:
	n_sc_transport = int(raw_input("Give number of Small Cells in transport area: "))
	n_sc_resident = int(raw_input("Give number of Small Cells in resident area: "))
	#get the number of resources that share the network
	shared = int(2)
	table_weekday = table_transport_resident_weekdays
	table_weekend = table_transport_resident_weekend
	not_shared_1_weekday = table_transport_weekdays
	not_shared_2_weekday = table_resident_weekdays
	not_shared_1_weekend = table_transport_weekend
	not_shared_2_weekend = table_resident_weekend
elif pattern_combo == 3:
	n_sc_office = int(raw_input("Give number of Small Cells in office area: "))
	n_sc_resident = int(raw_input("Give number of Small Cells in resident area: "))
	#get the number of resources that share the network
	shared = int(2)
	table_weekday = table_office_resident_weekdays
	table_weekend = table_office_resident_weekend
	not_shared_1_weekday = table_resident_weekdays
	not_shared_2_weekday = table_office_weekdays
	not_shared_1_weekend = table_resident_weekend
	not_shared_2_weekend = table_office_weekend
elif pattern_combo == 4 :
	n_sc_transport = int(raw_input("Give number of Small Cells in transport area: "))
	n_sc_resident = int(raw_input("Give number of Small Cells in resident area: "))
	n_sc_office = int(raw_input("Give number of Small Cells in office area: "))
	#get the number of resources that share the network
	shared = int(3)
	table_weekday = table_office_resident_transport_weekdays
	table_weekend = table_office_resident_transport_weekend
	not_shared_1_weekday = table_transport_weekdays
	not_shared_2_weekday = table_office_weekdays
	not_shared_3_weekday = table_resident_weekdays
	not_shared_1_weekend = table_transport_weekend
	not_shared_2_weekend = table_office_weekend
	not_shared_2_weekend = table_resident_weekend
else:
	print " Please type 1 or 2 or 3 or 4 "
	exit()



# select architecture and define number of wavelengths
print "Please select the transport architecture:"
slc = int(raw_input("\n\t1 for NG-PON2 or \n\t2 for WR-WDM-PON \n"))
if slc == 1:
	wavelength = 16
	print "16 wavelengths are available to be shared between " + str(shared) + " different areas"
else:
        print "80  wavelengths are available to be shared between " + str(shared) + " different areas"
        wavelength = 80
if True:
	wss_office = 0
	wss_transport = 0
	wss_resident = 0

        #find how many WSS we need and how resources are
	try:
		wss_office = int(n_sc_office / int((wavelength/shared)))
		wss_office_mod= int(n_sc_office % int((wavelength/shared)))
		#check if there is unequal sharing
		#if wss_office_mod !=0:
			#print str(wss_office_mod) + " sc remain in office: this means that in one WSS there will be unequal sharing of resources"
	except:
		pass
	try:
		wss_transport = int(n_sc_transport / int((wavelength/shared)))
		wss_transport_mod = int(n_sc_transport % int((wavelength/shared)))
		#print wss_transport_mod
#check if there is unequal sharing
		#if wss_transport_mod !=0:
			#print  str(wss_transport_mod) + " sc remain in transport: this means that in one WSS there will be unequal sharing of resources"
	except:
		pass
	try:
	    wss_resident = int(n_sc_resident / int((wavelength/shared)))
		#wss_resident_mod = int(n_sc_resident % (wavelength/shared))
	    wss_resident_mod = int(n_sc_resident % int((wavelength/shared)))
		#check if there is unequal sharing
	    #if wss_resident_mod !=0:
			#print wss_resident_mod + " sc remain is resident: this means that in one WSS there will be unequal sharing of resources"
	except:
		pass

	#calculate number of wss that are needed


	#add wss values in a table and remove zeros, if any
	list_of_wss = [wss_transport,wss_resident,wss_office]

	print list_of_wss
	#check triple equality
	if list_of_wss[0] != list_of_wss[1] or list_of_wss[0] != list_of_wss[2]:
		try:
			list_of_wss.remove(0)
		except:
			pass
		print list_of_wss
		min_wss = min(list_of_wss)
		print "min_devices = " + str(min_wss)
		max_wss = max(list_of_wss)
		#find which value is office, transport, resident
		#find max
		if max_wss == wss_office:
	                        max_sc = n_sc_office
	                        max_sc_mod = wss_office_mod
				max_area = "office"
				print "max sc is office"
	        elif max_wss == wss_transport:
	        		max_sc = n_sc_transport
	        		max_sc_mod = wss_transport_mod
				max_area = "transport"
				print "max sc is transport"
		else:
			max_sc = n_sc_resident
			max_sc_mod = wss_resident_mod
			max_area = "resident"
			print "max sc is resident"


		#find middle and calculate wss number, if 3 areas
		if pattern_combo == 4:
			list_of_wss.sort()
			middle_wss = list_of_wss[1]
			if min_wss == wss_office:
	                        min_sc = n_sc_office
	                        min_sc_mod = wss_office_mod
	                        min_wss = wss_office
	                        print "min sc is office"
				v1="transport"
				v2="resident"
		        elif min_wss == wss_transport:
	                        min_sc = n_sc_transport
	                        min_sc_mod = wss_transport_mod
	                        min_wss = wss_transport
	                        print "min sc is transport"
				v1="office"
				v2="resident"
	        	else:
	                	min_sc = n_sc_resident
	                	min_sc_mod = wss_resident_mod
	                	min_wss = wss_resident
	                	print "min sc is resident"
				v1="transport"
				v2="office"

			if middle_wss == wss_office:
				middle_sc = n_sc_office
				middle_sc_mod = wss_office_mod
			elif middle_wss == wss_transport:
				middle_sc = n_sc_transport
				middle_sc_mod = wss_transport_mod
			else:
				middle_sc = n_sc_resident
				middle_sc_mod = wss_resident_mod

			remaining_from_middle = int(middle_sc - min_sc)
			print "\nremaining_from_middle " + str(remaining_from_middle)
			print str(int((wavelength/shared)+1))
			print str(min_wss)
			if wavelength == 16:
				remaining_from_max = int(max_sc - (min_wss*(int((wavelength/shared)+1))))
			else:
				remaining_from_max = int(max_sc - (min_wss*(int((wavelength/shared)+2))))
			print "\nremaining_from_max " + str(remaining_from_max)
			#check if the max is from the same area
			if remaining_from_max >= remaining_from_middle:
				print "\nmax value is still " + max_area
			else:
				print " \nmax value has changed between " + v1 + " and " + v2
				if max_area is v1:
					max_area = v2

				elif max_area is v2:
					max_area = v1

				else:
					print "something is wrong...."

				temp = remaining_from_middle
				remaining_from_middle = remaining_from_max
				remaining_from_max = temp
				print "new max remaining: " + str(remaining_from_max)
			remaining_wss_for_middle = int(remaining_from_middle/(wavelength/(shared-1)))
			print "\n remaining_devices_for_middle "+ str(remaining_wss_for_middle)
			remaining_sc_for_middle_mod = int(remaining_from_middle%(wavelength/(shared-1)))
			print "\n remaining_sc_for_middle_mod " + str (remaining_sc_for_middle_mod)
			#remaining_sc_max = int(max_sc - (remaining_from_middle-remaining_sc_for_middle_mod))

			if remaining_sc_for_middle_mod == 0:
				not_shared_wss = int((remaining_from_max-remaining_from_middle)/16)
				if ((remaining_from_max-remaining_from_middle)%16) !=0:
					not_shared_wss = not_shared_wss + 1
					print str((remaining_from_max-remaining_from_middle)%16) + " remain to be connected in one device"
			else:
				not_shared_wss = int((remaining_from_max-remaining_from_middle)/16)
				if ((remaining_from_max-remaining_from_middle)%16) !=0:
					print "\none device has unequal sharing of resources."
					saved_wv = wavelength - (((remaining_from_max-remaining_from_middle)%16)+remaining_sc_for_middle_mod)
					print "\n In this case, " + str(saved_wv) + " are not used"
					print str((remaining_from_max-remaining_from_middle)%16) + " + " + str(remaining_sc_for_middle_mod) + " wavelengths are needed."
					try:
						if remaining_from_max == temp and max_area == v1:
							print str(remaining_sc_for_middle_mod) + " are from " + v2 + " area and " + str(((remaining_from_max-remaining_from_middle)%16)) + " are from " + v1
						elif remaining_from_max == temp and max_area == v2:
							print str(remaining_sc_for_middle_mod) + " are from " + v1 + " area and " + str(((remaining_from_max-remaining_from_middle)%16)) + " are from " + v2
						else:
							print "\n\tHEY DUDE...something is wrong...\n"
					except:
						pass
					if max_area == v1:
						print str(remaining_sc_for_middle_mod) + " are from " + v1 + " area and " + str(((remaining_from_max-remaining_from_middle)%16)) + " are from " + v2
					elif max_area == v2:
						print str(remaining_sc_for_middle_mod) + " are from " + v2 + " area and " + str(((remaining_from_max-remaining_from_middle)%16)) + " are from " + v1
					else:
						print "\n\tHEY DUDE...something is wrong...\n"

				#remaining_from_max = remaining_from_max - remaining_sc_for_middle_mod
				#unequal sharing in wss
				#unequal_max_wss = int(wavelength - remaining_sc_for_middle_mod)

				#not_shared_wss = int((remaining_from_max-remaining_from_middle)/16)
	                        #if ((remaining_from_max-remaining_from_middle)%16) !=0:
	                        #        not_shared_wss = not_shared_wss + 1
			print "\nIn total we need " + str(min_wss) + " shared device by 3 areas plus " + str(remaining_wss_for_middle)+" are shared between " + v1 + "-" + v2 + " and " + str(not_shared_wss) + " device assigned only to " + max_area + " area."
			# calculate savings in small Cells
			table_save_sc_3share =  []
			table_save_sc_3share_weekend =  []
			#print len(table_weekday)
			#print table_save_sc_3share
			for x in range(0, len(table_weekday)):
				#print x
				#print "table_weekday[x]=" + str(table_weekday[x])
				#print "(n_sc_office+n_sc_transport+n_sc_resident) = " + str ((n_sc_office+n_sc_transport+n_sc_resident))
				table_save_sc_3share.append(int(((min_wss*wavelength) * (table_weekday[x]/100))))
				table_save_sc_3share_weekend.append(int(((min_wss*wavelength) * (table_weekend[x]/100))))

			#print " table_save_sc_3share " + str(table_save_sc_3share)
	#table_transport_office_weekdays = [90,25,25,25,50,60]
	#table_transport_resident_weekdays = [75,25,40,10,25,50]
	#table_office_resident_weekdays = [75,12,25,25,25,50]
	#table_office_resident_transport_weekdays = [75,33,20,20,35,40]
			#print v1,v2
			table_save_sc_2share = []
			table_save_sc_2share_weekend = []
			if v1 in str("table_transport_office_weekdays") and v2 in str("table_transport_office_weekdays"):
				for x in range(0, len(table_transport_office_weekdays)):
					table_save_sc_2share.append(int(((remaining_wss_for_middle*wavelength) * (table_transport_office_weekdays[x]/100))))
					table_save_sc_2share_weekend.append(int(((remaining_wss_for_middle*wavelength) * (table_transport_office_weekend[x]/100))))
			elif v1 in str("table_transport_resident_weekdays") and v2 in str("table_transport_resident_weekdays"):
				for x in range(0, len(table_transport_resident_weekdays)):
					table_save_sc_2share.append(int(((remaining_wss_for_middle*wavelength) * (table_transport_resident_weekdays[x]/100))))
					table_save_sc_2share_weekend.append(int(((remaining_wss_for_middle*wavelength) * (table_transport_resident_weekend[x]/100))))
			elif v1 in str("table_office_resident_weekdays") and v2 in str("table_office_resident_weekdays"):
				for x in range(0, len(table_office_resident_weekdays)):
					table_save_sc_2share.append(int(((remaining_wss_for_middle*wavelength) * (table_office_resident_weekdays[x]/100))))
					table_save_sc_2share_weekend.append(int(((remaining_wss_for_middle*wavelength) * (table_office_resident_weekend[x]/100))))
			else:
				print "think again!!!!!!"
			#print len(table_save_sc_2share)
			#print "table_save_sc_2share " + str(table_save_sc_2share)
			sum_save_sc = []
			sum_save_sc_weekend = []
			for x in range(0, len(table_save_sc_2share)):
				sum_save_sc.append(int(table_save_sc_3share[x] + table_save_sc_2share[x]))
				sum_save_sc_weekend.append(int(table_save_sc_3share_weekend[x] + table_save_sc_2share_weekend[x]))
			print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
			print  "\nAt different times we use the following small cells during weekends:\n" + str(sum_save_sc_weekend)

		else:
			#print " test between 2 areas"
			table_save_sc_2share = []
			sum_save_sc = []
			table_save_sc_2share_weekend = []
			sum_save_sc_weekend = []
			if min_wss == wss_office:
	                        min_sc = n_sc_office
	                        min_sc_mod = wss_office_mod
	                        min_wss = wss_office
				min_area = "office"
	                 #       print "min sc is office"
		        elif min_wss == wss_transport:
	                        min_sc = n_sc_transport
	                        min_sc_mod = wss_transport_mod
	                        min_wss = wss_transport
	                  #      print "min sc is transport"
				min_area = "transport"
	        	else:
	                	min_sc = n_sc_resident
	                	min_sc_mod = wss_resident_mod
	                	min_wss = wss_resident
	                #	print "min sc is resident"
				min_area = "resident"

			#if two areas have equal amount of devices:
			if min_sc == max_sc:
				print "The two areas have equal amount of devices."
				if pattern_combo == 1:
					max_area = "transport"
					min_area = "office"
				elif pattern_combo == 2:
					max_area = "transport"
					min_area = "resident"
				elif pattern_combo == 3:
					max_area = "office"
					min_area = "resident"
				else:
					print "YOOOOOO....SOMTHING IS WRONG"
			#calculate how many device we need for the min_area
			max_remain_sc = max_sc - (min_wss*(wavelength/shared))
			#print " We need " + str(min_wss) + " device to share between areas " + min_area + " - " + max_area
			print "max_remain_sc " + str(max_remain_sc)


			if min_sc_mod == 0 :
				max_remain_wss = max_remain_sc / wavelength
				if (max_remain_sc % wavelength) != 0:
					max_remain_wss = int(max_remain_wss) + 1
					saved_wv = wavelength - (max_remain_sc % wavelength)
					print str((max_remain_sc % wavelength)) +  " are connected to one device from " +max_area+ " and " + str(saved_wv) + " wavelengths are saved"
					#print " we need " + str(max_remain_wss) + " to used only by " + max_area + " and will not be shared."
					print "\n\tIn total we need:"
					print "\n\t"+ str(min_wss) + " device to share between areas " + min_area + " - " + max_area + " and " + str(max_remain_wss) + " to used only by " + max_area
					for x in range(0, len(table_weekday)):
						#print table_weekday
						sum_save_sc.append(int(((min_sc*2) * (table_weekday[x]/100))))
						sum_save_sc_weekend.append(int(((min_sc*2) * (table_weekend[x]/100))))
					print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
					print  "\nAt different times we use the following small cells during weekends:\n" + str(sum_save_sc_weekend)
				elif (max_remain_sc % wavelength) == 0:
					#print "HERE"
					print "\n\tIn total we need:"
					print "\n\t"+ str(min_wss) + " device to share between areas " + min_area + " - " + max_area
					for x in range(0, len(table_weekday)):
						#print table_weekday
						sum_save_sc.append(int(((min_sc + max_sc) * (table_weekday[x]/100))))
						sum_save_sc_weekend.append(int(((min_sc + max_sc) * (table_weekend[x]/100))))
					print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
					print  "\nAt different times we use the following small cells during weekends:\n" + str(sum_save_sc_weekend)
				else:
					print "find what was WRONG"
					#print " we need " + str(max_remain_wss) + " to used only by " + max_area + " and will not be shared."
					#print "\n\tIn total we need:"
	                            #    print "\n\t" + str(min_wss) + " device to share between areas " + min_area + " - " + max_area + " and " + str(max_remain_wss) + " to used only by " + max_area
			# check for unequal sharing
			else :
				max_remain_wss = ((max_sc - (min_wss*(wavelength/shared))) / wavelength)
				print max_remain_sc
				if (max_remain_sc % wavelength) != 0 and (min_sc_mod+(max_remain_sc % wavelength))<= wavelength:
						#print "HERE"
						print "\none device has unequal sharing of resources."
						max_remain_wss = int(max_remain_wss) + 1
						print max_remain_wss
						saved_wv = wavelength - (min_sc_mod+(max_remain_sc % wavelength))
						#distribution of wavelengths
						min_shared_percentage = (min_sc_mod*100)/wavelength
						print "min_shared_percentage = " + str(min_shared_percentage)
						max_shared_percentage = ((max_remain_sc % wavelength)*100)/wavelength
						print "max_shared_percentage = " + str(max_shared_percentage)
						print "\nIn this case, " + str(saved_wv) + " wavelengths are not used"
						print "in the shared wss, " + str(min_sc_mod) + " are from " + min_area + " area and " + str((max_remain_sc % wavelength)) + " are from " + max_area
						#print "and we need " + str(max_remain_wss) + " to used only by "+ max_area
						if max_area == min_area:
							#print "HERE"
							table_save_sc_2share_eq_sh = []
							table_save_sc_2share_eq_sh_weekend = []
							print "\n\tIn total we need:"
							print "\n" + str(min_wss) + " device to share between areas " + min_area + " - " + max_area + " and one device with equal shared resources but not maximum usage."
							for x in range(0, len(table_weekday)):
								table_save_sc_2share_eq_sh.append(int(((min_sc_mod*2) * (table_weekday[x]/100))))
								table_save_sc_2share.append(int((((min_wss*(wavelength/shared))*2) * (table_weekday[x]/100))))
								sum_save_sc.append(int(table_save_sc_2share[x] + table_save_sc_2share_eq_sh[x]))
								#weekend
								table_save_sc_2share_eq_sh_weekend.append(int(((min_sc_mod*2) * (table_weekend[x]/100))))
								table_save_sc_2share_weekend.append(int((((min_wss*(wavelength/shared))*2) * (table_weekend[x]/100))))
								sum_save_sc_weekend.append(int(table_save_sc_2share_weekend[x] + table_save_sc_2share_eq_sh_weekend[x]))
							print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
							print  "\nAt different times we use the following small cells during weekends:\n" + str(sum_save_sc_weekend)
						else:
							#print "HERE"
							table_save_sc_2share_uneq_sh = []
							table_save_sc_2share_uneq_sh_weekend = []
							print "\n\tIn total we need:"
							print "\n" + str(min_wss) + " device to share between areas " + min_area + " - " + max_area + " and one device with unequal sharing"
							for x in range(0, len(table_weekday)):
								#print len(table_weekday)
								table_save_sc_2share_uneq_sh.append(int(((min_sc_mod+(max_remain_sc % wavelength)) * (table_weekday[x]/100))))
								table_save_sc_2share.append(int((((min_wss*(wavelength/shared))*2) * (table_weekday[x]/100))))
								sum_save_sc.append(int(table_save_sc_2share[x] + table_save_sc_2share_uneq_sh[x]))
								#print x
								table_save_sc_2share_uneq_sh_weekend.append(int(((min_sc_mod+(max_remain_sc % wavelength)) * (table_weekend[x]/100))))
								#print table_weekend[x]
								#print table_save_sc_2share_uneq_sh_weekend[x]
								table_save_sc_2share_weekend.append(int((((min_wss*(wavelength/shared))*2) * (table_weekend[x]/100))))
								#print table_save_sc_2share_weekend[x]
								sum_save_sc_weekend.append(int(table_save_sc_2share_weekend[x] + table_save_sc_2share_uneq_sh_weekend[x]))
							print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
							print  "\nAt different times we use the following small cells during weekends:\n" + str(sum_save_sc_weekend)
				elif (max_remain_sc % wavelength) != 0 and (min_sc_mod+(max_remain_sc % wavelength)) > wavelength:
					#distribution of wavelengths
					min_shared_percentage = (min_sc_mod*100)/wavelength
					print "min_shared_percentage = " + str(min_shared_percentage)

					max_shared_percentage = ((max_remain_sc % wavelength)*100)/wavelength
					print "max_shared_percentage = " + str(max_shared_percentage)
					max_shared_sc = wavelength - min_sc_mod
					print "\nIn one device we have unequal sharing of resources. The distribution is:\n " + str(min_sc_mod) + " from " + min_area + " and " + str(max_shared_sc) + " from the " + max_area
					not_shared_sc = int((max_remain_sc % wavelength) - max_shared_sc)
					print "\nOne device does not share resources and has " + str(not_shared_sc) + " connected from the " + max_area + " area."
					table_save_sc_2share_uneq_sh = []
					table_save_sc_2share_uneq_sh_weekend = []
					for x in range(0, len(table_weekday)):
						table_save_sc_2share_uneq_sh.append(int(((min_sc_mod*2) * (table_weekday[x]/100))))
						#in case of unequal sharing, eg 4 + 12, we can use the save pattern between the 4 and 4.
						table_save_sc_2share.append(int((((min_wss*(wavelength/shared))*2) * (table_weekday[x]/100))))
						sum_save_sc.append(int(table_save_sc_2share[x] + table_save_sc_2share_uneq_sh[x]))
						#weekend
						table_save_sc_2share_uneq_sh_weekend.append(int(((min_sc_mod*2) * (table_weekend[x]/100))))
						table_save_sc_2share_weekend.append(int((((min_wss*(wavelength/shared))*2) * (table_weekend[x]/100))))
						sum_save_sc_weekend.append(int(table_save_sc_2share_weekend[x] + table_save_sc_2share_uneq_sh_weekend[x]))
					print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
					print  "\nAt different times we use the following small cells during weekend:\n" + str(sum_save_sc_weekend)
				elif (max_remain_sc % wavelength) == 0:
					print "\none device has unequal sharing of resources."
					saved_wv = wavelength - min_sc_mod
					print "\n In this case, " + str(saved_wv) + " wavelengths are not used and the remaining used " + str(min_sc_mod) + " are from " + max_area + " area."
					#print " we need " + str(max_remain_wss) + " to used only by " + max_area
					#print "\n\tIn total we need:"
	                #                print "\n\t" + str(min_wss) + " device to share between areas " + min_area + " - " + max_area + " and " + str(max_remain_wss) + " to used only by " + max_area
					table_save_sc_2share_uneq_sh = []
					table_save_sc_2share_uneq_sh_weekend = []
					for x in range(0, len(table_weekday)):
						table_save_sc_2share_uneq_sh.append(int(((min_sc_mod*2) * (table_weekday[x]/100))))
						#in case of unequal sharing, eg 4 + 12, we can use the save pattern between the 4 and 4.
						table_save_sc_2share.append(int((((min_wss*(wavelength/shared))*2) * (table_weekday[x]/100))))
						sum_save_sc.append(int(table_save_sc_2share[x] + table_save_sc_2share_uneq_sh[x]))
						#weekend
						table_save_sc_2share_uneq_sh_weekend.append(int(((min_sc_mod*2) * (table_weekend[x]/100))))
						table_save_sc_2share_weekend.append(int((((min_wss*(wavelength/shared))*2) * (table_weekend[x]/100))))
						sum_save_sc_weekend.append(int(table_save_sc_2share_weekend[x] + table_save_sc_2share_uneq_sh_weekend[x]))
					print  "\nAt different times we use the following small cells:\n" + str(sum_save_sc)
					print  "\nAt different times we use the following small cells during weekend:\n" + str(sum_save_sc_weekend)
				else:
					print"/n HEY DUDE....YOU ARE STUPID!!!"

			#print "test print"
	#if 3 values are equal:
	else:
		print "\nIn total we need " + str(list_of_wss[0]) + " device to be shared between the three areas."
		table_save_sc_3share =  []
		table_save_sc_3share_weekend =  []
		#print len(table_weekday)
		#print table_save_sc_3share
		for x in range(0, len(table_weekday)):
			#print x
			#print "table_weekday[x]=" + str(table_weekday[x])
			#print "(n_sc_office+n_sc_transport+n_sc_resident) = " + str ((n_sc_office+n_sc_transport+n_sc_resident))
			table_save_sc_3share.append(int(((list_of_wss[0]*wavelength) * (table_weekday[x]/100))))
			table_save_sc_3share_weekend.append(int(((list_of_wss[0]*wavelength) * (table_weekend[x]/100))))
		print  "\nAt different times we use the following small cells:\n" + str(table_save_sc_3share)
		print  "\nAt different times we use the following small cells during weekends:\n" + str(table_save_sc_3share_weekend)
	print "\n If we did't share any resources:"
	table_save_not_share_weekday = []
	table_save_not_share_weekend = []
	if pattern_combo == 4:
		for x in range(0, 6):
			table_save_not_share_weekday.append(int(((n_sc_transport) * (table_transport_weekdays[x]/100))+(n_sc_resident * (table_resident_weekdays[x]/100))+(n_sc_office * (table_office_weekdays[x]/100))))
			table_save_not_share_weekend.append(int(((n_sc_transport) * (table_transport_weekend[x]/100))+(n_sc_resident * (table_resident_weekend[x]/100))+(n_sc_office * (table_office_weekend[x]/100))))
		print "During weekdays we use in total:"
		print table_save_not_share_weekday
		print "and during weekends"
		print table_save_not_share_weekend
	elif pattern_combo == 1:
		for x in range(0, 6):
			table_save_not_share_weekday.append(int(((n_sc_transport) * (table_transport_weekdays[x]/100))+(n_sc_office * (table_office_weekdays[x]/100))))
			table_save_not_share_weekend.append(int(((n_sc_transport) * (table_transport_weekend[x]/100))+(n_sc_office * (table_office_weekend[x]/100))))
		print "During weekdays we use in total:"
		print table_save_not_share_weekday
		print "and during weekends"
		print table_save_not_share_weekend
	if pattern_combo == 2:
		for x in range(0, 6):
			table_save_not_share_weekday.append(int(((n_sc_transport) * (table_transport_weekdays[x]/100))+(n_sc_resident * (table_resident_weekdays[x]/100))))
			table_save_not_share_weekend.append(int(((n_sc_transport) * (table_transport_weekend[x]/100))+(n_sc_resident * (table_resident_weekend[x]/100))))
		print "During weekdays we use in total:"
		print table_save_not_share_weekday
		print "and during weekends"
		print table_save_not_share_weekend
	if pattern_combo == 3:
		#print "HERE"
		for x in range(0, 6):
			#print x
			table_save_not_share_weekday.append(int((n_sc_resident * (table_resident_weekdays[x]/100))+(n_sc_office * (table_office_weekdays[x]/100))))
			table_save_not_share_weekend.append(int((n_sc_resident * (table_resident_weekend[x]/100))+(n_sc_office * (table_office_weekend[x]/100))))
		print "During weekdays we use in total:"
		print table_save_not_share_weekday
		print "and during weekends"
		print table_save_not_share_weekend

	#x=['04:00', '08:00', '16:00', '18:00', '20:00', '21:00'],
    #y=sum_save_sc)
    # Add data
	time = ['04:00', '08:00', '16:00', '18:00', '20:00', '21:00']
	print "\n"
	#print sum_save_sc_weekend


	# Create and style traces
	trace0 = go.Scatter(
	    x = time,
	    y = sum_save_sc,
	    name = 'shared_infrastructure',
	    line = dict(
	        color = ('rgb(205, 12, 24)'),
	        width = 4)
	)
	trace1 = go.Scatter(
	    x = time,
	    y = sum_save_sc_weekend,
	    name = 'shared_infrastructure_weekend',
	    line = dict(
	        color = ('rgb(22, 96, 167)'),
	        width = 4,)
	)
	trace2 = go.Scatter(
	    x = time,
	    y = table_save_not_share_weekday,
	    name = 'not_shared_infrastructure',
	    line = dict(
	        color = ('rgb(205, 12, 24)'),
	        width = 4,
	        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
	)
	trace3 = go.Scatter(
	    x = time,
	    y = table_save_not_share_weekend,
	    name = 'not_shared_infrastructure',
	    line = dict(
	        color = ('rgb(22, 96, 167)'),
	        width = 4,
	        dash = 'dash')
	)
	trace4 = go.Scatter(
	    x = time,
	    y = sum_save_sc,
	    name = 'shared_infrastructure',
	    line = dict(
	        color = ('rgb(205, 12, 24)'),
	        width = 4)
	)
	trace5 = go.Scatter(
	    x = time,
	    y = sum_save_sc_weekend,
	    name = 'shared_infrastructure_weekend',
	    line = dict(
	        color = ('rgb(22, 96, 167)'),
	        width = 4,)
	)

	data = [trace0, trace1, trace2, trace3, trace4, trace5]

	# Edit the layout
	layout = dict(title = 'Usage of small cells during weekdays and weekends',
	              xaxis = dict(title = 'Time of day'),
	              yaxis = dict(title = 'Save of Small Cells'),
	              )

	# Plot and embed in ipython notebook!
	fig = dict(data=data, layout=layout)
	py.iplot(fig, filename='styled-line')
else:
	print "ZONG"
