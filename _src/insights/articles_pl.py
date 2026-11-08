"""Polish versions of the Insights articles (translated 8 Nov 2026 from articles.py).
Keep facts, dates, figures and sources in step with the English originals."""
from datetime import date
import charts
from charts import bars, line, stack
from articles import src, table

TOPIC = "Biometan"
MON = ["sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz", "paź", "lis", "gru"]


def exhibit(n, title, body, source, note=""):
    note_html = f'<p class="ex-note">{note}</p>' if note else ""
    return (f'<figure class="exhibit"><figcaption><span class="ex-num">Wykres {n}</span>'
            f'<span class="ex-title">{title}</span></figcaption>'
            f'<div class="ex-body">{body}</div>{note_html}'
            f'<p class="ex-source">Źródło: {source}</p></figure>')


def ym(d):
    return f"{MON[d.month - 1]} {d.year % 100}"


def link(t, u):
    return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'


charts.NUM.update(group=" ", dec=",")

# ---------------------------------------------------------------- 1
P1_TTF = line(
    [(date(2025, 9, 1), 32.06, None), (date(2025, 11, 3), 31.87, None),
     (date(2026, 2, 27), 32.1, None), (date(2026, 3, 24), 54.04, "54"),
     (date(2026, 4, 1), 47.51, None), (date(2026, 5, 1), 45.96, None),
     (date(2026, 6, 1), 47.41, None), (date(2026, 7, 1), 43.60, None),
     (date(2026, 8, 3), 57.49, None), (date(2026, 9, 1), 71.77, None),
     (date(2026, 10, 22), 89.0, "89")],
    "Cena gazu TTF w Holandii, wrzesień 2025 – październik 2026, EUR/MWh",
    unit=" EUR/MWh", notes=[(date(2026, 2, 27), "Początek konfliktu")], month_fmt=ym)

P1 = dict(
    title="Szok gazowy w Europie w 2026 r. i argumenty za krajowym gazem",
    short="Szok gazowy 2026",
    standfirst="Cena gazu TTF wzrosła od lutego niemal trzykrotnie. Biometan przestał być wyłącznie narzędziem klimatycznym i stał się kwestią bezpieczeństwa dostaw, a to zmienia, kto go kupuje i dlaczego.",
    keypoints=[
        "22 października 2026 r. TTF zbliżył się do 89 EUR/MWh, o 177% więcej niż w lutym, gdy wybuchł konflikt na Bliskim Wschodzie.",
        "Emisje są dziś wyceniane nie tylko wewnątrz UE, ale też na granicy: pierwsza cena certyfikatu CBAM, opublikowana w kwietniu, wyniosła 75,36 EUR/t CO₂.",
        "Plan AccelerateEU Komisji Europejskiej wymienia biometan jako krajowe źródło dostaw. Spodziewamy się, że odbiorcy zaczną traktować go jako zasób zabezpieczający dostawy, a nie tylko jako atrybut ekologiczny.",
    ],
    seo="Cena gazu TTF wzrosła w 2026 r. o 177%. Jak szok cenowy, CBAM i ETS2 zmieniają wartość krajowego gazu odnawialnego w Europie.",
    keywords="rynek energii w Europie 2026, cena gazu TTF, AccelerateEU, ETS2, biometan, bezpieczeństwo energetyczne",
    body=f"""
<p>Dziesięć miesięcy temu europejski rynek gazu wyglądał spokojnie. Przy rosnących dostawach LNG i wysokim poziomie zapasów kontrakt TTF na najbliższy miesiąc spadł na początku grudnia 2025 r. poniżej 27 EUR/MWh, do najniższego poziomu od 20 miesięcy. Według danych Komisji Europejskiej, na które powołuje się ANSA, 22 października 2026 r. ten sam benchmark zbliżył się do 89 EUR/MWh, o 177% więcej niż w lutym. W lutym wybuchł konflikt z udziałem Iranu, a bezpieczeństwo żeglugi przez Cieśninę Ormuz stanęło pod znakiem zapytania.</p>

{exhibit(1, "Cena gazu TTF, wrzesień 2025 – październik 2026 (EUR/MWh)", P1_TTF,
         src(("minfin.com.ua, dane historyczne TTF", "https://index.minfin.com.ua/markets/gas/ttf/2026-09/"),
             ("Trading Economics", "https://tradingeconomics.com/commodity/eu-natural-gas%20"),
             ("ANSA za SoldiOnline", "https://www.soldionline.it/notizie/forex-commodities/gas-ue-177-da-febbraio-cosa-ce-dietro-il-balzo-del-ttf-a-89-mwh")) + "; Qiao Partners.",
         "Ceny z pojedynczych dni, przeważnie z pierwszego dnia handlowego miesiąca. Cenę z końca lutego wyliczono na podstawie wzrostu o 177% podanego przez Komisję.")}

<h2>Dywersyfikacja zmniejszyła jedno ryzyko, ale odsłoniła inne</h2>
<p>Po 2022 r. Europa zastąpiła rosyjski gaz rurociągowy skroplonym gazem z USA, Kataru i innych krajów, ograniczając zależność od jednego dostawcy. Nie zmniejszyło to jednak zależności od szlaków morskich ani nie zmieniło faktu, że Europa konkuruje z odbiorcami z Azji o te same ładunki. Zakłócenia w 2026 r. sprawdziły właśnie tę ekspozycję.</p>
<p>Dziś na rynku widać trzy zjawiska. Po pierwsze, zmienność cen stała się strukturalna: odbiorcy, którzy budżetowali według krzywej terminowej z grudnia 2025 r., płacą obecnie ponad trzy razy więcej. Po drugie, gaz i uprawnienia do emisji są ze sobą powiązane: kontrakt EUA na grudzień 2026 r. w połowie stycznia osiągnął około 92 EUR/t, a w maju spadł do 74–77 EUR/t, gdy wysokie ceny gazu zmieniły opłacalność zmiany paliwa. Po trzecie, koszt emisji pobierany jest na granicy: CBAM wszedł w fazę docelową 1 stycznia 2026 r., a 7 kwietnia Komisja opublikowała pierwszą kwartalną cenę certyfikatu CBAM: 75,36 EUR/t CO₂.</p>

<h2>Bruksela traktuje biometan jako narzędzie bezpieczeństwa</h2>
<p>Odpowiedź Komisji, AccelerateEU (COM(2026) 370), opublikowano 22 kwietnia 2026 r. Plan łączy krótkoterminowe wsparcie dla gospodarstw domowych i przemysłu z działaniami ograniczającymi zależność od importu paliw kopalnych i wskazuje biometan jako jedno z krajowych źródeł gazu, które trzeba szybko rozbudować. Następnie powstała unijna Platforma Biometanu. Komisarz UE ds. energii Dan Jørgensen powiedział, że jej celem jest wzmocnienie bezpieczeństwa dostaw.</p>
<p>W tym samym czasie doprecyzowano długoterminowe ramy emisyjne. 5 marca 2026 r. Rada UE formalnie przyjęła cel na 2040 r.: redukcję emisji netto gazów cieplarnianych o 90% w porównaniu z 1990 r. W tym samym pakiecie start ETS2, obejmującego paliwa dla budynków i transportu drogowego, przesunięto o rok, na 1 stycznia 2028 r.</p>

{exhibit(2, "Ceny i decyzje polityczne w 2026 r.",
         table(["Data", "Wydarzenie", "Znaczenie dla odbiorców gazu"], [
             ["1 stycznia", "CBAM wchodzi w fazę docelową", "Koszt emisji obejmuje import stali, cementu, aluminium, nawozów, wodoru i energii elektrycznej"],
             ["15 stycznia", "EUA na grudzień 2026 r. powyżej 92 EUR/t", "Najwyższa cena uprawnień od ponad dwóch lat"],
             ["5 marca", "Cel na 2040 r. przyjęty; ETS2 przesunięty na 2028 r.", "Długoterminowa ścieżka redukcji zapisana w prawie"],
             ["7 kwietnia", "Pierwsza cena certyfikatu CBAM: 75,36 EUR/t", "Koszt emisji na granicy staje się znaną liczbą"],
             ["22 kwietnia", "Publikacja AccelerateEU", "Biometan wskazany jako krajowe źródło dostaw"],
             ["22 października", "TTF blisko 89 EUR/MWh", "177% powyżej poziomu z lutego"],
         ]),
         src(("ICAP", "https://icapcarbonaction.com/en/news/eu-reaches-agreement-2040-climate-target-postpones-ets-2-one-year"),
             ("GMK Center", "https://gmk.center/en/news/european-carbon-prices-exceeded-e90-t-in-january/"),
             ("Homaio", "https://homaio.com/post/2030-eua-price-predictions-expert-analysis-of-3-scenarios"),
             ("Brussels Times", "https://www.brusselstimes.com/2091683/eu-unveils-accelerateeu-clean-energy-plan-amid-mounting-fossil-fuel-crisis")) + ".")}

<h2>Dlaczego cząsteczki gazu mają tu znaczenie</h2>
<p>Elektryfikacja przejmie większość pracy przy dekarbonizacji Europy, ale znaczna część popytu nadal wymaga paliw gazowych lub ciekłych: ciepło wysokotemperaturowe w przemyśle, chemia, ciężki transport drogowy, żegluga oraz sezonowe bilansowanie systemu elektroenergetycznego. W tych zastosowaniach realne opcje to importowany gaz ziemny, wodór, ciekłe biopaliwa i biometan.</p>
<p>Spośród nich tylko biometan jest jednocześnie produkowany lokalnie, chemicznie identyczny z gazem ziemnym, zgodny z istniejącą siecią i urządzeniami oraz już dziś dojrzały komercyjnie. Instalacja przetwarzająca obornik, resztki pożniwne lub odpady spożywcze zatłacza gaz do tej samej sieci co importowany LNG, a u odbiorcy końcowego nie trzeba wymieniać żadnych urządzeń.</p>

<h2>Konsekwencje</h2>
<p>Dla odbiorców przemysłowych gaz kopalny niesie dziś trzy ryzyka cenowe: cenę towaru, cenę uprawnień do emisji w UE oraz, dla firm eksportujących do UE i ich konkurentów, cenę emisji na granicy. Wieloletni kontrakt na biometan odpowiada na wszystkie trzy jednocześnie. Dlatego działy zakupów, które dotąd traktowały biometan jako zakup zrównoważony, zaczynają traktować go jako zabezpieczenie.</p>
<p>Dla inwestorów argument bezpieczeństwa poszerza poparcie polityczne. Politykę klimatyczną można odłożyć, czego przykładem jest ETS2; polityka bezpieczeństwa zwykle przetrwa zmianę rządu. Biometan ma dziś poparcie z obu stron.</p>
<p>Dla rządów oznacza to, że przy obecnym tempie budowy cel 35 mld m³ na 2030 r. jest poza zasięgiem, co analizujemy w częściach 2 i 3. Najsilniej inwestycje przyspiesza pewność przychodów, czyli kontrakty różnicowe, aukcje i obowiązki domieszkowe, a nie wyłącznie dotacje inwestycyjne.</p>

<h2>Perspektywy</h2>
<p>Jeśli żegluga wróci do normy, ceny gazu mogą spaść, a ceny EUA się zmienią. Uważamy jednak, że zmiana zachowań odbiorców nie odwróci się wraz z cenami. Szok z 2026 r. pokazał odbiorcom przemysłowym i publicznym, ile kosztuje importowany gaz w czasie kryzysu, a harmonogram regulacji do 2030 r. dokłada do tego koszt emisji. Kapitał, który dziś buduje krajowe dostawy gazu odnawialnego, trafia na moment, w którym popyt wspierają jednocześnie prawo klimatyczne i polityka bezpieczeństwa.</p>
""",
)

