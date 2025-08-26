
def check_anagrams(input_string_1: str, input_string_2: str) -> bool:

    string_1 = ""
    string_2 = ""

    for char in input_string_1:
        if char!= " ":
            string_1 += char

    string_1 = string_1.lower()          
    print(f'The String_1 without spaces is : {string_1}')


    for char in input_string_2:
        if char!= " ":
            string_2 += char

    string_2 = string_2.lower()           
    print(f'The String_2 without spaces is : {string_2}')
    # return string_1, string_2

    if len(string_1) != len(string_2):
        return False

    freq_string_1_dict = {}
    freq_string_2_dict = {}

    for char in string_1:
        freq_string_1_dict[char] = freq_string_1_dict.get(char, 0) + 1 

    for char in string_2:
        freq_string_2_dict[char] = freq_string_2_dict.get(char, 0) + 1


    if freq_string_1_dict == freq_string_2_dict:
        return True
    else:
        return False     

def are_anagrams_count(s1: str, s2: str) -> bool:
    # Normalize strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    # Count character frequencies
    freq1, freq2 = {}, {}
    
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
    
    # Compare dictionaries
    return freq1 == freq2

def are_anagrams_sort(s1: str, s2: str) -> bool:
    # Normalize strings: lowercase + remove spaces
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # If lengths differ, they can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Compare sorted strings
    return sorted(s1) == sorted(s2)


def main():

        user_input_1 = input("Enter the String 1 :")

        user_input_2 = input("Enter the String 2 :")

        is_anagram = check_anagrams(user_input_1, user_input_2)

        if is_anagram:

            print(f'The String 1 :: {user_input_1} and String 2 :: {user_input_2} are ANAGRAMS')

        else:
            print(f'The String 1 :: {user_input_1} and String 2 :: {user_input_2} are NOT Anagrams')

        # Example usage
        print(are_anagrams_count("listen", "silent"))      # True
        print(are_anagrams_count("triangle", "integral"))  # True
        print(are_anagrams_count("hello", "world"))        # False  

        # Example usage
        print(are_anagrams_sort("listen", "silent"))      # True
        print(are_anagrams_sort("triangle", "integral"))  # True
        print(are_anagrams_sort("hello", "world"))        # False  


if __name__ == '__main__':
    main()

