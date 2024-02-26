translation_table = str.maketrans({
    "“": "\"",
    "”": "\"",
    "’": "\'",
    "‘": "\'",
    "—": " &#8212; ",
    "…": "..."
})

while True:
    try:
        url = input('\nUrl: ').strip() # From Bible Gateway
        version = url.split('&version=')[1]
        
        ref = url.split('?search=')[1].split('&version=')[0]
        ref = ref.replace('+', ' ').replace('%3A', ':').title()

        first_verse = ref.split(':')[1].split('-')[0] if '-' in ref else ref.split(':')[1]
        verse = input("Verse: ").strip().translate(translation_table)

        print(f'\n<!--{ref}--><p><sup>{first_verse} </sup>{verse} <nobr><a href="{url}" target="_blank">{ref}</a> ({version})</nobr></p>\n')
        print(f'<nobr><a href="{url}" target="_blank">{ref}</a></nobr>\n')           
    except IndexError:
        print("\nError Occured.\n")
