from GameEngine.Util.KeyboardManager import KeyboardManager

km = KeyboardManager("file.txt")

for k,v in km.config.items():
	print(k+", "+v)

#km.write_config("file.txt")


print(km.on_keys(["W","S","A"]))
print(km.on_keys(["W","S","A"]))
print(km.on_keys(["W","S"]))

print(km.on_keys(["W","S","A"]))
print(km.on_keys(["D"]))
