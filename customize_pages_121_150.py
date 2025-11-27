import os

def customize_pages():
    pages_dir = 'pages'
    
    pages_content = {
        "121_🌐_Steem.py": '''import streamlit as st
import requests
import json

st.set_page_config(page_title="Steem", page_icon="🪙")

st.markdown("# 🪙 Steem Blockchain")
st.write("Get global properties of the Steem blockchain.")

if st.button("Get Properties"):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "condenser_api.get_dynamic_global_properties",
            "params": [],
            "id": 1
        }
        response = requests.post("https://api.steemit.com", json=payload)
        if response.status_code == 200:
            data = response.json().get("result", {})
            st.metric("Head Block Number", data.get("head_block_number"))
            st.metric("Total Vesting Fund Steem", data.get("total_vesting_fund_steem"))
            st.metric("Time", data.get("time"))
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "122_🌐_Walltime.py": '''import streamlit as st

st.set_page_config(page_title="Walltime", page_icon="🧱")

st.markdown("# 🧱 Walltime")
st.write("Cryptocurrency exchange info.")

st.info("The Walltime API documentation is currently sparse. Please visit their site.")
st.markdown("[Walltime.info](https://walltime.info/)")
''',

        "123_🌐_Bhagavad_Gita_telugu.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Bhagavad Gita", page_icon="🕉️")

st.markdown("# 🕉️ Bhagavad Gita")
st.write("Read verses from the Bhagavad Gita.")

if st.button("Get Random Verse"):
    try:
        response = requests.get("https://gita-api.vercel.app/random-verse")
        if response.status_code == 200:
            data = response.json()
            # The API structure might vary, adjusting based on common response
            st.subheader(f"Chapter {data.get('chapter_no')}, Verse {data.get('verse_no')}")
            st.markdown(f"**Sanskrit:** {data.get('slok', '')}")
            st.markdown(f"**Translation:** {data.get('transliteration', '')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "124_🌐_Bibleapi.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Bible API", page_icon="📖")

st.markdown("# 📖 Bible Verses")
st.write("Search for Bible verses.")

query = st.text_input("Enter Reference (e.g., John 3:16)", "John 3:16")

if st.button("Get Verse"):
    try:
        response = requests.get(f"https://bible-api.com/{query}")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### {data['reference']}")
            st.markdown(f"*{data['text']}*")
            st.caption(f"Translation: {data['translation_name']}")
        else:
            st.error("Verse not found.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "125_🌐_British_National_Bibliography.py": '''import streamlit as st

st.set_page_config(page_title="British National Bibliography", page_icon="🇬🇧")

st.markdown("# 🇬🇧 British National Bibliography")
st.write("Linked Open Data from the British Library.")

st.info("This API uses SPARQL which is complex for a simple demo. Visit the portal below.")
st.markdown("[BNB Linked Data](http://bnb.data.bl.uk/)")
''',

        "126_🌐_Crossref_Metadata_Search.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Crossref", page_icon="📚")

st.markdown("# 📚 Crossref Metadata Search")
st.write("Search for academic works.")

query = st.text_input("Search Query", "machine learning")

if st.button("Search"):
    try:
        response = requests.get(f"https://api.crossref.org/works?query={query}&rows=5")
        if response.status_code == 200:
            data = response.json()
            items = data["message"]["items"]
            for item in items:
                title = item.get("title", ["Untitled"])[0]
                st.subheader(title)
                st.write(f"**DOI:** {item.get('DOI')}")
                st.write(f"**Publisher:** {item.get('publisher')}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "127_🌐_GurbaniNow.py": '''import streamlit as st
import requests

st.set_page_config(page_title="GurbaniNow", page_icon="🙏")

st.markdown("# 🙏 GurbaniNow")
st.write("Get the daily Hukamnama.")

if st.button("Get Hukamnama"):
    try:
        response = requests.get("https://api.gurbaninow.com/v2/hukamnama/today")
        if response.status_code == 200:
            data = response.json()
            hukam = data.get("hukamnama", [])
            if hukam:
                line = hukam[0]["line"]
                st.markdown(f"### {line['gurmukhi']['unicode']}")
                st.markdown(f"*{line['translation']['english']['default']}*")
            else:
                st.warning("No data available.")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "128_🌐_Open_Library.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Open Library", page_icon="🏛️")

