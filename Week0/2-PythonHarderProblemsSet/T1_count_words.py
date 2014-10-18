def count_words(arr):
    count_of_words = {}
    for word in arr:   # trqbva da sloja chek ako veche e vkarana edin put dumata v dictionary da ne q vkarva vtori put
        # trqbva da si dobavq proverki za prazen i za chisla (eventualno)
        count_of_words[word] = arr.count(word)
    return count_of_words

print (count_words(["python", "python", "python", "ruby"]))
