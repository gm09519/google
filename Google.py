from google import search
out=open("new_data.txt","w")
for title in search('<google dork>', stop=100):
            print(title)
            out.write(title)
            out.write("\n")
out.close()