from src.lookups import all_industries

weird_indus_codes = [10,101,1011,1012,1013,102,1021,1022,1023,1024,1025,1026,1027,1028,1029]

indus_temp = all_industries
weird_indus = []
gen1_indus = []
gen2_indus = [] 
gen3_indus = [] 
gen4_indus = [] 
gen5_indus = []  


for code in weird_indus_codes:
    weird_indus.append(indus_temp[code])
    del indus_temp[code]

for code, title in indus_temp.items():
    if code < 100:
        gen1_indus.append(code)
    elif code < 1000:
        gen2_indus.append(code)
    elif code < 10000:
        gen3_indus.append(code)
    elif code < 100000:
        gen4_indus.append(code)
    elif code < 1000000:
        gen5_indus.append(code)



generation_dict = {1:gen1_indus,
2:gen2_indus,
3:gen3_indus,
4:gen4_indus,
5:gen5_indus}

print(generation_dict)



