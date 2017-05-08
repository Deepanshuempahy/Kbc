# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Question 1
# Ab aap 10 aur questions, unke options and keys add karo apni lists mei





questions = ["1 How many days in a weake","2 How many student in this class room","3 How many botels in the Friz","4 How many pillos in the Navgurukul","5 How many state in india","6 What is the capital of panjab","7 what is the capital is India","8 Who is the most powerfull in the world","9 Who is the most powerfull country in the world","10 Where is navgurukul","11 Who is the first indian women go in space","12 Who is the caption of cricket team","13 who is the first woman president of india","14 who is the first president of india rajinder"]




Pehli_list =[10,50,"26bottles","20pillos","34","Bihar","Delhi","Donal trmped","Dubai","Gajia bad","saniya mirza","Ms Dhoni", "savatri bai phuley","Dr Bheem raw Ambadger",]
Doosri_list =[20,12,"18bottels","30pillos","29","up","utrakhand","Modi","U S A","Delhi","Kalpana chavala","Shavag","Partibha patil","Rajander parshad",]
Teesri_list =[7,90,"80boyttles","7pillos","50","Chandigar","Aagara","Khali","Russia","Hariyana","Ketrina keff","Virath kohli","Indra gandhi","Javar lal nehru"]
Chauthi_list =[12,100,"190bottles","68pillos","20","Hariyana","Madhey pardesh","Under taker"."Pakisthan","Punjab","Mery kon","Krish gaill","Soniya gandhi","Abdul klam"]






# Queston 2
# Ab aap apne KBC game mei har ek question ka alag alag prize rakhoge
# jaise pehle question ke liye 1000 INR, doosre question ke liye 2000 INR ...
# 1 - 1000
# 2 - 2000
# 3 - 3000
# 4 - 5000
# 5 - 10000
# 5 questions ke baad likho "Congrats! Aapka padaav pura ho gaya hai."
# 6 - 20000
# 7 - 40000
# 8 - 80000
# 9 - 160000
# 10 - 320000
# 10 questions ke baad print karo "Congrats! Aapka doosra padaav pura ho gaya hai."
# 11 - 640000
# 12 - 1250000
# 13 - 2500000
# 14 - 5000000
# 15 - 1000000
# 15 questions ke baad print karo "Congrats! Aap ek crore rupye jeet gaye hai."



questions = [" How many days in a weake"," How many student in this class room"," How many botels in the Friz"," How many pillos in the Navgurukul"," How many state in india"," What is the capital of panjab"," what is the capital is India"," Who is the most powerfull in the world"," Who is the most powerfull country in the world"," Where is navgurukul"," Who is the first indian women go in space"," Who is the caption of cricket team"," who is the first woman president of india"," who is the first president of india","Who is the borne of terarist"]


Var1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
Answer_list = (2,1,1,1,1,2,0,0,1,1,1,2,1,1,1,3)
Prize_list = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000)




Pehli_list =["10","50","26bottles","20pillos","34","Bihar","Delhi","Donal trmped","Dubai","Gajia bad","saniya mirza","Ms Dhoni", "savatri bai phuley","Dr Bheem raw Ambadger","Dubai"]
Doosri_list =["20","12","18bottels","30pillos","29","up","utrakhand","Modi","U S A","Delhi","Kalpana chavala","Shavag","Partibha patil","Rajander parshad","Izrahil"]
Teesri_list =["7","90","80boyttles","7pillos","50","Chandigar","Aagara","Khali","Russia","Hariyana","Ketrina keff","Virath kohli","Indra gandhi","Javar lal nehru","India"]
Chauthi_list =["12","100","190bottles","68pillos","20","Hariyana","Madhey pardesh","Under taker","Pakisthan","Punjab","Mery kon","Krish gaill","Soniya gandhi","Abdul klam","Pakisthan"]



for index in range(15):
	print "Aapka",Var1[index],"Yeh hai"
	print questions[index]
	print Pehli_list[index]	
	print Doosri_list[index]
	print Teesri_list[index]
	print Chauthi_list[index]
	Var3 = int(raw_input("Answer dallo\n"))
	if Var3 == Answer_list[index]:
		print "congrats Aapka jabvab sahi hai"
	else:
		print "Afsos aapka javab galat hai"
	if Var3 == Answer_list[index]:
		print "Aap" ,Prize_list[index],	"jit chukey hain"
	if Prize_list[index] == 10000:
		print "Congrats! Aapka padaav pura ho gaya hai."
	if Prize_list[index]== 3200000:
		print "Congrats! Aapka doosra padaav pura ho gaya hai."
	if Prize_list[index]== 10000000:
		print "Congrats! Aap ek crore rupye jeet gaye hai."










