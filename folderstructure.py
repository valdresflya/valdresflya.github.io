#%%
import os
import glob
import json

#%%
dir = [e.path for e in os.scandir("./images/") if e.is_dir()]

# %%
li = []
for e in dir:
    pat=e+'/*.jpg'
    name=e[9:]
    print(pat)
    files=[e2.replace("\\","/") for e2 in glob.glob(pat)]
    subdic = {"source":e, "front":files[0],"name":name,"childList":files}
    li.append(subdic)
dic = { "structure":li}

#%%
print(dic)
# %%
with open("../src/assets/sample.json", "w") as outfile:
    json.dump(dic, outfile)

# %%

# %%
