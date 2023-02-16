file_write = open(r"alibabagj_postcode_id_new.txt", "w", encoding="utf-8")
with open(r"alibabagj_postcode_id.txt", "r", encoding="utf-8") as tm_227:
    for i in tm_227:
        s_id = i.strip().split(",")
        county = s_id[3]
        if len(county) == 0:
            s_id[3] = s_id[2]
            file_write.write(",".join(s_id) + "\n")
        else:
            file_write.write(",".join(s_id) + "\n")





