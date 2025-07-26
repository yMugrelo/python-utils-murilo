favortite_languages = {
    'jen' : ['python', 'ruby'],
    'kevin' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}
print("table favortite language:")
for name, language in favortite_languages.items():
    language_str = ", ".join(language)
    print(f"\t{name}'s favorite language is: {language_str}.\n")