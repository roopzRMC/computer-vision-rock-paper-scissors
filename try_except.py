# %%
with open('labels.txt') as f:
    print(f.read())
f.close()
# %% 
## use try except to look for a non existent file and if its nor there - create it 
try:
    with open('test.txt') as tfile:
        print(tfile.read())
    tfile.close()
except:
    print('file not found')
    with open('test.txt', 'w') as tfile:
        tfile.write('Hello, i am a file')
    tfile.close()
# %%