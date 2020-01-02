import random


class CodeMachine:
    def __init__(self, letterTable):
        self.letterTable = letterTable

    def decode(self, encodedMessage, key=12):
        decodedMsg = []

        for i in range(len(encodedMessage)):
            encodedMessage[len(encodedMessage) - 1 - i] = \
                ((encodedMessage[len(encodedMessage) - 1 - i] - len(self.letterTable)) % len(dictionary)) - key

        for j in range(len(encodedMessage)):
            index = encodedMessage[j]
            decodedMsg.append(dictionary[index])
        print(encodedMessage)
        print(len(encodedMessage))
        print(decodedMsg)
        print(len(decodedMsg))
        print("".join(decodedMsg))
        return dictionary

    def encode(self, plainMsg, key=12):
        encodedMessage = []
        messageInCharArray = list(plainMsg)

        for i in range(len(messageInCharArray)):
            randomNumber = random.randint(-100, 100)

            try:
                # Number of correspondence in the char-array
                current = self.letterTable.index(messageInCharArray[i])
            except ValueError:
                print("Warning: Could not find the letter "
                      + messageInCharArray[i] + "in the configured messageInCharArray!")
            else:
                # Number of correspondence in the char-array + random number + 30 + 0
                current += randomNumber * len(self.letterTable) + key
                encodedMessage.append(current)

        print(encodedMessage)
        return encodedMessage


dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', '-', '.', '/', '_']

coder = CodeMachine(dictionary)

encodedMsg = [3064, -1526, -1886, -1641, -1287, -857, -2430, -1221, -1068, -495, 1404, -1690, -1595, 339, -2176, 1399,
              2560, -940, -2609, 1870, -2475, -2685, 2997, -1380, 460, -915, 762, 2971, 2186, -61, -2054, 968, 83,
              -1278, -1077, 1646, 2489, -1504, -770, 357, -2041, 1796, 2417, 76, 2640, -1590, 1940, 1736, 1345, -2260,
              1748, -460, -1895, -1663, -1924, 1649, 1674, -2088, -809, -1330, -1156, 529, -1304, -1761, 889, -2879,
              1074, -787]

coder.decode(encodedMsg)