# ---------------------------------------------------------------- 2
P2_PLANTS = bars([("2018", 483), ("2020", 729), ("2021", 1023), ("2022–23", 1322),
                  ("2024", 1548), ("2025", 1678), ("2026", 1975)],
                 "Liczba działających biometanowni w Europie według edycji mapy, 2018–2026", highlight=-1)
P2_GAP = stack([("Zbudowane do połowy 2026 r.", 8.2, "accent"),
                ("Zakontraktowane projekty", 9, "mid"),
                ("Bez konkretnych projektów", 17.8, "gap")], 35,
               "Moce biometanu wobec celu 35 mld m³ na 2030 r., mld m³ rocznie", unit=" mld m³", target_label="Cel")

P2 = dict(
    title="Biometan na poziomie 8 mld m³: ile Europa osiągnęła i ile jej brakuje",
    short="Biometan: 8 mld m³",
    standfirst="Zainstalowana moc wzrosła w ciągu roku o 17%, a zobowiązania inwestycyjne sięgnęły 36 mld euro. Nawet jeśli powstaną wszystkie ogłoszone projekty, Europa osiągnie mniej więcej połowę celu na 2030 r.",
    keypoints=[
        "Na koniec II kwartału 2026 r. w Europie działało 1975 biometanowni o mocy 8,2 mld m³ rocznie; w ostatnich dwunastu miesiącach uruchomiono 327 instalacji.",
        "Ogłoszone inwestycje o wartości 36 mld euro dodadzą do 2030 r. około 9 mld m³ mocy. Na mniej więcej 18 mld m³ z celu 35 mld m³ nie ma jeszcze konkretnych projektów.",
        "Pięć krajów odpowiada za 95% produkcji. Kolejny wzrost przyjdzie z nowych rynków i platform wieloinstalacyjnych.",
    ],
    seo="Europejskie moce biometanu osiągnęły w 2026 r. 8,2 mld m³ w 1975 instalacjach. Luka wobec celu 35 mld m³ na 2030 r. i to, skąd przyjdzie wzrost.",
    keywords="rynek biometanu w Europie, moce biometanu w Europie 2026, REPowerEU 35 mld m³, inwestycje w biometan",
    body=f"""
<p>1 lipca Europejskie Stowarzyszenie Biogazu (EBA) i Gas Infrastructure Europe (GIE) opublikowały edycję 2026 Europejskiej Mapy Biometanu. Na koniec II kwartału zainstalowana moc wynosiła 8,2 mld m³ rocznie, o ponad 1 mld m³ i 17% więcej niż rok wcześniej. Liczba działających instalacji wzrosła z 1678 do 1975, w tym 327 nowo uruchomionych. To mniej więcej czterokrotnie więcej niż w 2018 r.</p>

{exhibit(1, "Działające biometanownie w Europie według edycji mapy", P2_PLANTS,
         src(("EBA / GIE, Europejska Mapa Biometanu 2026", "https://advancedbiofuelsusa.info/europe-adds-1-bcm-of-biomethane-production-but-acceleration-of-its-own-source-of-renewable-gas-can-go-much-faster"),
             ("GIE, wcześniejsze edycje", "https://www.gie.eu/?p=3977")) + ".",
         "Każda edycja liczy instalacje działające w dniu zamknięcia danych. Edycja 2026 obejmuje dane do końca II kwartału 2026 r.")}

<h2>Większe i bardziej przemysłowe instalacje</h2>
<p>Przeciętna europejska biometanownia produkuje dziś około 472 Nm³ na godzinę, kilkukrotnie więcej niż rolnicze agregaty biogazowe, które dominowały na rynku przez ostatnią dekadę. To efekt przejścia od produkcji energii elektrycznej na miejscu do uszlachetniania gazu i zatłaczania go do sieci gazowej.</p>
<p>Cały sektor biogazu jest znacznie większy niż flota biometanowni. Według raportu statystycznego EBA łączna produkcja biogazu i biometanu w Europie wyniosła w 2024 r. 22 mld m³, z czego 19 mld m³ w UE. Większość biogazu wciąż spala się w silnikach produkujących prąd i ciepło. Każdą z tych lokalizacji można przekształcić w projekt zatłaczania do sieci, a modernizacja jest często tańsza i szybsza niż nowa budowa.</p>
<p>Zmieniła się też struktura rynku. Francja, dzięki taryfie gwarantowanej, która zapewnia finansowanie mniejszym instalacjom zatłaczającym gaz do sieci, wyprzedziła Niemcy i jest dziś największym producentem biometanu w Europie.</p>

<h2>Rachunek na 2030 rok</h2>
<p>Raport EBA Investment Outlook 2026 wylicza zakontraktowane inwestycje na 36 mld euro, wobec 28 mld euro rok wcześniej. Jeśli zostaną w pełni zrealizowane, dodadzą do 2030 r. około 9 mld m³ rocznej mocy. Razem z obecnymi instalacjami Europa osiągnie około 17 mld m³, mniej więcej połowę celu REPowerEU wynoszącego 35 mld m³.</p>

{exhibit(2, "Moce wobec celu na 2030 r. (mld m³ rocznie)", P2_GAP,
         src(("EBA, Biomethane Investment Outlook 2026", "https://uabio.org/en/news/19820/"),
             ("EBA / GIE", "https://advancedbiofuelsusa.info/europe-adds-1-bcm-of-biomethane-production-but-acceleration-of-its-own-source-of-renewable-gas-can-go-much-faster")) + "; obliczenia Qiao Partners.",
         "Zainstalowana moc obejmuje całą Europę, w tym kraje spoza UE; cel 35 mld m³ dotyczy tylko UE. Porównanie ma charakter orientacyjny.")}

<p>Surowce nie wydają się ograniczeniem. Badanie Guidehouse dla EBA z 2026 r. szacuje zrównoważony potencjał UE na 31–32 mld m³ w 2030 r. i do 184 mld m³ w 2050 r. Hamulcem są czas wydawania pozwoleń, przyłączenia do sieci, pewność przychodów oraz moce wykonawcze deweloperów i wykonawców. EBA zwraca też uwagę, że pięć krajów odpowiada za 95% europejskiej produkcji, a większość państw członkowskich dopiero zaczyna.</p>

<h2>Skąd przyjdzie wzrost</h2>
{exhibit(3, "Europejskie rynki biometanu według etapu rozwoju",
         table(["Etap", "Przykładowe kraje", "Sytuacja", "Typowa szansa"], [
             ["Dojrzałe", "Francja, Niemcy, Dania, Włochy, Holandia", "Utrwalone systemy taryf lub obowiązków; silna konkurencja o surowiec", "Konsolidacja, wymiana urządzeń, przekształcanie biogazowni z silnikami w instalacje zatłaczające do sieci"],
             ["Rozwijające się", "Hiszpania, Belgia, Wielka Brytania, Austria, Szwecja", "Ramy prawne gotowe, rosnący portfel projektów", "Nowe platformy oparte na umowach odbioru"],
             ["Wschodzące", "Polska, Czechy, Rumunia, Węgry, Grecja, kraje bałtyckie", "Systemy wsparcia uchwalone w latach 2025–26", "Wczesne zabezpieczenie gruntów, przyłączy i surowca"],
         ]),
         "Qiao Partners na podstawie danych krajowych EBA i ustawodawstwa krajowego.")}

<p>Pierwszą falę europejskiego biometanu tworzyli rolnicy wspierani dotacjami krajowymi. Spodziewamy się, że następna będzie wyglądać inaczej: fundusze infrastrukturalne i przedsiębiorstwa użyteczności publicznej będą posiadać portfele od 10 do 50 instalacji o standardowym projekcie, zarządzane z centralnej sterowni i sprzedające do kilku rynków jednocześnie. Przykładem tego modelu jest hiszpański Asterion Industrial Partners, który przeznacza 1,5 mld euro na platformę paneuropejską i do końca 2026 r. chce mieć 20 działających instalacji.</p>

<h2>Perspektywy</h2>
<p>Przy obecnym tempie Europa może dodawać 1–1,5 mld m³ mocy rocznie; do osiągnięcia 35 mld m³ w 2030 r. potrzeba około 6 mld m³ rocznie. Cel prawdopodobnie nie zostanie osiągnięty, ale wielkość luki ma znaczenie dla inwestorów: oznacza, że do końca dekady popyt na nowe moce i wytwarzane przez nie certyfikaty będzie wyższy od podaży. Najciekawsze punkty wejścia widzimy na rynkach wschodzących, gdzie przepisy są nowe, a konkurencja o lokalizacje i surowiec wciąż ograniczona.</p>
""",
)

