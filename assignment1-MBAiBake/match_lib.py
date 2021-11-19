def match(pattern, source):
    pind = 0
    sind = 0
    response = []

    while sind < len(source) or pind < len(pattern):
        if pind == len(pattern):
            return None
        elif pattern[pind] == '%':
            if pind == len(pattern) - 1:
                end = ' '.join(source[sind:len(source)])
                response.append(end)
                return response
            else:
                pind += 1
                accumulator = ""
                while source[sind] != pattern[pind]:
                    accumulator += source[sind] + " "
                    sind += 1
                    if len(source) - sind == 0:
                        return None
                accumulator = accumulator.rstrip()
                response.append(accumulator)
        elif sind == len(source):
            return None
        elif pattern[pind] == '_':
            response.append(source[sind])
            sind += 1
            pind += 1
            continue
        elif source[sind] == pattern[pind]:
            sind += 1
            pind += 1
            continue
        else:
            return None
    return response

if __name__ == '__main__':
    print(match(["x", "_", "_"], ["x", "y", "z"]))
    #print(match(["x", "%", "z"], ["x", "y", "z"]))
    #print(match(["%", "z"], ["x", "y", "z"]))
    #print(match(["x", "%", "y"], ["x", "y", "z"]))
    #print(match(["x", "%", "y", "z"], ["x", "y", "z"]))
    #print(match(["x", "y", "z", "%"], ["x", "y", "z"]))
    #print(match(["_", "%"], ["x", "y", "z"]))