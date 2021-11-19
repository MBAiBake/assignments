def match(pattern, source):
    """Attempt to match pattern to source. % matches a sequence of zero or
        more words and _ matches any single word.

    Args:
        pattern - a list of strings. % and/or _ are utilized as placeholder
                  to match/extract words from the source
        source - a list of string. A phrase/sentence/question represented as
                 a list of words (strings).

    Returns:
        if a match is detected, returns a list of strings - a list of matched
        words (words in the source corresponding to _'s or %'s, in the
        pattern, if any).
        else if no match is detected, returns None. 

    """
    sind = 0      #current index we are looking at in the source list
    pind = 0      #current index we are looking at in the pattern list
    result = []   #a place to store the substitutions that we will 
    			         #return if matched
    accumulator = "" #a place to store a substitution for a %
    	         #that we are currently collecting
    accumulating = False #a boolean to tell us whether or 
    		         #not we are currently storing up a % substitution
    while True:
        #1) if we are at the end of the pattern and the source 
        if len(pattern) == pind and len(source) == sind:
        # Both lists end simultaneously: clean up and return
            if accumulating:
                result = result + [accumulator.strip()]
            return result
        #2) if we are just at the end of the pattern but not the source
        elif len(pattern) == pind:
            if accumulating:
                accumulator = accumulator + " " + source[sind]
                sind = sind + 1
            else:
                return None
        #3) if we encounter a %
        elif pattern[pind] == "%":
            accumulating = True
            accumulator = ""
            pind = pind + 1
        #4) if we are at the end of the source
        elif len(source) == sind:
            return None
        #5) if we encounter an _
        elif pattern[pind] == "_":
            result = result + [source[sind]]
            pind = pind + 1
            sind = sind + 1
        #6) if current items are equal
        elif pattern[pind] == source[sind]:
            if accumulating:
               accumulating = False
               result = result + [accumulator.strip()]
            pind = pind + 1
            sind = sind + 1
        #7) current items are unequal
        else:
            if accumulating:
                accumulator = accumulator + " " + source[sind]
                sind = sind + 1
            else:
                return None