# ---------------------------------------------------------------- 3
P3_RATE = bars([("Uruchomione w ostatnich 12 mies.", 327),
                ("Potrzebne rocznie: zakontraktowane projekty", 480),
                ("Potrzebne rocznie: cel 35 mld m³", 1430)],
               "Biometanownie uruchamiane rocznie wobec tempa potrzebnego do 2030 r.", highlight=2)

P3 = dict(
    title="6500 instalacji do zbudowania: gdzie trafią europejskie wydatki na urządzenia do biometanu",
    short="Fala budowy urządzeń",
    standfirst="Osiągnięcie celu na 2030 r. wymaga ponad czterokrotnie szybszej budowy niż obecnie. Wąskim gardłem nie są już surowce i finansowanie, lecz moce produkcyjne i wykonawcze.",
    keypoints=[
        "Według naszych szacunków wypełnienie luki do celu 35 mld m³ wymaga około 6500 nowych instalacji o obecnej średniej wielkości, a w ostatnim roku uruchomiono 327.",
        "Prognozy rynkowe wyceniają globalny rynek uszlachetniania biogazu w 2026 r. na 1,6–2,2 mld USD, z roczną dynamiką około 10–11%; Europa odpowiada za 45–66% popytu.",
        "Uszlachetnianie, fermentacja z infrastrukturą towarzyszącą, odzysk CO₂ i bio-LNG to cztery odrębne rynki urządzeń, do których dochodzą przychody z serwisu.",
    ],
    seo="Europa potrzebuje około 6500 kolejnych biometanowni, by osiągnąć 35 mld m³ w 2030 r. Wielkość rynków urządzeń do uszlachetniania, fermentacji, CO₂ i bio-LNG.",
    keywords="rynek urządzeń do biometanu, rynek uszlachetniania biogazu w Europie, uszlachetnianie membranowe, urządzenia bio-LNG, biogeniczne CO₂",
    body=f"""
<p>1975 europejskich biometanowni produkuje rocznie około 8,2 mld m³, średnio około 4,2 mln m³ na instalację. Przy tej średniej wielkości wypełnienie luki do celu 35 mld m³ wymaga około 6500 nowych instalacji. Samo zbudowanie projektów zakontraktowanych w portfelu EBA o wartości 36 mld euro wymaga około 2200. W ciągu czterech i pół roku do końca 2030 r. oznacza to odpowiednio około 1430 i 480 instalacji rocznie. W ostatnich dwunastu miesiącach Europa uruchomiła 327.</p>

{exhibit(1, "Instalacje uruchamiane rocznie: obecnie i tyle, ile potrzeba do 2030 r.", P3_RATE,
         "EBA / GIE, Europejska Mapa Biometanu 2026; EBA, Biomethane Investment Outlook 2026; obliczenia Qiao Partners.",
         "Przy średniej produkcji około 4,2 mln m³ na instalację w 2026 r. i terminie na koniec 2030 r. Większe instalacje zmniejszają ich liczbę, ale nie łączną wartość urządzeń.")}

<p>Większe instalacje zmniejszą potrzebną liczbę, a część mocy przyjdzie z przekształcania istniejących biogazowni, ale nie zmienia to wniosku: przez resztę dekady europejscy deweloperzy, firmy inżynieryjne i dostawcy urządzeń muszą dostarczać kilka razy więcej niż obecnie.</p>

<h2>Jak duży jest rynek urządzeń</h2>
<p>Prognozy komercyjne obejmują różne zakresy, ale zgadzają się co do kierunku wzrostu i udziału Europy w popycie.</p>

{exhibit(2, "Opublikowane prognozy rynku urządzeń do uszlachetniania biogazu",
         table(["Źródło (data)", "Zakres", "Prognoza", "Dynamika", "Udział Europy"], [
             [link("Global Market Insights", "https://www.gminsights.com/industry-analysis/biogas-upgrading-technology-market") + " (czerwiec 2026)", "Technologie uszlachetniania, świat", "2,2 mld USD (2026) do 5,9 mld USD (2035)", "11,2% rocznie", "Największy region"],
             [link("Persistence Market Research", "https://www.persistencemarketresearch.com/market-research/biogas-upgrading-market.asp") + " (sierpień 2026)", "Uszlachetnianie, świat", "1,6 mld USD (2026) do 3,2 mld USD (2033)", "10,1% rocznie", "44,7%"],
             [link("gasworld", "https://www.gasworld.com/story/biogas-upgrading-market-to-top-4bn-by-2030/2254502.article/"), "Uszlachetnianie, świat", "Ponad 4 mld USD (2030)", "–", "61,9%"],
             [link("QYResearch", "https://marketpublishers.com/report/equipment/global-biogas-upgrading-equipment-market-2018-by-manufacturers-forecast-to-2023.html") + " (2026)", "Urządzenia do uszlachetniania, świat", "–", "–", "ok. 66%"],
             [link("BCC Research", "https://www.bccresearch.com/market-research/energy-and-resources/biogas-upgrading.html?ro=yes"), "Membrany do separacji gazów, wszystkie zastosowania", "1,5 mld USD (2025) do 2,5 mld USD (2031)", "9,1% rocznie", "–"],
         ], cls="tbl-dense"),
         "Według linków. Zakresy się różnią, więc dane nie są bezpośrednio porównywalne.")}

<p>Uszlachetnianie to tylko część nakładów inwestycyjnych instalacji. Komory fermentacyjne, obsługa surowca, magazynowanie gazu, sprężanie, przyłącze do sieci, skraplanie i odzysk CO₂ łącznie stanowią większą część. Cały europejski rynek urządzeń do biometanu jest więc kilkukrotnie większy niż powyższe dane dotyczące uszlachetniania.</p>

<h2>Cztery rynki urządzeń</h2>
<p><strong>Uszlachetnianie.</strong> Według EBA około połowa europejskich instalacji przyłączonych do sieci oddziela metan od CO₂ za pomocą membran; pozostałe stosują adsorpcję zmiennociśnieniową, płuczki wodne lub aminowe oraz technologie kriogeniczne. Membrany zyskują udział dzięki modułowości i niskim kosztom eksploatacji, a dostawcy oferują dziś kontenerowe zestawy o wydajności od około 80 do 12 000 Nm³/h. Marże koncentrują się w modułach membranowych, sprężarkach i systemach sterowania.</p>
<p><strong>Fermentacja i infrastruktura towarzysząca.</strong> Zbiorniki, mieszadła, dwumembranowe magazyny gazu, pompy, wymienniki ciepła, odsiarczanie i wstępne przygotowanie surowca. To wielkoseryjne wyroby stalowe i polimerowe, które można standaryzować; w przetargach liczą się cena i termin dostawy.</p>
<p><strong>Odzysk CO₂.</strong> Uszlachetnianie daje niemal czysty strumień biogenicznego CO₂, który większość instalacji wciąż wypuszcza do atmosfery. Po skropleniu można go sprzedać odbiorcom z branży spożywczej, napojowej i szklarniowej albo trwale składować. Szwajcarski projekt podpisał z INEOS umowę na składowanie od 2026 r. biogenicznego CO₂ z produkcji biometanu pod duńskim dnem Morza Północnego.</p>
<p><strong>Bio-LNG i bio-CNG.</strong> Wiele źródeł surowca leży daleko od sieci gazowej. Małe instalacje skraplania, zbiorniki kriogeniczne, kontenery ISO i stacje tankowania pozwalają tym instalacjom sprzedawać do transportu drogowego i żeglugi, gdzie rynki zgodności płacą premię.</p>
<p>Każda instalacja to także około 20 lat przychodów z serwisu: zdalny monitoring, optymalizacja procesu biologicznego, wymiana membran i umowy serwisowe.</p>

<h2>Kto buduje</h2>
<p>Europejscy integratorzy rosną, ale pod presją. Niemiecki EnviTec Biogas ogłosił w lipcu 2026 r. inwestycję 100 mln euro w rozwój biometanu, jednocześnie obniżając prognozę zysku przed opodatkowaniem na 2026 r. do 5–15 mln euro z powodu niekorzystnych zmian regulacyjnych. Weltec Biopower zbudował ponad 450 instalacji w 27 krajach. Na rynek weszli też dostawcy z Azji: chińscy producenci dostarczyli membranowe instalacje do uszlachetniania i dwumembranowe magazyny gazu do projektów w Polsce, Hiszpanii, Włoszech i Wielkiej Brytanii.</p>

{exhibit(3, "Czym kierują się kupujący przy wyborze urządzeń",
         table(["Priorytet kupującego", "Co musi wykazać dostawca"], [
             ["Szybkie uruchomienie", "Urządzenia zaprojektowane z wyprzedzeniem, kontenerowe, testowane fabrycznie"],
             ["Bankowalność", "Referencje w Europie, gwarancje parametrów, gwarancja zabezpieczona ubezpieczeniem"],
             ["Emisja metanu", "Certyfikowana niska emisja; bezpośrednio wpływa na redukcję emisji według RED III i wartość certyfikatów"],
             ["Serwis lokalny", "Części zamienne i technicy w Europie, reakcja w ciągu 24–48 godzin"],
             ["Całkowity koszt posiadania", "Zużycie energii na Nm³, żywotność membran, dostępność powyżej 95%"],
         ]),
         "Qiao Partners.")}

<h2>Perspektywy</h2>
<p>Spodziewamy się, że rynek urządzeń przejdzie od inżynierii projektowej do produkcji przemysłowej: standardowe projekty, powtarzalne moduły, ceny ilościowe i długoterminowe umowy serwisowe. Dostawcy, którzy zaoferują standardowe linie 250–1000 Nm³/h montowane i serwisowane w Europie, mogą zdobyć ponadproporcjonalny udział w następnej fali budowy. Ponieważ moce produkcyjne Europy są ograniczone, współpraca z dostawcami z Azji staje się dla deweloperów kwestią praktyczną, a nie polityczną. Struktury takiej współpracy omawiamy w następnej części serii.</p>
""",
)

