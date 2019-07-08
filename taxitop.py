import json
companys = [{
			"plan": 160000,
			"start_date": 1562410302,
			"validity": 30,
            "total_adds":2,
			"adds": ["add", "add1"]
},{
			"plan": 160000,
			"start_date": 1562410302,
			"validity": 30,
            "total_adds":3,
			"adds": ["add", "add1", "add2"]
},{
			"plan": 160000,
			"start_date": 1562410302,
			"validity": 30,
            "total_adds":4,
			"adds": ["add", "add1", "add2", "add3"]
},{
			"plan": 160000,
			"start_date": 1562410302,
			"validity": 30,
            "total_adds":5,
            "adds": ["add", "add1", "add2", "add3","add4"]
},{
			"plan": 160000,
			"start_date": 1562410302,
			"validity": 30,
            "total_adds":6,
			"adds": ["add", "add1", "add2", "add3","azd4","amd4"]
}]

cabs = [{
        "total_slots":2400,
        "running_time":8
},{
        "total_slots":2400,
        "running_time":8
},{
        "total_slots":2400,
        "running_time":8
},{
        "total_slots":2400,
        "running_time":8    
},{
        "total_slots":2400,
        "running_time":8
}]
    
print(len(cabs),len(companys))

def calculateTotaladds():
    total = 0
    for x in companys:
        total = total +x['total_adds']
    return total
def calculateTotalCabSlots():
    total = 0
    for x in cabs:
        total = total + x['total_slots']
    return total

def addAndAabSloats():
    total_slots = calculateTotalCabSlots();
    total_adds = calculateTotaladds();
    formAddOverSlotes()
    print(total_adds,total_slots);

def formAddOverSlotes():
    total =[]
    list_companies =[]
    for company in companys:
        for i,add in enumerate(company['adds']):
            info = {
                "add": add,
                "index": i
            }
            total.append(info)
    total.sort(key=lambda x:x['index'])
    final_adds = []
    for tot in total:
        final_adds.append(tot['add'])
    print(final_adds)
addAndAabSloats()