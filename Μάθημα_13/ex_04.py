def pogchamp_situation(*poggers, **poggers2):
    s = 0
    my_dict = {}
    for pepega in poggers:
        s += int(pepega)

    for key, value in poggers2.items():
        if value in my_dict:
            my_dict[value] += (", " + key)
        else:
            my_dict[value] = key

    print(f"The total sum of grades is: {s}\nThe average grade of students is: {s / len(poggers)}")
    print(my_dict)


pogchamp_situation(18, 20, 20, 19, 13, Tsantalis="Math", Tsiamitas="Programming",
                   Karakasis="Programming", Mamaras="Philology", Gkaros="Physics")

