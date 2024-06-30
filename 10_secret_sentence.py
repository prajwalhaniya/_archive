'''
Luka is writing a secret sentence in class. He doesn’t want the teacher to be
able to read it, so instead of writing down the original sentence, he writes
down an encoded version. After each vowel in the sentence (a, e, i, o, or u),

he adds the letter p and that vowel again. For example, rather than write
down the sentence i like you, he would write ipi lipikepe yopoupu.
The teacher acquires Luka’s encoded sentence. Recover Luka’s original
sentence for the teacher.
'''

sentence = input()

result = ''
i = 0

while i < len(sentence):
    result += sentence[i]
    if sentence[i] in 'aeiou':
        i += 3
    else:
        i += 1

print(result)