# ---------------------------------------------------------------- 4
P4 = dict(
    title="Chiny a rozbudowa europejskiego biometanu: struktury, które działają",
    short="Chiny a rozbudowa rynku",
    standfirst="Europie brakuje mocy produkcyjnych do budowy biometanowni. Chińscy dostawcy je mają, ale mierzą się z ostrzejszą polityką przemysłową UE. Struktura wejścia na rynek jest dziś równie ważna jak cena.",
    keypoints=[
        "Chińscy producenci już dostarczają instalacje do uszlachetniania i magazyny gazu do europejskich projektów; zapotrzebowanie na moce produkcyjne będzie rosło do 2030 r.",
        "Akt w sprawie przemysłu neutralnego emisyjnie (NZIA) od 2026 r. wprowadza kryteria odporności w przetargach publicznych i aukcjach. Proponowany Akt o przyspieszeniu przemysłowym (IAA) uzależni duże inwestycje zagraniczne od spółek joint venture i transferu technologii.",
        "Spółki joint venture z europejską większością, licencje technologiczne i mniejszościowe udziały w europejskich platformach to modele wejścia, które najpewniej przetrwają tę zmianę polityki.",
    ],
    seo="Jak chińscy producenci i inwestorzy mogą uczestniczyć w rozbudowie europejskiego biometanu w świetle NZIA, IAA i przepisów o inwestycjach zagranicznych.",
    keywords="chińskie inwestycje w biometan w Europie, kryteria odporności NZIA, Industrial Accelerator Act inwestycje zagraniczne, czyste technologie Chiny–Europa, chińskie urządzenia do biogazu",
    body=f"""
<p>W poprzedniej części serii oszacowaliśmy, że Europa musi uruchamiać rocznie kilka razy więcej biometanowni niż obecnie, by zbliżyć się do celu na 2030 r. Europejscy integratorzy sami nie są w stanie w takim tempie produkować, dostarczać i uruchamiać instalacji. Chińscy producenci mogą dostarczać membrany, zbiorniki stalowe, sprężarki i urządzenia kriogeniczne w dużych ilościach i po niskich kosztach. Przeszkoda polega na tym, że 2026 r. przyniósł też najbardziej asertywną politykę przemysłową UE od pokolenia.</p>

<h2>Skąd bierze się szansa</h2>
<p>Udziałowi chińskich firm sprzyjają trzy czynniki. Pierwszy to opisana wyżej luka w mocach. Drugi to koszty: rosnące ceny energii i pracy w Europie podniosły ceny wytwarzania u dostawców z UE właśnie wtedy, gdy deweloperzy najbardziej potrzebują tańszych dóbr inwestycyjnych. Trzeci to doświadczenie: Chiny prowadzą jeden z największych programów biogazowych na świecie, z planami obejmującymi tysiące dużych instalacji, a chińscy dostawcy eksportują już dwumembranowe magazyny gazu i membranowe instalacje do uszlachetniania do projektów w Europie.</p>
<p>Współpraca od dawna działa w obu kierunkach. EnviTec Biogas zbudował kilka instalacji w Chinach, a Air Liquide prowadzi tam działalność w zakresie biometanu. Europejskie firmy znają chińskich partnerów, a chińskie firmy mają doświadczenie projektowe z europejską technologią.</p>

<h2>Przepisy, z którymi mierzą się chińskie firmy</h2>
{exhibit(1, "Przepisy UE istotne dla udziału chińskich firm w biometanie (stan na 1 listopada 2026 r.)",
         table(["Przepis", "Co przewiduje", "Status", "Znaczenie dla biometanu"], [
             ["Akt w sprawie przemysłu neutralnego emisyjnie (NZIA)", "Pozacenowe kryteria odporności i zrównoważenia w zamówieniach publicznych i aukcjach OZE", "Od 30 grudnia 2025 r. stosowane do co najmniej 30% wolumenu aukcji lub 6 GW rocznie; wytyczne przetargowe opublikowano w lipcu 2026 r.", "Urządzenia od dominującego dostawcy spoza UE mogą otrzymać niższą ocenę w przetargach z dotacją; montaż w UE poprawia ocenę"],
             ["Akt o przyspieszeniu przemysłowym (projekt)", "Inwestycje powyżej 100 mln euro w sektorach, w których jedno państwo trzecie ma ponad 40% światowych mocy, muszą spełnić cztery z sześciu warunków, m.in. joint venture z udziałem zagranicznym do 49% i licencjonowanie IP", "Zaproponowany 4 marca 2026 r.; w procesie legislacyjnym, przyjęcie spodziewane w 2027 r.", "Dotyczy głównie baterii i pojazdów elektrycznych; pokazuje, jak Bruksela podchodzi do dużych inwestycji z Chin"],
             ["Rozporządzenie w sprawie subsydiów zagranicznych", "Komisja bada subsydia państw trzecich w dużych przetargach i przejęciach", "Obowiązuje", "Dotyczy przejęć dużych platform i zamówień publicznych"],
             ["Krajowa kontrola inwestycji zagranicznych", "Kontrola inwestycji w energetykę i infrastrukturę krytyczną przez państwa członkowskie", "Obowiązuje w większości państw", "Instalacje przyłączone do sieci mogą podlegać kontroli; udziały mniejszościowe i joint venture łatwiej uzyskują zgodę"],
             ["Przepisy produktowe i dotyczące zrównoważenia", "Oznakowanie CE, przepisy o urządzeniach ciśnieniowych i ATEX; rozliczanie emisji według RED III; systemy certyfikacji, np. ISCC", "Obowiązują", "Kredytodawcy i jednostki certyfikujące sprawdzają parametry urządzeń, nie tylko cenę"],
         ], cls="tbl-dense"),
         src(("Herbert Smith Freehills Kramer", "https://www.hsfkramer.com/zh/notes/energy/2025-posts/the-net-zero-industry-act-new-implementing-rules-to-accelerate-clean-technology-manufacturing-in-the-eu"),
             ("Carbon Pulse", "https://carbon-pulse.com/534444/"),
             ("Jones Day", "https://trendingnowinesg.jonesday.com/post/102mm0d/eu-industrial-accelerator-act-what-companies-need-to-know"),
             ("Squire Patton Boggs", "https://www.squirepattonboggs.com/media/v10hvn1w/industrial-accelerator-act-a-general-overview.pdf"),
             ("JD Supra", "https://www.jdsupra.com/legalnews/european-commission-proposes-industrial-7246033/")) + ".")}

<p>Chińskie Ministerstwo Handlu ostrzegło w kwietniu, że podejmie środki zaradcze, jeśli IAA zaszkodzi interesom chińskich firm. Dla firm wchodzących do Europy oznacza to, że trwałość ich pozycji zależy nie tylko od zgodności z obecnymi przepisami, ale także od struktury wejścia.</p>

<h2>Pięć sposobów wejścia</h2>
{exhibit(2, "Modele wejścia dla chińskich producentów i inwestorów",
         table(["Model", "Jak działa", "Potrzebny kapitał", "Ryzyko zmian polityki", "Dla kogo"], [
             ["Joint venture na montaż i serwis w UE", "Strona chińska dostarcza kluczowe komponenty; spółka z europejską większością montuje, certyfikuje i serwisuje", "Średni", "Niskie", "Producenci, którzy chcą długoterminowego udziału w rynku"],
             ["Licencja technologiczna", "Licencjonowanie IP z zakresu membran, sprężania lub kriogeniki europejskim producentom za opłaty licencyjne", "Niski", "Niskie", "Właściciele technologii, którzy nie planują fabryk w Europie"],
             ["Mniejszościowy udział w europejskiej platformie", "Inwestor obejmuje mniej niż 50% udziałów w deweloperze wielu instalacji, zwykle z prawem do dostaw urządzeń", "Średni do wysokiego", "Niskie do średniego", "Fundusze, grupy przemysłowe, family offices"],
             ["Finansowanie przez dostawcę", "Dostawa urządzeń z odroczoną płatnością w zamian za udziały w projekcie lub długoterminową umowę serwisową", "Średni", "Średnie", "Producenci z silnym bilansem; deweloperzy z niedoborem kapitału"],
             ["Bezpośredni eksport", "Sprzedaż kompletnych systemów przez europejskich dystrybutorów", "Niski", "Wysokie", "Komponenty, części zamienne, projekty bez dotacji"],
         ], cls="tbl-dense"),
         "Qiao Partners.")}

<h2>Na co patrzą europejscy kupujący i kredytodawcy</h2>
<p>Z naszego doświadczenia większość procesów zakupowych rozstrzyga się na tych samych pięciu pytaniach. Czy gwarancję da się wyegzekwować przez 20 lat życia instalacji za pośrednictwem podmiotu zarejestrowanego w UE i ubezpieczenia? Czy parametry są certyfikowane, zwłaszcza emisja metanu i zużycie energii na Nm³, które bezpośrednio wpływają na redukcję emisji według RED III i wartość certyfikatów? Czy są referencje z działających instalacji w Europie? Czy części zamienne i technicy mogą dotrzeć na miejsce w ciągu 24–48 godzin? Czy dokumentacja jest kompletna, od dokumentacji technicznej CE po cyberbezpieczeństwo podłączonych systemów sterowania i przejrzystość źródeł finansowania dostawcy?</p>
<p>Dla kredytodawców dwie lub trzy instalacje działające w Europie ważą więcej niż długa lista referencji z Azji.</p>

<h2>Perspektywy</h2>
<p>Spodziewamy się, że chińskie firmy, które odniosą sukces na europejskim rynku biometanu, połączą koszty i skalę chińskiej produkcji z montażem w Europie, spółką operacyjną z europejską większością i gwarancjami akceptowanymi przez banki. Czysty eksport pozostanie możliwy dla komponentów i mniejszych projektów, ale ten model jest najbardziej narażony na kryteria oceny w przetargach i przyszłe środki handlowe. Firmy, które zbudują bazę zainstalowanych urządzeń w latach 2026–2028, będą też mieć umowy serwisowe tych instalacji w szczycie europejskiej budowy około 2030 r.</p>
""",
)

