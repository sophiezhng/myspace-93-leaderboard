import json
import requests
import time

limit = 100
# Write is formatted for .md files
path_to_file = "index.md"

def main():
    sorted_users = get_users()
    f = open(path_to_file, "w")
    count = 1
    f.write("Last updated: {{ \"now\" | date: site.date_format }}\n\nPlace | Name | Country | # of Fwiends\n| --- | --- | --- | --- |\n")
    for item in sorted_users[:limit]:
        time.sleep(11)
        r = requests.get('https://myspace.windows93.net/api.php?id='+item[0])
        check_stat(r)
        user = r.json()
        f.write("\#"+str(count)+" | "+user["name"]+" | "+user["country"]+" | "+str(item[1]["fwiends"])+"\n")
        count+=1
    f.write("\nFork the source code [here](https://github.com/sophiezhng/myspace-93-leaderboard)")
    f.close()
            
def get_users():
    r = requests.get('https://myspace.windows93.net/api.php')
    check_stat(r)
    json = r.json()["fwiends"]
    sorted_list = sorted(json.items(), key=lambda x: x[1]["fwiends"], reverse=True)
    return sorted_list[:limit]

def check_stat(request):
    if request.json()["success"] == False:
        exit(1)

if __name__ == "__main__":
    main()
