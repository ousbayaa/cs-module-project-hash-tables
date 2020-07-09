def word_count(s):
    # Your code here
    if len(s) == 0:
        return {}
    bad = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "'", "\\"]
    for i in bad:
        if i in s:
            s = s.replace(i,"")
    dictionary = {}
    answer = s.lower()
    answer = answer.split()
    counter = 1
    for each in answer:
        if each in dictionary:
            dictionary[each] += 1
        else:
            dictionary[each] =counter
    return dictionary

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))