st.markdown("# 🏛️ Open Library Search")
st.write("Search for books in the Open Library.")

query = st.text_input("Book Title", "The Lord of the Rings")

if st.button("Search"):
    try:
        response = requests.get(f"https://openlibrary.org/search.json?q={query}&limit=5")
        if response.status_code == 200:
            data = response.json()
            docs = data.get("docs", [])
            for doc in docs:
                st.subheader(doc.get("title"))
                st.write(f"**Author:** {', '.join(doc.get('author_name', []))}")
                st.write(f"**First Published:** {doc.get('first_publish_year')}")
                if "cover_i" in doc:
                    st.image(f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-M.jpg")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "129_🌐_Penguin_Publishing.py": '''import streamlit as st
import requests
import xml.etree.ElementTree as ET

st.set_page_config(page_title="Penguin Publishing", page_icon="🐧")

st.markdown("# 🐧 Penguin Publishing")
st.write("Search for books published by Penguin.")

query = st.text_input("Author Name", "Grisham")

if st.button("Search"):
    try:
        response = requests.get(f"https://reststop.randomhouse.com/resources/works/?start=0&max=5&expandLevel=1&search={query}", headers={"Accept": "application/json"})
        if response.status_code == 200:
            # The API might return JSON if requested, otherwise XML
            try:
                data = response.json()
                works = data.get("work", [])
                if isinstance(works, dict): works = [works] # Handle single result
                
                for work in works:
                    st.subheader(work.get("titleweb"))
                    st.write(f"**Author:** {work.get('authorweb')}")
                    st.markdown("---")
            except:
                st.warning("Could not parse response (likely XML).")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "130_🌐_Quran.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Quran", page_icon="☪️")

st.markdown("# ☪️ Al-Quran")
st.write("Read verses from the Quran.")

surah = st.number_input("Surah Number", 1, 114, 1)
ayah = st.number_input("Ayah Number", 1, 286, 1)

if st.button("Get Ayah"):
    try:
        response = requests.get(f"http://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad")
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"### {data['data']['text']}")
            st.caption(f"Surah {data['data']['surah']['englishName']}, Ayah {data['data']['numberInSurah']}")
        else:
            st.error("Ayah not found.")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "131_🌐_Quran_Cloud.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Quran Cloud", page_icon="☁️")

st.markdown("# ☁️ Quran Cloud Audio")
st.write("Listen to the Quran.")

surah = st.number_input("Surah Number", 1, 114, 1)

if st.button("Get Audio"):
    try:
        response = requests.get(f"http://api.alquran.cloud/v1/surah/{surah}/ar.alafasy")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data["data"]["englishName"])
            for ayah in data["data"]["ayahs"][:5]: # Limit to first 5 for demo
                st.write(f"Ayah {ayah['numberInSurah']}")
                st.audio(ayah["audio"])
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "132_🌐_Quranapi.py": '''import streamlit as st

st.set_page_config(page_title="Quran API", page_icon="📖")

st.markdown("# 📖 Quran API")
st.write("Another Quran resource.")

st.info("This page is similar to the previous Quran pages. Please use those for full functionality.")
''',

        "133_🌐_Rig_Veda.py": '''import streamlit as st

st.set_page_config(page_title="Rig Veda", page_icon="🕉️")

st.markdown("# 🕉️ Rig Veda")
st.write("Ancient Indian collection of Vedic Sanskrit hymns.")

st.info("The Rig Veda API is currently offline or unstable. Please visit VedaWeb for research.")
st.markdown("[VedaWeb](https://vedaweb.uni-koeln.de/)")
''',

        "134_🌐_Thirukkural.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Thirukkural", page_icon="📜")

st.markdown("# 📜 Thirukkural")
st.write("Classic Tamil text.")

