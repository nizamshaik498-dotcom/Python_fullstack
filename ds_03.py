#SET

visitors={"wahid","Nizam","Althaf","Raihan"}
print(visitors)
empty_set=set()
raw=[1,2,2,3,3,3]
unique=list(set(raw))
print("Wahid" in visitors)
print(len(visitors))
visitors.add("Alex")
visitors.update(["Ram","Mrunal"])
visitors.remove("Raihan")
visitors.discard("ghost")
visitors.pop()
cs_students={"wahid","Nizam","Althaf","Raihan"}
web_students={"Nizam","Althaf","Raihan"}
print(cs_students & web_students)
print(cs_students | web_students)
print(cs_students - web_students)
print(cs_students ^ web_students)