# ---------------------------------------------------------------- 5
P5 = dict(
    title="Struktura przychodów biometanowni: jak przepisy UE wyznaczają zarobki instalacji",
    short="Struktura przychodów",
    standfirst="Biometanownia sprzedaje gaz oraz zestaw atrybutów tworzonych przez prawo. Większość wartości zależy od tego, który odbiorca otrzyma który atrybut, i od tego, by nigdy nie rozliczyć tej samej korzyści dwa razy.",
    keypoints=[
        "Jedna megawatogodzina biometanu może przynosić przychód z samego gazu, wsparcia krajowego, certyfikatów, obowiązków transportowych, zgodności w żegludze i rynku uprawnień, a do tego z CO₂ i pofermentu.",
        "ETS2 od 1 stycznia 2028 r. stworzy nową grupę odbiorców objętych obowiązkami. Certyfikowany biometan liczy się w ETS2 jako zeroemisyjny.",
        "Ceny wyznacza intensywność emisji. Instalacje o niskiej emisji metanu, przetwarzające obornik i odzyskujące CO₂, uzyskują najwyższe premie na rynkach obowiązków transportowych i w żegludze.",
    ],
    seo="Jak EU ETS, ETS2, RED III, FuelEU Maritime, CBAM i gwarancje pochodzenia razem wyznaczają przychody europejskiej biometanowni.",
    keywords="model przychodów biometanowni, biometan ETS2, FuelEU Maritime bio-LNG, unijna baza danych, gwarancje pochodzenia, RED III",
    body=f"""
<p>Przychód europejskiej biometanowni to cena fizycznego gazu plus nawet pięć atrybutów tworzonych przez przepisy oraz przychody z produktów ubocznych. W 2026 r. całą strukturę podniosły dwie zmiany: gaz kopalny przewartościował się do niemal 89 EUR/MWh, a instrumenty emisyjne, które biometan pozwala ograniczyć, od EU ETS i jego rozszerzenia na żeglugę po CBAM i nadchodzący ETS2, są bliżej pełnego działania.</p>

{exhibit(1, "Warstwy przychodów dostępne dla producenta biometanu w Europie",
         table(["Warstwa", "Instrument", "Kto płaci", "Czynnik 2026–28"], [
             ["Towar", "Fizyczny gaz sprzedawany na hubie (TTF, THE, PEG)", "Spółki obrotu, przedsiębiorstwa użyteczności publicznej, przemysł", "TTF blisko 89 EUR/MWh 22 października 2026 r."],
             ["Wsparcie krajowe", "Taryfy gwarantowane, kontrakty różnicowe, aukcje, dotacje inwestycyjne", "Rządy", "Nowe systemy w Polsce, Grecji i innych krajach; AccelerateEU"],
             ["Certyfikaty", "Gwarancje pochodzenia; dowody zrównoważenia według RED III, śledzone w unijnej bazie danych", "Odbiorcy korporacyjni, przedsiębiorstwa użyteczności publicznej", "Raportowanie emisji zakresu 1; wdrażanie RED III do prawa krajowego"],
             ["Obowiązki transportowe", "Krajowe obowiązki redukcji emisji dla dostawców paliw, np. niemiecka kwota THG", "Dostawcy paliw", "Premie za gaz o niskiej intensywności emisji i z obornika"],
             ["Żegluga", "Limity intensywności emisji FuelEU Maritime (2% poniżej 2020 r. od 2025 r., 6% od 2030 r.) oraz EU ETS w żegludze", "Armatorzy, pule zgodności", "Popyt flot napędzanych LNG na bio-LNG"],
             ["Rynek uprawnień", "EU ETS (zerowy współczynnik emisji dla zrównoważonego biometanu); ETS2 od 2028 r.", "Instalacje objęte systemem, dostawcy paliw", "Certyfikowany biometan liczy się w ETS2 jako zeroemisyjny"],
             ["Produkty uboczne", "Biogeniczne CO₂, nawóz z pofermentu", "Branża spożywcza i napojowa, szklarnie, składowanie CO₂, gospodarstwa rolne", "Pierwsze umowy na składowanie; ceny nawozów"],
         ], cls="tbl-dense"),
         src(("3Degrees", "https://3degreesinc.com/insights/eu-ets2-what-it-means-and-why-biomethane-matters"),
             ("ANSA za SoldiOnline", "https://www.soldionline.it/notizie/forex-commodities/gas-ue-177-da-febbraio-cosa-ce-dietro-il-balzo-del-ttf-a-89-mwh")) + "; Qiao Partners.",
         "Nie każda instalacja uzyskuje każdą warstwę. Kwalifikowalność zależy od surowca, certyfikacji i państwa członkowskiego.")}

<h2>Najszybciej zmieniają się warstwy emisyjne</h2>
<p><strong>EU ETS.</strong> Analitycy oczekują zacieśnienia podaży uprawnień w 2026 i 2027 r. Montel w grudniu 2025 r. prognozował średnią cenę w 2026 r. blisko 92 EUR/t; później wysokie ceny gazu sprowadziły rynek wiosną do poziomu około 75 euro. Państwa członkowskie ustalają szczegółowe zasady stosowania biometanu przez instalacje objęte ETS; Włochy zatwierdziły wytyczne w 2026 r.</p>
<p><strong>ETS2.</strong> Od 1 stycznia 2028 r. dostawcy paliw dla budynków i transportu drogowego muszą posiadać uprawnienia za emisje ze sprzedanych paliw, a pierwsze umorzenie przypada w maju 2029 r. Każda megawatogodzina certyfikowanego biometanu w sieci dystrybucyjnej zmniejsza ten obowiązek, co tworzy dużą nową grupę odbiorców.</p>
<p><strong>CBAM.</strong> Po ustaleniu pierwszej ceny certyfikatu na 75,36 EUR/t CO₂ unijni producenci stali, cementu, nawozów, aluminium i wodoru, którzy ograniczają emisje z ciepła procesowego, zyskują przewagę kosztową nad wysokoemisyjnym importem i krajowymi konkurentami, którzy emisji nie ograniczyli.</p>

<h2>Trzy zasady łączenia przychodów</h2>
<p><strong>Każdą korzyść rozlicza się tylko raz.</strong> Ta sama megawatogodzina nie może jednocześnie zaliczyć się do obowiązku transportowego, puli zgodności w żegludze i redukcji emisji zakresu 1 firmy. Służą temu zasady bilansu masy według RED III i unijna baza danych, a odbiorcy coraz częściej to weryfikują.</p>
<p><strong>Ceny wyznacza intensywność emisji.</strong> Surowiec i parametry instalacji decydują o wyniku emisyjnym. Najlepsze wyniki i najwyższe premie uzyskują instalacje przetwarzające obornik, z niską emisją metanu i odzyskiem CO₂. Słaba kontrola emisji metanu obniża wartość każdej warstwy.</p>
<p><strong>Gaz i atrybuty wycenia się osobno.</strong> Długoterminowe umowy odbioru coraz częściej łączą cenę gazu powiązaną z hubem ze stałą lub minimalną ceną atrybutów. Producent otrzymuje przychód akceptowany przez banki, a odbiorca spełnia obowiązki po znanym koszcie.</p>

<h2>Perspektywy</h2>
<p>Spodziewamy się, że kolejna przewaga konkurencyjna w europejskim biometanie będzie handlowa, nie technologiczna. Producenci i odbiorcy, którzy potrafią certyfikować, śledzić i kierować każdy atrybut na rynek płacący najwięcej, ponad granicami i przez start ETS2 w 2028 r., osiągną marże niedostępne dla instalacji sprzedających jeden pakiet. Dla inwestorów oznacza to, że struktura certyfikacji i odbioru projektu zasługuje na równie staranne due diligence jak jego inżynieria.</p>
""",
)

