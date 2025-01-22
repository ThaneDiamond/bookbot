def main():
        
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
    def word_count(text):
        words = text.split()
        return len(words)
        
    def letter_count(text):
        alphabet_count = {}
        for letter in text.lower():
            alphabet_count[letter] = alphabet_count.get(letter, 0) + 1
        return alphabet_count

    def sort_on(dict):
        return dict["num"]


    def report_print():
        alphabet_count = letter_count(file_contents)
        alphabet_list = []

        for entry in alphabet_count:
            alphabet_list.append(entry)
                
                

        print("Begin report of books/frankenstein.txt")
        print(word_count(file_contents)) 
        for entry in alphabet_list:
            for item in entry:
                if item.isalpha(): 
                    num = alphabet_count[item]
                    print(f"the '{item}' character was found {num} times") 
        
    report_print()


main()