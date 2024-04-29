# hidden in plain sight
from binascii import hexlify, unhexlify




def reverseObj(obj: dict):
    reved = dict()
    
    for k,v in obj.items():
        reved[v] = k

    return reved


class Hips:
    def __init__(self, custom_map=None):
        if custom_map:
            self.map = map
        else:
            self.map = {
                0: "\n",
                1: " \n",
                2: "  \n",
                3: "   \n",
                4: "    \n",
                5: "     \n",
                6: "      \n",
                7: "       \n",
                8: "        \n",
                8: "         \n",
                9: "          \n",
                "a": "\t\n",
                "b": " \t\n",
                "c": "  \t\n",
                "d": "   \t\n",
                "e": "    \t\n",
                "f": "     \t\n"
            }


    def encode(self, data, file_path):
        self.data = hexlify(str(data).encode()).decode()
        self.data = list(self.data)
        self.chars = []
        self.path = file_path

        try:
            for i in self.data:
                if i.isdigit():
                    self.chars.append(self.map[int(i)])
                else:
                    self.chars.append(self.map[i])

            with open(self.path, 'w') as f:
                f.writelines(self.chars)
        except Exception:
            print("error encoding")


    def decode(self, file_path):
        self.path = file_path

        try:
            with open(self.path, "r") as f:
                data = f.readlines()
                map = reverseObj(self.map)
                r = []
                for l in data:
                    r.append(map[l])

                hx = ""

                for x in r:
                    hx+=str(x)

                res = unhexlify(hx.encode()).decode()
                return res
        except Exception:
            print("error decoding")


x = Hips()


x.encode("This string is hidden in plain sight!", "example.txt")

decoded = x.decode("example.txt")

print(decoded)

