import json

groups = ["دروس پایه",
          "دروس عمومی",
          "دروس اصلی",
          "دروس تخصصی",
          "دروس اختیاری",
          "دروس تمرکز تخصصی"]


def num_maker(s):
    adad = "۰۱۲۳۴۵۶۷۸۹"
    if s in adad:
        return int(adad.find(s))
    else:
        return int(s)


def group_assign(n):
    n = num_maker(n)
    if int(n) <= len(groups):
        return groups[int(n)]
    else:
        return None


classdict = {}
with open("computerITKey.json", "w") as fin:
    while True:
        name = input("unit name> ")
        if name:
            classdict[name] = {}
            className = classdict[name]
            className["name"] = name
            for i, e in enumerate(groups):
                print("{", i, "-", e)
            className["group"] = group_assign(input(name + " - group> "))
            className["vahed"] = num_maker(input(name + " - vahed> "))
            className["before"] = input(name + " - before> ")
            # after has to be made later
            # className["after"] = input(name + " - after> ")
            print("-------------------------------")
            print(className)
            print("+++++++++++++++++++++++++++++++")
        else:
            break
    json.dump(classdict, fin, ensure_ascii=False, indent=8)
