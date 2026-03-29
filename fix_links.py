import re
import os

filepath = 'terms/godhead/jesus-version.draft.md'

with open(filepath, 'r') as f:
    content = f.read()

# Map common virtual paths to physical paths (approximate)
mappings = {
    '/bible/concepts/glory': '../../evolution/1st-c-christians.md',
    '/bible/concepts/name': 'https://biblehub.com/greek/3686.htm',
    '/bible/concepts/word': 'https://biblehub.com/greek/3056.htm',
    '/bible/concepts/sin': 'https://biblehub.com/greek/266.htm',
    '/bible/concepts/righteousness': '../../evolution/1st-c-jesus.md',
    '/bible/concepts/shema': '../../evolution/325-nicaea-creed.md',
    '/bible/concepts/holy': '../holy.draft.md',
    '/bible/concepts/consecration': '../../evolution/1st-c-jesus.md',
    '/bible/concepts/sanctification': '../sanctification.draft.md',
    '/god/father': '../../evolution/325-nicaea-creed.md',
    '/god/son/essence/of-man': '../../evolution/1st-c-jesus.md',
    '/god/son/essence/as-god/claims/glory': '../../evolution/1st-c-christians.md',
    '/god/son/essence/as-god/similarities': '../../evolution/325-nicaea-creed.md',
    '/god/son/essence/not-god/serve-god': '../../evolution/1st-c-jesus.md',
    '/god/son/christ': '../../evolution/1st-c-jesus.md',
    '/god/son': '../../evolution/1st-c-jesus.md',
    '/god/spirit': '../holy.draft.md',
    '/eternal/death': '../../evolution/1233-papal-inquisition.md',
    '/life/faith': 'https://eternal.family.net.za/life/faith',
    '/bible/doctrines/trinitarian': '../godhead.draft.md',
    '/bible/translations/differences/en': 'https://biblehub.com/greek/1722.htm',
    '/god/son/essence/as-god/similarities/act': '../../evolution/1st-c-jesus.md',
    '/god/son/essence/as-god/similarities#jesus-speaks-like-a-father': '../../evolution/1st-c-jesus.md',
    '/god/son/essence/of-man/limitations#jesus-is-not-omnipresent': '../../evolution/1st-c-jesus.md',
    '/god/son/essence/of-man/limitations': '../../evolution/1st-c-jesus.md',
    '/god/son/essence/as-god/incarnation': '../../evolution/1st-c-jesus.md',
}

def replace_link(match):
    text = match.group(1)
    url = match.group(2)
    if url in mappings:
        new_url = mappings[url]
        # Project rule: use .md extension even if it is .draft.md
        if new_url.endswith('.draft.md'):
             new_url = new_url.replace('.draft.md', '.md')
        elif new_url.endswith('.drafts.md'):
             new_url = new_url.replace('.drafts.md', '.md')
        return f'[{text}]({new_url})'
    elif url.startswith('/'):
        # If not in mappings, just keep text
        return text
    return match.group(0)

new_content = re.sub(r'\[([^\]]+)\]\((/[^\)]+)\)', replace_link, content)

with open(filepath, 'w') as f:
    f.write(new_content)