# ---------------------------------------------------------------- 6
P6 = dict(
    title="Polska: kolejny europejski rynek biometanu",
    short="Polska",
    standfirst="Do 2025 r. Polska była największą luką na europejskiej mapie biometanu. W 2026 r. zyskała system aukcyjny, program dotacji i prostsze zasady przyłączania do sieci. Okno na wczesne pozycje to lata 2026–2028.",
    keypoints=[
        "Polska oferuje już taryfę z premią gwarantowaną dla instalacji do 1 MW, we wrześniu parlament uchwalił system aukcyjny dla większych instalacji, a 800 mln zł przeznaczono na dotacje inwestycyjne.",
        "Polska Organizacja Biometanu naliczyła na koniec III kwartału 2025 r. 122 projekty w przygotowaniu; na koniec I kwartału 2026 r. zarejestrowanych było 208 biogazowni rolniczych.",
        "Duży sektor rolno-spożywczy, przemysł zależny od gazu oraz dostęp do niemieckiego rynku i rynku zgodności w żegludze sprawiają, że polski biometan ma wartość także poza Polską.",
    ],
    seo="Nowy system aukcyjny dla biometanu w Polsce, dotacje 800 mln zł i 122 projekty w przygotowaniu. Dlaczego lata 2026–2028 to okno na wczesne pozycje.",
    keywords="biometan w Polsce, biometan Polska, aukcje biometanu Polska, dotacje NFOŚiGW na biometan, gaz odnawialny w Europie Środkowo-Wschodniej",
    body=f"""
<p>Polska ma jedną z największych baz surowców rolniczych w Europie i przemysł silnie zależny od gazu, a do 2025 r. niemal nie produkowała biometanu. Kancelaria Rödl &amp; Partner nazwała ją największą luką na europejskiej mapie biometanu. Ta sytuacja szybko się zmienia. Do jesieni 2026 r. Polska wprowadziła system wsparcia dla małych instalacji, system aukcyjny dla dużych, program dotacji oraz nowe zasady przyłączania do sieci.</p>

<h2>Ramy prawne</h2>
{exhibit(1, "Wsparcie biometanu w Polsce (stan na 1 listopada 2026 r.)",
         table(["Instrument", "Na czym polega", "Status"], [
             ["Premia gwarantowana dla instalacji do 1 MW", "Producent sprzedaje po cenie rynkowej i otrzymuje różnicę do ceny gwarantowanej", "Działa; wnioski do 30 czerwca 2027 r. (" + link("CMS", "https://cms.law/en/pol/legal-updates/poland-enacted-law-creating-incentives-for-investing-in-renewable-energy") + ")"],
             ["System aukcyjny dla instalacji powyżej 1 MW", "Aukcje konkurencyjne z kryteriami zrównoważenia; import biometanu do 5% rocznego wolumenu", "Przyjęty przez rząd 14 lipca 2026 r.; uchwalony przez Sejm na początku września; Senat przyjął nowelizację ustawy o OZE 24 września (" + link("QCI", "https://www.qcintel.com/biofuels/article/polish-legislators-vote-for-biomethane-support-scheme-law-72371.html") + ", " + link("KPMG", "https://kpmg.com/pl/en/insights/law/energy-newsletter-biomethane-gets-a-new-support-scheme.html") + ")"],
             ["Program dotacji NFOŚiGW", "Dotacje do 45% kosztów kwalifikowanych z puli 800 mln zł (ok. 189 mln euro) z Funduszu Modernizacyjnego", "Nabór wniosków od I połowy 2026 r. (" + link("IEA Bioenergy", "https://task37.ieabioenergy.com/wp-content/uploads/sites/32/2026/04/Newsletter-T37-03_2026-Policy-issues.pdf") + ")"],
             ["Nowelizacja Prawa energetycznego", "Prostsze pozwolenia dla biogazu; bezpośrednie gazociągi biometanu tam, gdzie przyłączenie do sieci jest nieopłacalne", "Podpisana 2 kwietnia 2026 r."],
         ], cls="tbl-dense"),
         src(("Bird &amp; Bird", "https://www.twobirds.com/en/insights/2025/poland-introduces-auction-based-support-system-for-biomethane-production-in-installations-above-1-mw"),
             ("Poland Insight", "https://polandinsight.com/polands-biogas-and-biomethane-market-needs-stronger-support-to-unlock-its-full-potential-66601/")) + " oraz linki w tabeli.")}

<p>Wczesne projekty przepisów zakładały pierwszy wolumen aukcyjny na poziomie około 300 mln m³ rocznie, czyli około 3,1 TWh. Polska Organizacja Biometanu szacuje, że wystarczy to na około 50 nowych instalacji. Ostateczne wolumeny i terminy zależą od rozporządzeń wykonawczych.</p>

<h2>Portfel projektów</h2>
<p>Polska Organizacja Biometanu naliczyła na koniec III kwartału 2025 r. 122 projekty biometanowe na różnych etapach przygotowania. Oddzielnie, na koniec I kwartału 2026 r. w Krajowym Ośrodku Wsparcia Rolnictwa (KOWR) zarejestrowanych było 208 biogazowni rolniczych. Większość z nich spala biogaz, wytwarzając prąd i ciepło, a wiele można przekształcić w instalacje zatłaczające gaz do sieci. Angażuje się też kapitał publiczny: w styczniu 2026 r. Polski Zielony Fundusz podpisał z Green Gas Energy umowę o wartości 59 mln zł na dziewięć rolniczych biometanowni.</p>

<h2>Dlaczego polski biometan ma znaczenie poza Polską</h2>
<p>Polski sektor hodowlany, mleczarski i przetwórstwa spożywczego wytwarza obornik i pozostałości, czyli surowce o niskiej intensywności emisji, które uzyskują najwyższe premie w niemieckich obowiązkach transportowych i w żegludze. Popyt krajowy jest znaczący: chemia, nawozy, rafinacja, szkło, przetwórstwo spożywcze i ciepłownictwo systemowe zużywają gaz i są objęte EU ETS, CBAM, a od 2028 r. także ETS2. Dzięki bilansowi masy i unijnej bazie danych certyfikowany polski biometan można też sprzedawać odbiorcom w innych krajach UE. Do tego położenie Polski czyni ją praktyczną bazą do montażu i serwisu urządzeń dla Europy Środkowo-Wschodniej.</p>

<h2>Ryzyka</h2>
{exhibit(2, "Ryzyka realizacyjne i sposoby ich ograniczania",
         table(["Ryzyko", "Sposób ograniczenia"], [
             ["Opóźnienia rozporządzeń wykonawczych do aukcji", "Pierwsze etapy realizować w systemie do 1 MW lub z dotacją; utrzymywać pozwolenia gotowe do aukcji"],
             ["Przepustowość przyłączy do sieci", "Wykorzystać nową ścieżkę bezpośredniego gazociągu, grupować instalacje lub skraplać gaz do bio-LNG"],
             ["Konkurencja o surowiec", "Wcześnie podpisać wieloletnie umowy na obornik i pozostałości ze spółdzielniami"],
             ["Akceptacja lokalna", "Plany zarządzania zapachem, ruchem i pofermentem; dzielenie się korzyściami ze społecznościami"],
         ]),
         "Qiao Partners.")}

<h2>Perspektywy</h2>
<p>Dzisiejsza Polska przypomina Francję sprzed mniej więcej dekady: ramy prawne są gotowe, a rynek jeszcze nie zareagował. Z naszego doświadczenia taka luka zamyka się w ciągu trzech–czterech lat. Deweloperzy, dostawcy i inwestorzy, którzy zabezpieczą surowiec, grunty, przyłącza i odbiór przed rozstrzygnięciem pierwszych dużych aukcji, będą dyktować warunki tym, którzy przyjdą później.</p>
""",
)

