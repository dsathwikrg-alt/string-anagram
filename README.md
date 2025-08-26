# string-anagram
Check if two strings are anagrams or NOT.

Example: dictionary access vs definition
freq1 = {}                # define empty dictionary
freq1['a'] = 1            # assign key 'a'
print(freq1['a'])         # access key 'a' → 1


If you try:

freq1{a} = 1   # ❌ invalid


#################################################################


Example: "Apple" (lowercased → "apple")
s1 = "apple"
freq1 = {}

for char in s1:
    freq1[char] = freq1.get(char, 0) + 1

Iteration 1 → char = 'a'

freq1.get('a', 0) → not found, so 0

0 + 1 = 1

Update: freq1['a'] = 1

Now:

freq1 = {'a': 1}

Iteration 2 → char = 'p'

freq1.get('p', 0) → not found, so 0

0 + 1 = 1

Update: freq1['p'] = 1

Now:

freq1 = {'a': 1, 'p': 1}

Iteration 3 → char = 'p' again

freq1.get('p', 0) → already exists, value is 1

1 + 1 = 2

Update: freq1['p'] = 2

Now:

freq1 = {'a': 1, 'p': 2}

Iteration 4 → char = 'l'

freq1.get('l', 0) → not found → 0

0 + 1 = 1

Update: freq1['l'] = 1

Now:

freq1 = {'a': 1, 'p': 2, 'l': 1}

Iteration 5 → char = 'e'

freq1.get('e', 0) → not found → 0

0 + 1 = 1

Update: freq1['e'] = 1

Final dictionary:

freq1 = {'a': 1, 'p': 2, 'l': 1, 'e': 1}

✅ Why p did not reset to 0

Because:

On second time when char = 'p', the dictionary already had 'p': 1 from the previous iteration.

So freq1.get('p', 0) returned 1 (not 0).

Then 1 + 1 = 2 was stored.

👉 Each loop iteration looks at the current dictionary contents, not a fresh dictionary.

⚡ In short:

The first time a character is seen → get() falls back to 0.

Every next time → it retrieves the stored count, increments it, and updates the dictionary.

#################################################################

🔹 Interview Tip

If asked for efficiency, use the frequency count approach (O(n)).

If asked for simplicity, use the sorting approach (less code).