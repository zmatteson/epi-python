import collections 

def check_constructible(letter, magazine):
    l_counter = collections.Counter(letter)
    m_counter = collections.Counter(magazine)
    return not(l_counter - m_counter)

if __name__ == '__main__':
    letter = 'I am Zeb'
    magazine = 'I am Zeb and I really would love working at Google'
    print(check_constructible(letter, magazine))