if st.button("Get Random Kural"):
    try:
        response = requests.get("https://api-thirukkural.vercel.app/api?num=rnd")
        if response.status_code == 200:
            data = response.json()
            st.subheader(f"Kural {data.get('number')}")
            st.markdown(f"**Tamil:** {data.get('line1')}\\n{data.get('line2')}")
            st.markdown(f"**English:** {data.get('eng')}")
            st.write(f"**Explanation:** {data.get('eng_exp')}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "135_🌐_Vedic_Society.py": '''import streamlit as st

st.set_page_config(page_title="Vedic Society", page_icon="🕉️")

st.markdown("# 🕉️ Vedic Society")
st.write("Resources on Vedic culture.")

st.info("API endpoint currently unavailable.")
''',

        "136_🌐_Wizard_World.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Wizard World", page_icon="🧙")

st.markdown("# 🧙 Wizard World (Harry Potter)")
st.write("Explore spells from the Wizarding World.")

if st.button("Get Random Spell"):
    try:
        response = requests.get("https://wizard-world-api.herokuapp.com/Spells")
        if response.status_code == 200:
            spells = response.json()
            if spells:
                import random
                spell = random.choice(spells)
                st.header(spell['name'])
                st.write(f"**Incantation:** {spell.get('incantation', 'Unknown')}")
                st.write(f"**Effect:** {spell.get('effect', 'Unknown')}")
                st.write(f"**Type:** {spell.get('type', 'Unknown')}")
                st.write(f"**Light:** {spell.get('light', 'None')}")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "137_🌐_Wolne_Lektury.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Wolne Lektury", page_icon="🇵🇱")

st.markdown("# 🇵🇱 Wolne Lektury")
st.write("Free Polish Literature.")

if st.button("Get Random Book"):
    try:
        # Fetching a known book for demo as random endpoint isn't direct
        response = requests.get("https://wolnelektury.pl/api/books/studnia-i-wahadlo/")
        if response.status_code == 200:
            book = response.json()
            st.header(book['title'])
            st.write(f"**Author:** {book['authors'][0]['name']}")
            st.image(book['cover'], use_column_width=True)
            st.markdown(f"[Read Online]({book['url']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "138_🌐_Tenders_in_Hungary.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Tenders Hungary", page_icon="🇭🇺")

st.markdown("# 🇭🇺 Tenders in Hungary")
st.write("Latest government tenders.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/hu/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "139_🌐_Tenders_in_Poland.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Tenders Poland", page_icon="🇵🇱")

st.markdown("# 🇵🇱 Tenders in Poland")
st.write("Latest government tenders.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/pl/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "140_🌐_Tenders_in_Romania.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Tenders Romania", page_icon="🇷🇴")

st.markdown("# 🇷🇴 Tenders in Romania")
st.write("Latest government tenders.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/ro/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "141_🌐_Tenders_in_Spain.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Tenders Spain", page_icon="🇪🇸")

st.markdown("# 🇪🇸 Tenders in Spain")
st.write("Latest government tenders.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/es/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "142_🌐_Tenders_in_Ukraine.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Tenders Ukraine", page_icon="🇺🇦")

st.markdown("# 🇺🇦 Tenders in Ukraine")
st.write("Latest government tenders.")

st.info("The API for Ukraine tenders might be intermittent due to current events.")

if st.button("Fetch Tenders"):
    try:
        response = requests.get("https://tenders.guru/api/ua/tenders")
        if response.status_code == 200:
            data = response.json()
            for tender in data['data'][:5]:
                st.subheader(tender['title'])
                st.write(f"**Date:** {tender['date']}")
                st.write(f"**Category:** {tender['category_name']}")
                st.markdown("---")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "143_🌐_Church_Calendar.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Church Calendar", page_icon="⛪")

st.markdown("# ⛪ Church Calendar")
st.write("Catholic liturgical calendar.")

if st.button("Get Today's Calendar"):
    try:
        response = requests.get("http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today")
        if response.status_code == 200:
            data = response.json()
            st.subheader(data["date"])
            st.write(f"**Season:** {data['season']}")
            st.write(f"**Celebrations:**")
            for cel in data['celebrations']:
                st.write(f"- {cel['title']} ({cel['colour']})")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "144_🌐_Czech_Namedays_Calendar.py": '''import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Czech Namedays", page_icon="🇨🇿")

st.markdown("# 🇨🇿 Czech Namedays")
st.write("Find out who has a nameday today in Czechia.")

if st.button("Get Nameday"):
    try:
        today = datetime.date.today()
        response = requests.get(f"https://svatky.adresa.info/json?date={today.strftime('%d%m')}")
        if response.status_code == 200:
            data = response.json()
            # API returns list of entries
            names = [entry['name'] for entry in data]
            st.success(f"Today's Nameday: {', '.join(names)}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "145_🌐_Hebrew_Calendar.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Hebrew Calendar", page_icon="🕎")

st.markdown("# 🕎 Hebrew Calendar")
st.write("Convert dates to Hebrew calendar.")

if st.button("Get Today's Hebrew Date"):
    try:
        response = requests.get("https://www.hebcal.com/converter?cfg=json&gy=2023&gm=10&gd=25&g2h=1") # Using fixed date for demo or current
        # Better: use current date
        import datetime
        now = datetime.datetime.now()
        url = f"https://www.hebcal.com/converter?cfg=json&gy={now.year}&gm={now.month}&gd={now.day}&g2h=1"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.header(data["hebrew"])
            st.write(f"**Year:** {data['hy']}")
            st.write(f"**Month:** {data['hm']}")
            st.write(f"**Day:** {data['hd']}")
            st.write(f"**Events:** {', '.join(data['events'])}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "146_🌐_LectServe.py": '''import streamlit as st
import requests

st.set_page_config(page_title="LectServe", page_icon="📖")

st.markdown("# 📖 LectServe")
st.write("Lectionary for the day.")

if st.button("Get Lectionary"):
    try:
        response = requests.get("http://www.lectserve.com/u/json/today")
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Date:** {data.get('date')}")
            # Note: Response structure varies, printing raw for safety if simple keys missing
            st.json(data)
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "147_🌐_NagerDate.py": '''import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Nager.Date", page_icon="📅")

st.markdown("# 📅 Public Holidays")
st.write("Global public holidays.")

country = st.text_input("Country Code (e.g., US, GB, AT)", "US")
year = st.number_input("Year", 2020, 2030, datetime.datetime.now().year)

if st.button("Get Holidays"):
    try:
        response = requests.get(f"https://date.nager.at/api/v3/publicholidays/{year}/{country}")
        if response.status_code == 200:
            holidays = response.json()
            for holiday in holidays:
                st.write(f"**{holiday['date']}:** {holiday['name']} ({holiday['localName']})")
        else:
            st.error("API Error (Invalid Country Code?)")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "148_🌐_Namedays_Calendar.py": '''import streamlit as st
import requests

st.set_page_config(page_title="Namedays", page_icon="🎉")

st.markdown("# 🎉 Namedays")
st.write("Find namedays for different countries.")

country = st.selectbox("Country", ["us", "cz", "sk", "pl", "fr", "hu", "hr", "se", "at", "it", "es", "de"])
day = st.number_input("Day", 1, 31, 1)
month = st.number_input("Month", 1, 12, 1)

if st.button("Check Nameday"):
    try:
        response = requests.get(f"https://api.abalin.net/namedays?country={country}&day={day}&month={month}")
        if response.status_code == 200:
            data = response.json()
            names = data.get("data", {}).get("namedays", {}).get(country)
            st.success(f"Nameday in {country.upper()}: {names}")
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Error: {e}")
''',

        "149_🌐_NonWorking_Days.py": '''import streamlit as st

st.set_page_config(page_title="NonWorking Days", page_icon="🏖️")

st.markdown("# 🏖️ NonWorking Days")
st.write("Database of non-working days.")

st.info("This API is similar to Nager.Date. Please use the Public Holidays page for better results.")
''',

        "150_🌐_NonWorking_Days_150.py": '''import streamlit as st

st.set_page_config(page_title="NonWorking Days II", page_icon="🏖️")

st.markdown("# 🏖️ NonWorking Days II")
st.write("Database of non-working days.")

st.info("Duplicate entry. Please use the Public Holidays page.")
'''
    }

    for filename, content in pages_content.items():
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Customized {filename}")

if __name__ == "__main__":
    customize_pages()
