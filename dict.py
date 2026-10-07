d = {"name": "Rohit", "age": 20}
d["city"] = "Delhi"
d.get("phone", "N/A")      # safe lookup, no error if missing
for k, v in d.items():
    print(k, v)
print(d.keys()); print(d.values())