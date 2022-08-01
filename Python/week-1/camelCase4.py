from re import findall


def camelCase(items):
    for item in items:
        # item = str(item)
        parts = item.split(';')

        if parts[0] == 'S':
            if parts[1] in ['V', 'M']:
                part = str(parts[2]).replace('()', '')
                combined = ''
                for i in range(len(part)):
                    if part[i].isupper():
                        combined += f" {part[i].lower()}"
                    else:
                        combined += part[i]

                print(f"{combined}")

            elif parts[1] == 'C':
                splitted = findall('[A-Z][^A-Z]*', parts[2])
                combined = ' '.join(x.lower() for x in splitted)
                print(f"{combined}")

        elif parts[0] == 'C':
            if parts[1] == 'M':
                combined = ''.join(x.lower() if idx == 0 else x for idx, x in enumerate(parts[2].title()) if not x.isspace())
                print(f"{combined}()")

            elif parts[1] == 'V':
                combined = ''.join(x.lower() if idx == 0 else x for idx, x in enumerate(parts[2].title()) if not x.isspace())
                print(f"{combined}")

            elif parts[1] == 'C':
                combined = ''.join(x for x in parts[2].title() if not x.isspace())
                print(f"{combined}")

if __name__ == '__main__':
    inputs = [
        "S;M;plasticCup()",
        "C;V;mobile phone",
        "C;C;coffee machine",
        "S;C;LargeSoftwareBook",
        "C;M;white sheet of paper",
        "S;V;pictureFrame"
    ]

    camelCase(inputs)