PL = {
    "europe-energy-market-2026": P1,
    "european-biomethane-market-2026": P2,
    "biomethane-equipment-market-europe": P3,
    "china-europe-biomethane-investment": P4,
    "biomethane-revenue-stack-eu-regulation": P5,
    "poland-biomethane-market-2026": P6,
}

charts.NUM.update(group=",", dec=".")

ALT_PL = {
    "insights/crossroads.jpg": "Osoba stojąca na skrzyżowaniu, strzałki wskazują cztery kierunki",
    "insights/containers.jpg": "Ułożone kontenery morskie",
    "insights/biomethane-domes.jpg": "Biometanownia z zielonymi kopułami komór fermentacyjnych na polu",
    "insights/solar-forest-canopy.jpg": "Panele słoneczne wśród drzew, widok z góry",
    "insights/biomethane-plant-trucks.jpg": "Ciężarówki z surowcem przyjeżdżające do biometanowni",
    "insights/charging-mountain.jpg": "Szybkie ładowarki i samochód elektryczny przy górskiej drodze",
    "insights/handshake-close.jpg": "Zbliżenie biznesowego uścisku dłoni nad stołem",
    "insights/handshake-tower.jpg": "Sylwetki dwóch osób ściskających dłonie w szklanym wieżowcu",
    "insights/eu-flags-berlaymont.jpg": "Flagi UE przed budynkiem Komisji Europejskiej",
    "insights/solar-forest-aerial.jpg": "Rzędy paneli słonecznych obok lasu, widok z góry",
    "insights/wind-patchwork.jpg": "Turbina wiatrowa wśród mozaiki pól, widok z góry",
    "insights/solar-lake.jpg": "Panele słoneczne wzdłuż krętej ścieżki nad jeziorem, widok z góry",
}
